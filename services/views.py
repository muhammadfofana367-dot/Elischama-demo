from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import ServiceForm
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')
class CreateServiceView(View):
    form_class = ServiceForm
    template_name = 'services/create_service.html'

    def get(self, request):
        form = ServiceForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.client = request.user
            service.save()
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})