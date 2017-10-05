from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.http import HttpResponse

from apps.reporte.forms import ReporteForm
from apps.reporte.models import Reporte
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import  UpdateView
from django.views.generic import  DeleteView

def indexReporte(request):
	return render(request,'registro_template/index.html')


class ReporteList(ListView):
	model = Reporte
	template_name = 'registro_template/registro_list.html'


class ReporteCreate(CreateView):
	model = Reporte
	form_class = ReporteForm
	template_name = 'registro_template/registro_create.html'
	success_url = reverse_lazy('Reportes:reporte_listar')


class ReporteUpdate(UpdateView):
	model = Reporte
	form_class = ReporteForm
	template_name = 'registro_template/registro_create.html'
	success_url = reverse_lazy('Reportes:reporte_listar')


class ReporteDelete(DeleteView):
	model = Reporte
	template_name = 'registro_template/registro_delete.html'
	success_url = reverse_lazy('Reportes:reporte_listar')
