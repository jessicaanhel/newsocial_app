from logging import getLogger
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from services.models import Services, Category
from services.forms import ServiceForm, ServiceEditForm

LOGGER = getLogger()


class ServiceDeleteView(DeleteView):
    template_name = 'service_confirm_delete.html'
    model = Services
    success_url = reverse_lazy('index')



class ServiceCreateView(CreateView):
    template_name = 'form.html'
    form_class = ServiceForm
    success_url = reverse_lazy('service_create')

    def form_valid(self, form):
        service = form.save(commit=False)
        service.user = self.request.user
        service.save()
        super().form_valid(form)

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ServiceView(ListView):
    template_name = 'services.html'
    model = Services


class CategoryView(ListView):
    template_name = 'category.html'
    model = Category


@login_required
def edit(request, pk):
    service = Services.objects.filter(id=pk).first()
    if request.method == 'POST':
        service_form = ServiceEditForm(instance=service, data=request.POST, files=request.FILES)
        if service_form.is_valid():
            service_form.save()
    else:
        service_form = ServiceEditForm(instance=service)

    return render(request, 'service_edit.html', {'service_form': service_form})


class UpdateServiceView(UpdateView):
    template_name = "service_edit.html"
    form_class = ServiceEditForm
    model = Services

    def get_object(self, queryset=None,):
        service = super().get_object(queryset)
        if service.owner != self.request.user:
            raise PermissionDenied()
        return service

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["service_form"] = context["form"]
        return context
