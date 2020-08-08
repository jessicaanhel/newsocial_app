from django.db import models
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    bio = models.TextField()


    def __str__(self):
        return 'Profil użytkownika {}.'.format(self.user.username)


