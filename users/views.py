from users.models import User
from users.serializers import UserSerializer, PassResetSerializer, UserUpdateSerializer, PassChangeSerializer
from users.permissions import UserPermissions
from rest_framework.permissions import IsAuthenticated
import sendgrid
from sendgrid.helpers.mail import *
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
import random
import string
from atest_blog.settings import sendgrid_apikey
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status


class CreateUserView(CreateAPIView):
    """
    create a new user
    """
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(
                email=serializer.validated_data['email'],
                first_name=serializer.validated_data['first_name'],
                last_name=serializer.validated_data['last_name'],
                password=make_password(serializer.validated_data['password'])
            )
        except Exception as exception:
            return JsonResponse({
                'success': False,
                'error': 'Error occured in registering user!'
            },
                status=500)

        return Response({'success': True}, status=status.HTTP_201_CREATED)


class UserSelfRetrieveView(RetrieveAPIView):
    """
    Get user details
    """
    serializer_class = UserSerializer
    permission_classes = [UserPermissions, ]

    def retrieve(self, request: Request, *args, **kwargs):
        serializer = UserSerializer(User.objects.filter(id=self.request.user.id), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserSelfUpdateView(UpdateAPIView):
    """
    Update user's first name and last name
    """
    serializer_class = UserUpdateSerializer
    permission_classes = [UserPermissions, ]

    def update(self, request: Request, *args, **kwargs):
        instance = User.objects.get(id=self.request.user.id)
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if 'first_name' in serializer.data:
            instance.first_name = serializer.data['first_name']

        if 'last_name' in serializer.data:
            instance.last_name = serializer.data['last_name']

        instance.save()
        return Response({'success': True}, status=status.HTTP_200_OK)


class PassResetView(CreateAPIView):
    """
    send a mail to user with updated password.
    """
    serializer_class = PassResetSerializer

    def create(self, request: Request, *args, **kwargs):
        try:
            serializer = UserSerializer(data=request.data)
            user = User.objects.get(email=serializer.data['email'])
        except Exception as exception:
            if exception.__class__.__name__ is 'DoesNotExist':
                return JsonResponse({
                    'success': False,
                    'error': 'User not found'
                },
                    status=404)
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'Error occured in retrieving user details'
                },
                    status=404)

        random_password = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        User.objects.filter(pk=user.id).update(password=make_password(random_password))
        is_password = User.objects.get(email=serializer.data['email']).check_password(random_password)

        if is_password:
            sg = sendgrid.SendGridAPIClient(apikey=sendgrid_apikey)
            from_email = Email("contact@atest.co.in")
            to_email = Email(user.email)
            subject = 'Password reset!'
            body = Content("text/plain",
                           """Hi,
                        Your password has been reset.
                        Your new password is: """ + random_password + """ 

                        Cheers,
                        Vibhor Goyal

                        Note: This is a system generated mail. Please do not revert.""")
            send_mail = Mail(from_email, subject, to_email, body)
            sg.client.mail.send.post(request_body=send_mail.get())

        return Response({'success': True}, status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    """
    Change user's password
    """
    serializer_class = PassChangeSerializer
    permission_classes = [UserPermissions, ]

    def update(self, request: Request, *args, **kwargs):
        instance = User.objects.get(id=self.request.user.id)
        serializer = PassChangeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        is_valid_password = instance.check_password(serializer.validated_data['old_password'])

        if not is_valid_password:
            return Response({'success': False, 'error': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)

        instance.password = make_password(serializer.validated_data['new_password'])
        instance.save()

        is_valid_password = instance.check_password(serializer.validated_data['new_password'])
        if not is_valid_password:
            return Response({'success': False, 'error': 'Password change failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'success': True}, status=status.HTTP_200_OK)
