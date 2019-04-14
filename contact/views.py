from rest_framework.generics import CreateAPIView
from django.http import JsonResponse
import sendgrid
from sendgrid.helpers.mail import *
from contact.serializers import ContactSerializer
from atest_blog.settings import sendgrid_apikey
from rest_framework.request import Request


class ContactView(CreateAPIView):
    serializer_class = ContactSerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sg = sendgrid.SendGridAPIClient(apikey=sendgrid_apikey)
        from_email = Email(serializer.data['email'])
        to_email = Email("vibhor.goyal@atest.co.in")
        subject = serializer.data['subject']
        body = Content("text/plain", serializer.data['body'])
        send_mail = Mail(from_email, subject, to_email, body)
        sg.client.mail.send.post(request_body=send_mail.get())

        from_email = Email("contact@atest.co.in")
        to_email = Email(serializer.data['email'])
        subject = 'Thanks for contacting aTest!'
        body = Content("text/plain",
                       """Hi,
                    Thanks for contacting. I will try to revert to your mail as soon as possible.

                    Cheers,
                    Vibhor Goyal

                    Note: This is a system generated mail. Please do not revert.""")
        send_mail = Mail(from_email, subject, to_email, body)
        sg.client.mail.send.post(request_body=send_mail.get())

        return JsonResponse({'success': True}, status=200)
