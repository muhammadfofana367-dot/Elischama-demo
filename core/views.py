from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class HomeView(View):
    template_name = 'pages/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class ServiceView(View):
    template_name = 'pages/service.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class TrainingView(View):
    template_name = 'pages/training.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class AboutView(View):
    template_name = 'pages/about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    

class ContactView(View):
    template_name = 'pages/contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)