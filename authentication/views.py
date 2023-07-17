from django.shortcuts import render
from django.contrib.auth import authenticate
from .models import User
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .tokens import create_jwt_pair_for_user


class UserCreationView(generics.GenericAPIView):
    serializer_class=serializers.UserCreationSerializer

    @swagger_auto_schema(operation_summary="Create a user account by signing Up")
    def post(self,request):

        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    serializer_class= serializers.LoginSerializer
    queryset=User.objects.all()

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)
    

