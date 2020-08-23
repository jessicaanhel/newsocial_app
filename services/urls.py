from django.contrib import admin
from django.urls import path


from . import views




app_name = "services"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.ServiceListView.as_view(), name='service_list'),
    path('detail/<pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    path('category', views.CategoryView.as_view(), name='category'),
    path('create', views.ServiceCreateView.as_view(), name='service_create'),
    path('edit2/<pk>', views.UpdateServiceView.as_view(), name='service_edit'),
    path('delete/<pk>', views.ServiceDeleteView.as_view(), name='service_delete'),


]
    # path('add-to-basket', views.BasketCreateView.as_view(), name='add_to_basket'),
    # path('indeks', views.IndexView.as_view(), name ='index')
    # path('add-to-basket/<pk>', views.formularz_dodawania_do_koszyka, name='add_to_basket'),
    #path('zamowienie', views.do_koszyka, name='do_koszyka'),
    #path('<int:pk>', views.order, name = 'kosz'),
    #path('basket/<pk>', views.wysłanie_formularza_do_koszyka, name='basket'),
    # path('basket', views.BasketListView.as_view(), name='basket')