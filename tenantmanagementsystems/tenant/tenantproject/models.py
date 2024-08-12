from django.db import models

# Create your models here.
# class student(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=10)

class register(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    photo = models.FileField(upload_to="profile")


class tenant(models.Model):
    username = models.CharField(max_length=100,default='0')
    roomno = models.IntegerField(default="0")
    tname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    occupation = models.CharField(max_length=10)
    contact = models.IntegerField(max_length=10,default="0")
    # rent = models.IntegerField(default="100")
    date = models.DateField()

class main(models.Model):
    username = models.CharField(max_length=100, default='0')
    roomno = models.IntegerField(default="0")
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=100)
    unit = models.IntegerField(max_length=10,default="0")
    amount = models.IntegerField(max_length=10,default="0")


class sub(models.Model):
    username = models.CharField(max_length=100, default='0')
    roomno = models.IntegerField(default="0")
    previous = models.IntegerField(max_length=10,)
    reading = models.IntegerField(max_length=10,)
    tmonth = models.IntegerField()
    tyear = models.IntegerField()

class tanker(models.Model):
    username = models.CharField(max_length=100, default='0')
    month = models.CharField(max_length=20)
    year = models.IntegerField(default="0")
    ttanker = models.IntegerField()
    amt = models.IntegerField()
    stenant = models.IntegerField()
