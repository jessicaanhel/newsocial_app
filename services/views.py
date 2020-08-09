from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from services.models import Services, Category
from services.forms import ServiceForm, ServiceEditForm

LOGGER = getLogger()

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


# @login_required
# def edit(request):
#     if request.method == 'POST':
#         service_form = ServiceEditForm(instance=request.user, data=request.POST, files=request.FILES)
#         if service_form.is_valid():
#             service_form.save()
#     else:
#         service_form = ServiceEditForm(instance=request.user)
#
#     return render(request, 'services/service_edit.html', {'service_form': service_form})
