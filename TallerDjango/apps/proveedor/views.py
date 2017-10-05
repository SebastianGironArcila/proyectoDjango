from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import  UpdateView
from django.views.generic import  DeleteView
from apps.proveedor.models import Proveedor
from apps.proveedor.forms import ProveedorForm


def indexProveedor(request):
	return render(request,'proveedor_template/index.html')


class ProveedorList(ListView):
	model = Proveedor
	template_name = 'proveedor_template/proveedor_list.html'


class ProveedorCreate(CreateView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'proveedor_template/proveedor_create.html'
	success_url = reverse_lazy('Proveedores:proveedor_listar')


class ProveedorUpdate(UpdateView):
	model = Proveedor
	form_class = ProveedorForm
	template_name = 'proveedor_template/proveedor_create.html'
	success_url = reverse_lazy('Proveedores:proveedor_listar')


class ProveedorDelete(DeleteView):
	model = Proveedor
	template_name = 'proveedor_template/proveedor_delete.html'
	success_url = reverse_lazy('Proveedores:proveedor_listar')
