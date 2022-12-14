from django.db import models

# Create your models here.
class Members(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  dob = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  phone = models.BigIntegerField()
  email = models.EmailField(primary_key=True)
  password = models.CharField(max_length=255)
  confirm_password = models.CharField(max_length=255)

class Members121(models.Model):
  fname = models.CharField(max_length=255)
  lname = models.CharField(max_length=255)
  dob = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)
  phone = models.BigIntegerField()
  email = models.EmailField(primary_key=True)
  password = models.CharField(max_length=255)
  confirm_password = models.CharField(max_length=255)