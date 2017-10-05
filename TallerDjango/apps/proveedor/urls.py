from django.conf.urls import url, include

from apps.proveedor.views import indexProveedor
from apps.proveedor.views import ProveedorList
from apps.proveedor.views import ProveedorCreate
from apps.proveedor.views import ProveedorUpdate
from apps.proveedor.views import ProveedorDelete


urlpatterns = [
	url(r'^$', indexProveedor),
	url(r'^listar$', ProveedorList.as_view(),name='proveedor_listar'),
	url(r'^nuevo$', ProveedorCreate.as_view(),name='proveedor_crear'),
	url(r'^editar/(?P<pk>\d+)/$', ProveedorUpdate.as_view(),name='proveedor_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', ProveedorDelete.as_view(),name='proveedor_eliminar'),
	

]