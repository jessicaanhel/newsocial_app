from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


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
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='PLN')
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True)
    deadline = models.DateTimeField()
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'PLN'
    def __str__(self):
        return self.title



class Basket(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #buyer = models.ForeignKey('User', verbose_name="user", related_name="clients", on_delete=models.DO_NOTHING)
    #seller = models.ForeignKey(Services.owner, on_delete=models.CASCADE)
    id_service = models.ForeignKey(Services, on_delete=models.DO_NOTHING)
    ilosc = models.FloatField(max_length=3, null=True, blank=True)
    #price = models.ForeignKey(Services.price, on_delete=models.DO_NOTHING)







