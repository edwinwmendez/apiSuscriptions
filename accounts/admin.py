from django.contrib import admin
from .models import Company, Program, Subscription, Version, City, Department


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'monthly_price', 'annual_price', 'permanent_price', 'trial_days', 'discount_percentage')
    search_fields = ('name',)
    list_filter = ('discount_percentage',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'program', 'subscription_type', 'subscription_date', 'expiration_date', 'is_active', 'price')
    search_fields = ('user__username', 'program__name')
    list_filter = ('program__name', 'subscription_type', 'is_active')


admin.site.register(Department)
admin.site.register(City)
admin.site.register(Company)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Version)
