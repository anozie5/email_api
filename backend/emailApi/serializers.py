from rest_framework import serializers
from .models import *

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'
        extra_kwargs = {
            'date_subscribed': {'read_only': True},
            'is_active': {'read_only': True}
        }