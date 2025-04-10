from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import LoginSerializer, RegisterSerializer, ListUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class LoginUserView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except Exception as e:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class GetUsersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RegisterSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = ListUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def get(self, request):
    #     users = ListUserSerializer
    #     serializer = self.serializer_class(users, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)