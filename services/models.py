from django.db import models
from django.conf import settings
#from account.models import Profile


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
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #rating_of_user = models.OneToOneField(Profile.rating, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    city = models.ForeignKey(Cities, on_delete=models.DO_NOTHING)
    deadline = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.title



