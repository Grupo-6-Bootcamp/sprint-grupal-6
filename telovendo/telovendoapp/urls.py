from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('formulario/', views.CrearProveedorView.as_view(),
         name='registro_proveedores'),
    path('proveedores/', views.ProveedoresView.as_view(), name='proveedores'),
    path('indexp/', views.IndexPageView.as_view(), name='homeprivado'),
]
