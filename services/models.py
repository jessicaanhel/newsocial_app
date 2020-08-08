from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Services(models.Model):
    title = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    rating = models.IntegerField(null=True)
    #rating = suma wszystkich ocen dzielona przez liczbe zakupow danej usługi
    bought = models.IntegerField(null=True)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    deadline = models.DateTimeField()
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title



