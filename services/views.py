from datetime import timezone
from logging import getLogger
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


def add_to_basket(request):
    print('Funkcja uruchomiona')
    # if request.method == "POST":
    #     basket = Basket.objects.filter(buyer=request.user).first()
    #     basket.items.add(Services.objects.filter(id=pk).first())
    buyer = request.user
    id_service = request.service.pk
    return render(request, 'basket.html', {'object_list': basket_id_user, 'service_obj': basket_id_service})

class BasketCreate(CreateView):
        template_name = 'form.html'
        form_class = BasketForm
        success_url = reverse_lazy('service_list')

        def form_valid(self, form):
            basket = form.save(commit=False)
            basket.user = self.request.user
            # basket.id_service = Services.objects.filter(id=pk).first()
            basket.save()
            super().form_valid(form)

        def form_invalid(self, form):
            LOGGER.warning('User provided invalid data.')
            return super().form_invalid(form)


def wysłanie_formularza_do_koszyka(request, pk):
    service = Services.objects.filter(id=pk).first()
    #buyer = request.user.username
    basket = Basket()
    if request.method == 'POST':
        basket.id_service.add(service)
        basket_finish = AddToBasketForm(instance=basket, data=request.POST, files=request.FILES)
        if basket_finish.is_valid():
            basket_finish.save()
    else:
        basket_finish = AddToBasketForm(instance=basket)
    return render(request, 'basket.html', {'basket_form': basket_finish, 'basket': basket })




class BasketListView(ListView):
    if request.method == "POST":
        basket.id_service.add(Services.objects.filter(id=pk).first())
    template_name = 'basket.html'
    model = Basket

def koszyk(request, *args, **kwargs):
    return render(request, "basket.html", {})


def order(request):
    basket = Basket.objects(...).first()
    # Create order
    basket.items.clear()# do czyszczenia

class BasketCreateView(CreateView):
    template_name = 'form.html'
    form_class = BasketForm
    success_url = reverse_lazy('services:service_list')

    def form_valid(self, form):
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()
        super().form_valid(form)
        #return HttpResponse("Here's the text of the Web page.")

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)

def do_koszyka(request):
    if request.method == "POST":
        form = BasketForm(request.POST)
        if form.is_valid():
            zamowienie = form.save(commit=False)
            zamowienie.data_publikacji = timezone.now()
            zamowienie.save()
            return redirect('services:kosz', pk=zamowienie.pk)
        else:
            form = BasketForm()
        return render(request, 'basket.html', {'form': form})

def order(request, pk):
    zamowienie = get_object_or_404(Basket, pk=pk)
    return render(request, 'basket.html', {'zamowienie': zamowienie})

    service = Services.objects.filter(id=pk).first()
    #buyer = request.user.username
    basket = Basket()
    if request.method == 'POST':
        basket.id_service.add(service)
        basket_finish = AddToBasketForm(instance=basket, data=request.POST, files=request.FILES)
        if basket_finish.is_valid():
            basket_finish.save()
    else:
        basket_finish = AddToBasketForm(instance=basket)
    return render(request, 'basket.html', {'basket_form': basket_finish, 'basket': basket })
"""
