from django.shortcuts import render
from rest_framework import generics
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserLoginSerializer
from django.contrib.auth import authenticate

# Create your views here.

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
