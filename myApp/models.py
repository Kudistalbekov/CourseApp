from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    imgpath=models.CharField(max_length=100,default="nodata")
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    logo=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longtitude = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    branchers = models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.address

class Contact(models.Model):
    PHONE = 1
    FACEBOOK = 2
    EMAIL = 3
    CHOICES = (
        (PHONE,'PHONE'),(FACEBOOK,'FACEBOOK'),(EMAIL,'EMAIL'),
    )
    type = models.IntegerField(choices=CHOICES)
    value=models.CharField(max_length=100)
    contacts=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='contact')
    def __str__(self):
        return self.contacts