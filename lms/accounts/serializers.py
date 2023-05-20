from rest_framework import serializers
from .models import User, phone_regex


class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[phone_regex], max_length=12)
    code = serializers.IntegerField(max_value=9999)
    password = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=123)
    name = serializers.CharField(max_length=123)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']

    phone = serializers.CharField(max_length=13)


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()


class ResetPasswordSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)


class ResetPasswordConfirmSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    password = serializers.CharField(max_length=64)


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'old_password']

    password = serializers.CharField(max_length=64, write_only=True)
    old_password = serializers.CharField(max_length=64, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'name', 'last_name']

    phone = serializers.CharField(max_length=13, validators=[phone_regex])
    id = serializers.IntegerField(read_only=True)