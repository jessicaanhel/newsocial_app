from logging import getLogger

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from services.models import Services, Category
from services.forms import ServiceForm

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
    template_name ='category.html'
    model = Category


# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#     profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
