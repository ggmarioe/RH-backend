import json
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status,permissions,viewsets

from .serializers import CustomUserSerializer, ExtraHourSerializer, MyTokenObtainPairSerializer
from rest_framework.views import APIView
from .models import CustomUser, ExtraHour

# Create your views here.
class ObtainTokenPairWithColorView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloWorldView(APIView):
    def get(self,request):
        return Response(data={'Hello': 'World'}, status=status.HTTP_200_OK)


class ExtraHourView(APIView):
    queryset = ExtraHour.objects.all()
    serializer_class = ExtraHourSerializer
    
    def get(self, request):
        extra_hours = ExtraHour.objects.all()
        serializer = ExtraHourSerializer(extra_hours, many=True)
        return Response(serializer.data)

    def post(self, request):
        form = ExtraHourSerializer(data=request.data)

        if form.is_valid(): 
            if request.method == 'POST':
                form.save()
                return Response(form.data, status=status.HTTP_201_CREATED)
                