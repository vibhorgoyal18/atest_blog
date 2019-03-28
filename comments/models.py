from django.db import models
import atest_blog.settings as settings


class Comments(models.Model):
    comment = models.TextField(blank=False)
    likes = models.IntegerField(blank=False, default=0)
    dislikes = models.IntegerField(blank=False, default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    blog = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_added',)
