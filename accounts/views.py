from django.shortcuts import render, redirect
from django.views import View
from .forms import UsuarioCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(login_required, name='dispatch')
class PerfilView(View):
    def get(self, request):
        return render(request, 'paginas/perfil.html')
    def post(self, request):
        # Lógica para manejar la actualización del perfil
        pass


class RegistroView(View):
    template_name = 'paginas/registro.html'

    def get(self, request):
        form_class = UsuarioCreationForm()
        return render(request, self.template_name, {'form': form_class})
    
    def post(self, request):
        # Lógica para manejar el registro de un nuevo usuario
        form_class= UsuarioCreationForm(request.POST)

        if form_class.is_valid():
            form_class.save()
            # Redirigir a la página de inicio de sesión u otra página después del registro exitoso
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form_class})
    