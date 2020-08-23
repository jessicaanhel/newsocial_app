from django.contrib import admin
from services.models import Category, Cities, Services, Basket
# Register your models here.
admin.site.register(Category)
admin.site.register(Cities)
admin.site.register(Services)
admin.site.register(Basket)