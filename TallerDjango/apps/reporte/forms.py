from django import forms
from apps.reporte.models import Reporte

class ReporteForm(forms.ModelForm):

	class Meta:
		model = Reporte

		fields = [

			'cantidadEntregasAnuales',
			'año',
			'registrante',
			'proveedor',
		]

		labels = {

			'cantidadEntregasAnuales':'Cantidad de Envios Anuales',
			'año':'Año',
			'registrante':'Nombre del Registrador',
			'proveedor':'Proveedor',
		}

		widgets = {

			'cantidadEntregasAnuales':forms.TextInput(attrs = {'class':'form-control'}),
			'año':forms.TextInput(attrs = {'class':'form-control'}),
			'registrante':forms.TextInput(attrs = {'class':'form-control'}),
			'proveedor':forms.Select(attrs = {'class':'form-control'}),


		}
