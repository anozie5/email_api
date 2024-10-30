from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets


# Create your views here.
class Subscribe(APIView):
    def get(self, request, id=None):
        if id is None:
            suber = Subscribers.objects.all()
            sub = SubSerializer(suber, many=True)
            return Response(sub.data, status=status.HTTP_200_OK)
        
        elif id is not None:
            suber = Subscribers.objects.get(id=id)
            sub = SubSerializer(suber)
            return Response(sub.data, status=status.HTTP_200_OK)
        
        return Response({'message': f'Subscription for {suber.email} is not found', 'errors': sub.errors}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        sub = SubSerializer(data=request.data)
        if sub.is_valid():
            sub.save()
            email = sub.validated_data['email']
            return Response(f"{email}'s subscription successful", status=status.HTTP_201_CREATED)
        return Response({'message': f'Subscription for {email} failed', 'errors': sub.errors}, status=status.HTTP_400_BAD_REQUEST)

