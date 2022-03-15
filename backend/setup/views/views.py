import json
from urllib.robotparser import RequestRate
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status,permissions,viewsets, decorators

from ..models.custom_user import CustomUser
from ..models.extra_hour import ExtraHour
from ..serializers import MyTokenObtainPairSerializer

# from .views.extra_hour_view import ExtraHourView

# Create your views here.
class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer





