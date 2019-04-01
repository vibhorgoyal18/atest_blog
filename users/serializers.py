from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8,
                                     style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "last_login", "email", "first_name", "last_name", "date_joined", "is_active", "password")


class PassResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    class Meta:
        fields: '__all__'


class PassChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=32)
    new_password = serializers.CharField(max_length=32)

    class Meta:
        fields: '__all__'


class UserUpdateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields: '__all__'
