from datetime import timezone, datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Department(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'


class City(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    address = models.CharField(max_length=255, verbose_name='Dirección', null=True, blank=True)
    ciudad = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    # Agrega más campos aquí según sea necesario

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class CustomUser(AbstractUser):
    # Atributo para diferenciar el campo "groups" en el modelo CustomUser
    groups = models.ManyToManyField(
        Group,
        verbose_name="Grupos",
        blank=True,
        help_text="Los grupos a los que pertenece este usuario.",
        related_name="custom_user_set",
        related_query_name="custom_user"
    )

    # Atributo para diferenciar el campo "user_permissions" en el modelo CustomUser
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="Permisos de usuario",
        blank=True,
        help_text="Los permisos específicos de este usuario.",
        related_name="custom_user_set",
        related_query_name="custom_user"
    )


class Program(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción', null=True, blank=True)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio mensual', null=True, blank=True)
    annual_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio anual', null=True, blank=True)
    permanent_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio permanente', null=True, blank=True)
    trial_days = models.IntegerField(default=0, verbose_name='Días de prueba', null=True, blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Porcentaje de descuento')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'


class Version(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Programa')
    number = models.CharField(max_length=255, verbose_name='Número')
    release_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de lanzamiento')
    release_notes = models.TextField(blank=True, null=True, verbose_name='Notas de la versión')
    file = models.FileField(upload_to='versions/', verbose_name='Archivo', null=True, blank=True)

    def __str__(self):
        return f'{self.program} - {self.number}'

    class Meta:
        verbose_name = 'Versión'
        verbose_name_plural = 'Versiones'


class Subscription(models.Model):
    USER_SUBSCRIPTION_TYPE_CHOICES = [
        ('monthly', 'Mensual'),
        ('annual', 'Anual'),
        ('permanent', 'Permanente'),
        ('trial', 'Prueba')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Programa')
    subscription_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de suscripción')
    expiration_date = models.DateTimeField(verbose_name='Fecha de vencimiento', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Activa')
    subscription_type = models.CharField(max_length=20, choices=USER_SUBSCRIPTION_TYPE_CHOICES, default='monthly', verbose_name='Tipo de suscripción')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio de la suscripción', blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.program} - {self.subscription_type}'

    class Meta:
        verbose_name = 'Suscripción'
        verbose_name_plural = 'Suscripciones'

    def save(self, *args, **kwargs):
        if self.subscription_type == 'trial':
            self.price = 0
            self.expiration_date = timezone.now() + timezone.timedelta(days=self.program.trial_days)
        else:
            if self.subscription_type == 'monthly':
                self.price = self.program.monthly_price
                self.expiration_date = timezone.now() + timezone.timedelta(days=30)
            elif self.subscription_type == 'annual':
                self.price = self.program.annual_price
                self.expiration_date = timezone.now() + timezone.timedelta(days=365)
            else:
                self.price = self.program.permanent_price
                self.expiration_date = None

            if self.subscription_type == 'annual' or self.subscription_type == 'permanent':
                self.price = self.price - (self.price * self.program.discount_percentage / 100)

        super(Subscription, self).save(*args, **kwargs)