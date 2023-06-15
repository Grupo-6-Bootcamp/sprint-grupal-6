from django.shortcuts import redirect, render
from django.views import View
from .forms import FormularioLogin
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        context = {'formulario_login': FormularioLogin()}
        return render(request, "login.html", context)

    def post(self, request):
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            context = {"error": "Usuario no encontrado",
                       'formulario_login': FormularioLogin()}
            return render(request, 'login.html', context)
        
@method_decorator(login_required, name='dispatch')
class CerrarSesion(View):
    def get(self, request):
        logout(request)
        return redirect('index')