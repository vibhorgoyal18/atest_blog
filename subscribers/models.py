from django.db import models


class Subscribers(models.Model):
    mails_sent = models.IntegerField(blank=False, default=0, editable=False)
    visits = models.IntegerField(blank=False, default=1, editable=False)
    last_mail_sent = models.DateTimeField(auto_now_add=True, editable=False)
    last_visit = models.DateTimeField(auto_now_add=True)
