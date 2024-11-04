from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView 



# Create your views here.
class Subscribe(APIView):
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [permissions.IsAuthenticated()]

    #     elif self.request.method == 'POST':
    #         return [permissions.AllowAny()]
            
    #     return super().get_permissions()
    
    def get(self, request, id=None):
        self.authentication_classes = [JWTAuthentication]

        if id is None:
            suber = Subscribers.objects.all()
            sub = SubSerializer(suber, many=True)
            return Response(sub.data, status=status.HTTP_200_OK)
        
        elif id is not None:
            suber = Subscribers.objects.get(id=id)
            sub = SubSerializer(suber)
            return Response(sub.data, status=status.HTTP_200_OK)
        
        return Response({'message': f'Subscription for {sub.email} is not found', 'errors': sub.errors}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        self.permission_classes = [AllowAny]

        sub = SubSerializer(data=request.data)
        if sub.is_valid():
            sub.save()
            email = sub.validated_data['email']
            return Response(f"{email}'s subscription successful", status=status.HTTP_201_CREATED)
        return Response({'message': f'Subscription for {email} failed', 'errors': sub.errors}, status=status.HTTP_400_BAD_REQUEST)



# for your private usage
class PrivateSignUpView(generics.CreateAPIView):
    queryset = Rotate.objects.all()
    serializer_class = PrivateSignUpSerial

    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)


class PrivateLoginView(TokenObtainPairView):
    serializer_class = PrivateLoginSerial

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        
        refresh = RefreshToken.for_user(user)
        
        user_data = {
            'username': user.username,
            'email': user.email,
        }

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': user_data
        }, status= status.HTTP_200_OK)





