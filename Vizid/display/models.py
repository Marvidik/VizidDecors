from django.db import models
from django.utils import timezone


# Create your models here.

class Section(models.Model):
    section = models.CharField(max_length=50)
    info = models.CharField(max_length=150)
    img = models.ImageField(upload_to="section")

    def __str__(self):
        return self.section


class Sub_section(models.Model):
    sec = models.ForeignKey(Section, on_delete=models.CASCADE)
    info = models.TextField(max_length=150)
    img = models.ImageField(upload_to="sub-section")


class Comment(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.email

class Meeting(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    phone= models.CharField(max_length=11)
    date = models.DateField(default=timezone.now())
    reason=models.TextField(max_length=100)

    def __str__(self):
        return self.phone


