from django.contrib import admin
from django.urls import path

from services.models import Category, Cities, Services
from . import views


admin.site.register(Category)
admin.site.register(Cities)
admin.site.register(Services)

urlpatterns = [
    path('', views.ServiceView.as_view(), name='services_list'),
    path('category', views.CategoryView.as_view(), name='category'),
    path('create', views.ServiceCreateView.as_view(), name='service_create'),
#    path('edit', views.ServiceEditForm.as_view(), name='service_edit')
]
