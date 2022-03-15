import json

from rest_framework.views import APIView
from ..models.extra_hour import ExtraHour
from ..models.custom_user import CustomUser

from ..serializers import ExtraHourSerializer
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from ..serializers import ExtraHourSerializer

class ExtraHourView(APIView):
    queryset = ExtraHour.objects.all()
    serializer_class = ExtraHourSerializer
    
    # Get all extra hours
    def get(self, request):
        extra_hours = ExtraHour.objects.all()
        serializer = ExtraHourSerializer(extra_hours, many=True)
        return Response(serializer.data)


    # Get extra hours by id
    def extra_hour_detail(request, id):
        print(f"parametro {id}")
        result = ExtraHour.objects.all().filter(id = id)
        serializer = ExtraHourSerializer(result, many=True)
        # devolver el primer registro por defecto 
        if len(result) > 0: 
            return JsonResponse(serializer.data[0], safe=False)
        else: 
            # caso de excecpión cuando no viene data
            return JsonResponse(serializer.data, safe=False)


    # Save extra hour
    def post(self, request):
        form = ExtraHourSerializer(data=request.data)
        if form.is_valid(): 
            if request.method == 'POST':
                form.save()
                return Response(form.data, status=status.HTTP_201_CREATED)


    def patch(self, request): 
        form = ExtraHourSerializer(data= request.data)
        if form.is_valid():
            if request.method == 'PATCH':
                form.save()
                return Response(form.data, status=status.HTTP_200_OK)
    

    def put(self, request): 
        form = ExtraHourSerializer(data= request.data)
        if form.is_valid():
            if request.method == 'PUT':
                form.save()
                return Response(form.data, status=status.HTTP_200_OK)


    def extra_hour_by_username(request, username):
        user = CustomUser.objects.get(username=username)
        result = ExtraHour.objects.all().filter(user = user.id)
        serializer = ExtraHourSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def delete(self, request):
        form = ExtraHourSerializer(data= request.data)
        if form.is_valid():
            if request.method == 'DELETE':
                form.save()
                return Response(form.data, status=status.HTTP_200_OK)