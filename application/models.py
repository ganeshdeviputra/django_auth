from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
