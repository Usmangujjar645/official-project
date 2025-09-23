from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class longAPIview(APIView):
    def get (self ,request):
        username = request.data.get('username')
    
        password= request.data.get('password')
