from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'password')
        # extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            # user = User(username=validated_data['username'],
            #             email=validated_data['email'],
            #             first_name=validated_data['first_name'],
            #             last_name=validated_data['last_name'])
            #
            # user.set_password(validated_data['password'])
            # user.save()
            # return user
            username = validated_data['username']
            email = validated_data['email']
            first_name = validated_data['first_name']
            last_name = validated_data['last_name']
            password = make_password(validated_data.get('password'))

        # def update(self, instance, validated_data):
        #     instance.email = validated_data.get('email', instance.email)
        #     instance.username = validated_data.get('username', instance.username)
        #     instance.first_name = validated_data.get('first_name', instance.first_name)
        #     instance.last_name = validated_data.get('last_name', instance.last_name)
        #     instance.password = (make_password(validated_data.get('password')), instance.password)
        #     instance.save()
        #     return instance
