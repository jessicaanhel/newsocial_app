from logging import getLogger
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

from services.models import Services, Category, Basket
from services.forms import ServiceForm, ServiceEditForm
from services.templatetags.service_extras import service_format

LOGGER = getLogger()

class ServiceListView(ListView):
    template_name = 'service_list.html'
    model = Services


class ServiceDetailView(DetailView):
    template_name = 'service_detail.html'
    model = Services

class ServiceDeleteView(DeleteView):
    template_name = 'service_confirm_delete.html'
    model = Services
    success_url = reverse_lazy('service:service_list')


class ServiceCreateView(CreateView):
    template_name = 'form.html'
    form_class = ServiceForm
    success_url = reverse_lazy('service:service_list')

    def form_valid(self, form):
        service = form.save(commit=False)
        service.user = self.request.user
        service.save()
        super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ServiceView(ListView):
    template_name = 'index.html'
    model = Services


class CategoryView(ListView):
    template_name = 'category.html'
    model = Category


# @login_required
# def edit(request, pk):
#     service = Services.objects.filter(id=pk).first()
#     if request.method == 'POST':
#         service_form = ServiceEditForm(instance=service, data=request.POST, files=request.FILES)
#         if service_form.is_valid():
#             service_form.save()
#     else:
#         service_form = ServiceEditForm(instance=service)
#
#     return render(request, 'service_edit.html', {'service_form': service_form})


class UpdateServiceView(UpdateView):
    template_name = "form.html"
    form_class = ServiceForm
    model = Services
    success_url = reverse_lazy('service:service_list')

    def get_object(self, queryset=None,):
        service = super().get_object(queryset)
        if service.owner != self.request.user:
            raise PermissionDenied()
        return service

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["service_form"] = context["form"]
        return context

class IndexView(ServiceListView):
    template_name = 'index.html'

"""
Koszyk
"""

def add_to_basket(request):
    print('Funkcja uruchomiona')
    # if request.method == "POST":
    #     basket = Basket.objects.filter(buyer=request.user).first()
    #     basket.items.add(Services.objects.filter(id=pk).first())
    basket_id_user = request.user
    basket_id_service = request.service.pk
    return render(request, 'basket.html', {'object_list': basket_id_user, 'service_obj': basket_id_service})


def order(request):
    basket = Basket.objects(...).first()
    # Create order
    basket.items.clear()# do czyszczenia
