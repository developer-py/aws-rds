from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    aadhar = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.name
