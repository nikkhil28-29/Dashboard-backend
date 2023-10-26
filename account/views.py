from django.shortcuts import render
from account.serializers import MyUserRegistrationSerializer,LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

from account.renderers import MyUserRenderers

# Create your views here.
class MyUserRegistrationView(APIView):
    renderer_classes=[MyUserRenderers]

    def post(self,request,format=None):
        serializer=MyUserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):   #is_valid wil call validate functiom from serializer.py
            user=serializer.save()
            return Response({'msg':'Registration Success'},
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )
    

class LoginView(APIView):
    def post(self,request,format=None):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):   #is_valid wil call validate functiom from serializer.py
            email=serializer.data.get('email')
            password=serializer.data.get('password')

            user= authenticate(email=email,password=password)
            # user=serializer.save()
            if user is not None:
                return Response({'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':'Email/Pass not Valid'}},status=status.HTTP_404_NOT_FOUND)
            

        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    
        