from django.db import models
import datetime
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class CreateBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_create_blog')
    title = models.TextField()
    blog = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    objects = models.Manager()

    def __str__(self):
        return self.title

class Comments(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE, related_name='comment_user')
    post = models.ForeignKey(CreateBlog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.text



    
