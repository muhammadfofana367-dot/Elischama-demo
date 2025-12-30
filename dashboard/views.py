from django.shortcuts import render
from django.views import View
from services.models import Service
from accounts.models import CustomUser
from accounts.forms import CustomUserChangeForm
from django.contrib.auth import get_user

# Create your views here.


class DashboardView(View):
    template_name = 'dashboard.html'
    

    def get(self, request):
        form_class = CustomUserChangeForm(instance=request.user)
        context = {
            'form_usuario': form_class,
        }
        return render(request, self.template_name, context)


class EditProfileView(View):
    form_class = CustomUserChangeForm
    template_name = 'profil/edit_profile.html'

    def get(self, request):
        user = request.user
        form = self.form_class(instance=user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = request.user
        form = self.form_class(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'form': form, 'success': True})
        return render(request, self.template_name, {'form': form})