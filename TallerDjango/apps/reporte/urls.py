from django.conf.urls import url, include

from apps.reporte.views import indexReporte
from apps.reporte.views import ReporteList
from apps.reporte.views import ReporteCreate
from apps.reporte.views import ReporteUpdate
from apps.reporte.views import ReporteDelete

urlpatterns = [
	url(r'^$', indexReporte),
	url(r'^nuevo$',ReporteCreate.as_view(), name='reporte_crear'),
	url(r'^listar$',ReporteList.as_view(), name='reporte_listar'),
	url(r'^editar/(?P<pk>\d+)/$',ReporteUpdate.as_view(), name='reporte_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', ReporteDelete.as_view(),name='reporte_eliminar'),

]