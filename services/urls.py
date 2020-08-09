from django.contrib import admin
from django.urls import path


from . import views




urlpatterns = [
    path('', views.ServiceView.as_view(), name='services_list'),
    path('category', views.CategoryView.as_view(), name='category'),
    path('create', views.ServiceCreateView.as_view(), name='service_create'),
    path('edit/<pk>', views.edit, name='service_edit'),
    path('edit2/<pk>', views.UpdateServiceView.as_view(), name='service_edit'),
    path('delete/<pk>', views.ServiceDeleteView.as_view(), name='services_delete')
]