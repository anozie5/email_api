from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'
        extra_kwargs = {
            'date_subscribed': {'read_only': True},
            'is_active': {'read_only': True}
        }


class PrivateSignUpSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password' : {'write_only': True, 'min_length': 8},}

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return(user)


class PrivateLoginSerial(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token

    class Meta:
        model = User
        fields = ['email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise serializers.ValidationError(f'Private user with {email} does not exist.')

            if not user.check_password(password):
                raise serializers.ValidationError('Incorrect password.')
            
            attrs['user'] = user
        else:
            raise serializers.ValidationError('Both email and password are required.')

        return attrs