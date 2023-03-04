from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Version, Program, Subscription, City
from django.contrib.auth.models import User
from .serializers import (
    CitySerializer,
    CompanySerializer,
    VersionSerializer,
    ProgramSerializer,
    SubscriptionSerializer,
    Department,
    DepartmentSerializer,
    UserSerializer)


class DepartmentList(APIView):
    """
    List all departamentos or create a new one.
    """
    def get(self, request, format=None):
        departamentos = Department.objects.all()
        serializer = DepartmentSerializer(departamentos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DepartmentDetail(APIView):
    """
    Retrieve, update or delete a departamento instance.
    """
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        departamento = self.get_object(pk)
        serializer = DepartmentSerializer(departamento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        departamento = self.get_object(pk)
        serializer = DepartmentSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        departamento = self.get_object(pk)
        departamento.delete()
        return Response(status=204)


class CityList(APIView):
    """
    List all cities or create a new one.
    """
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CityDetail(APIView):
    """
    Retrieve, update or delete a city instance.
    """
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=204)


class SubscriptionList(APIView):
    """
    List all subscriptions or create a new one.
    """
    def get(self, request, format=None):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SubscriptionDetail(APIView):
    """
    Retrieve, update or delete a subscription instance.
    """
    def get_object(self, pk):
        try:
            return Subscription.objects.get(pk=pk)
        except Subscription.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        subscription = self.get_object(pk)
        serializer = SubscriptionSerializer(subscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        subscription = self.get_object(pk)
        subscription.delete()
        return Response(status=204)


class CompanyList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    List all companies or create a new one.
    """
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CompanyDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=204)


class ProgramList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    List all programs or create a new one.
    """
    def get(self, request, format=None):
        programs = Program.objects.all()
        serializer = ProgramSerializer(programs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgramDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a program instance.
    """
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        program = self.get_object(pk)
        serializer = ProgramSerializer(program)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        program = self.get_object(pk)
        serializer = ProgramSerializer(program, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        program = self.get_object(pk)
        program.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VersionList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    List all versions or create a new one.
    """
    def get(self, request, format=None):
        versions = Version.objects.all()
        serializer = VersionSerializer(versions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VersionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class VersionDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a version instance.
    """
    def get_object(self, pk):
        try:
            return Version.objects.get(pk=pk)
        except Version.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        version = self.get_object(pk)
        serializer = VersionSerializer(version)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        version = self.get_object(pk)
        serializer = VersionSerializer(version, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk, format=None):
        version = self.get_object(pk)
        version.delete()
        return Response(status=204)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key})


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})