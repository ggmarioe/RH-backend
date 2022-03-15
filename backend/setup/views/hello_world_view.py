from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorldView(APIView):
    def get(self,request):
        return Response(data={'Hello': 'World'}, status=status.HTTP_200_OK)