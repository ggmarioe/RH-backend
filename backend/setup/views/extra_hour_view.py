import json
from ..models.extra_hour import ExtraHour
from ..models.custom_user import CustomUser
from ..serializers import ExtraHourSerializer
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ExtraHourView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ExtraHourSerializer
    
    # get the extra hour 
    # if any params are added it will return the extra hour with the params
    # if no params are added it will return all the extra hours
    def get(self,request, *args, **kwargs):
        id = request.query_params.get('id')

        if id != None: 
            #consulta por id 
            extra_hours = ExtraHour.objects.get(id = id)
            serializer = ExtraHourSerializer(extra_hours)
            return Response(serializer.data)

        extra_hours = ExtraHour.objects.all()
        serializer = ExtraHourSerializer(extra_hours, many=True)
        return Response(serializer.data)


    # Save extra hour
    def post(self, request):
        form = ExtraHourSerializer(data=request.data)

        if not form.is_valid():
            print(request.data)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

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
    

    def delete(self, request):
        form = ExtraHourSerializer(data= request.data)
        if form.is_valid():
            if request.method == 'DELETE':
                form.save()
                return Response(form.data, status=status.HTTP_200_OK)