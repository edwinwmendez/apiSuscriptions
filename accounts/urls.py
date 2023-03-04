from django.urls import path
from django.urls import re_path as url
from django.contrib.auth.views import LoginView

from .views import (
    CompanyList,
    CompanyDetail,
    ProgramList,
    ProgramDetail,
    VersionDetail,
    VersionList,
    SubscriptionList,
    SubscriptionDetail,
    CityList,
    CityDetail,
    DepartmentList,
    DepartmentDetail,
    CustomObtainAuthToken,
    CustomAuthToken)


urlpatterns = [
    path('departamentos/', DepartmentList.as_view(), name='departamento-list'),
    path('departamentos/<int:pk>/', DepartmentDetail.as_view(), name='departamento-detail'),
    path('ciudades/', CityList.as_view(), name='city-list'),
    path('ciudades/<int:pk>/', CityDetail.as_view(), name='city-detail'),
    path('empresas/', CompanyList.as_view()),
    path('empresas/<int:pk>/', CompanyDetail.as_view()),
    path('programas/', ProgramList.as_view(), name='program-list'),
    path('programas/<int:pk>/', ProgramDetail.as_view(), name='program-detail'),
    path('versiones/', VersionList.as_view(), name='version-list'),
    path('versiones/<int:pk>/', VersionDetail.as_view(), name='version-detail'),
    path('suscripciones/', SubscriptionList.as_view(), name='subscription-list'),
    path('suscripciones/<int:pk>/', SubscriptionDetail.as_view(), name='subscription-detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    #path('api-token-auth/', CustomObtainAuthToken.as_view()),
    path('api-token-auth/', CustomAuthToken.as_view()),
]
