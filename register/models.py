from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='userlink', unique=True)
    FirstName = models.CharField(max_length = 200, blank=True, null=True, verbose_name="First Name")
    LastName = models.CharField(max_length = 200, blank=True, null=True, verbose_name="Last Name")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length = 254, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = "{} id {}".format(self.user, self.id)
        return name

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email