from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=20, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    facebook = models.URLField(max_length=100, blank=True, null=True)
    instagram = models.URLField(max_length=100, blank=True, null=True)
    linkedin = models.URLField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username