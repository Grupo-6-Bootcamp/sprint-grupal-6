from django.shortcuts import redirect, render
from django.views import View
from .forms import FormularioLogin
from django.contrib.auth import logout, login, authenticate

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
            return redirect('homeprivado')
        else:
            context = {"error": "Usuario no encontrado", 'formulario_login': FormularioLogin()}
            return render(request, 'login.html', context)
        
class CerrarSesion(View):
    def get(self, request):
        logout(request)
        return redirect('index')