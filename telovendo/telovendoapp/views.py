from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from .forms import FormularioProveedores
from .models import Proveedores
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index(request):
    return render(request, "index.html")

def clients(request):
    clientes = [
        {
            "id": 1,
            "nombre": "Diego",
            "apellido": "Herrera",
            "email": "diego.herrer@email.cl",
            "edad": 25,
            "telefono": "31245698"
        },
        {
            "id": 2,
            "nombre": "Nicolas",
            "apellido": "Castro",
            "email": "nico.castro@email.cl",
            "edad": 28,
            "telefono": "31245864"
        },
        {
            "id": 3,
            "nombre": "Carolina",
            "apellido": "Vargas",
            "email": "caro.vargas@email.cl",
            "edad": 35,
            "telefono": "31663864"
        },
        {
            "id": 4,
            "nombre": "Valentina",
            "apellido": "Fernandez",
            "email": "vale.fer@email.cl",
            "edad": 30,
            "telefono": "2654815"
        },
        {
            "id": 5,
            "nombre": "Sebastian",
            "apellido": "Lopez",
            "email": "seba.lopez@mail.cl",
            "edad": 28,
            "telefono": "91856864"
        }
    ]
    return render(request, "clients.html", {"clientes": clientes})

class CrearProveedorView(View):
    template_name = "formulario.html"

    def get(self, request):
        form = FormularioProveedores()
        context = {'form': form}
        return render(request, 'formulario.html', context)

    def post(self, request):
        form = FormularioProveedores(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
        else:
            context = {'form': form}
            return render(request, 'formulario.html', context)


class ProveedoresView(TemplateView):
    template_name = "proveedores.html"

    def get(self, request):
        proveedores = Proveedores.objects.all()
        context = {"proveedores": proveedores}
        return render(request, "proveedores.html", context)


@method_decorator(login_required, name='dispatch')
class IndexPageView(TemplateView):
    template_name = "indexp.html"

    def get(self, request):
        return render(request, "indexp.html")

    def post(self, request):
        return render(request, "indexp.html")