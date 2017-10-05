from django.conf.urls import url, include

from apps.pago.views import indexPago
from apps.pago.views import PagoList
from apps.pago.views import PagoCreate
from apps.pago.views import PagoUpdate
from apps.pago.views import PagoDelete

urlpatterns = [
	url(r'^$', indexPago),
	url(r'^nuevo$',PagoCreate.as_view(), name='pago_crear'),
	url(r'^listar$',PagoList.as_view(), name='pago_listar'),
	url(r'^editar/(?P<pk>\d+)/$',PagoUpdate.as_view(), name='pago_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', PagoDelete.as_view(),name='pago_eliminar'),

]