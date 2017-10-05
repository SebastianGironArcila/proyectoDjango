from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
# Create your views here.
from apps.pago.forms import PagoForm
from apps.pago.models import Pago
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import  UpdateView
from django.views.generic import  DeleteView

def indexPago(request):
	return render(request,"pago_template/index.html")


class PagoList(ListView):
	model = Pago
	template_name = 'pago_template/pago_list.html'


class PagoCreate(CreateView):
	model = Pago
	form_class = PagoForm
	template_name = 'pago_template/pago_create.html'
	success_url = reverse_lazy('Pagos:pago_listar')


class PagoUpdate(UpdateView):
	model = Pago
	form_class = PagoForm
	template_name = 'pago_template/pago_create.html'
	success_url = reverse_lazy('Pagos:pago_listar')


class PagoDelete(DeleteView):
	model = Pago
	template_name = 'pago_template/pago_delete.html'
	success_url = reverse_lazy('Pagos:pago_listar')
