from django.contrib import admin
from django.urls import path


from . import views




app_name = "services"
urlpatterns = [
    #path('indeks', views.IndexView.as_view(), name ='index')
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.ServiceListView.as_view(), name='service_list'),
    path('detail/<pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    path('category', views.CategoryView.as_view(), name='category'),
    path('create', views.ServiceCreateView.as_view(), name='service_create'),
    #path('edit/<pk>', views.edit, name='service_edit'),
    path('edit2/<pk>', views.UpdateServiceView.as_view(), name='service_edit'),
    path('delete/<pk>', views.ServiceDeleteView.as_view(), name='service_delete')
]
