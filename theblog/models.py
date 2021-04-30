from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    Action=models.CharField(max_length=10,default="update")
    def __str__(self):
        return self.title+'.|.'+str(self.author)