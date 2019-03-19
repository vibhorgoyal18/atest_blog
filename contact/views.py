from rest_framework import viewsets
from django.http import JsonResponse
import sendgrid
from sendgrid.helpers.mail import *
import re


class SendMail(viewsets.ViewSet):

    def create(self, request):
        sg = sendgrid.SendGridAPIClient(
            apikey='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')
        if 'email' not in request.data:
            return JsonResponse({"success": False, "error": "Parameter named 'email' is not found"}, status=400)
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', request.data['email'])
        if match is None:
            return JsonResponse({"success": False, "error": "Email address is not valid"}, status=400)
        from_email = Email(request.data['email'])
        to_email = Email("vibhor.goyal@atest.co.in")
        if 'subject' not in request.data:
            return JsonResponse({"success": False, "error": "Parameter named 'subject' is not found"}, status=400)
        subject = request.data['subject']
        if 'body' not in request.data:
            return JsonResponse({"success": False, "error": "Parameter named 'body' is not found"}, status=400)
        body = Content("text/plain", request.data['body'])
        send_mail = Mail(from_email, subject, to_email, body)
        sg.client.mail.send.post(request_body=send_mail.get())

        from_email = Email("contact@atest.co.in")
        to_email = Email(request.data['email'])
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
