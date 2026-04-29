from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phoneno = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.firstname