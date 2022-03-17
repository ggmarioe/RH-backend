from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from ..serializers import CustomUserSerializer

class CustomUserCreate(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        