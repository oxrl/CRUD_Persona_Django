from django.conf.urls import url
from apps.persona.views import PersonaListView,PersonaCreate,PersonaEditar,PersonaEliminar

urlpatterns = [
    url(r'^listar$', PersonaListView.as_view(), name='Persona-list'),
    url(r'^create$', PersonaCreate.as_view(), name='Persona-create'),
    url(r'^editar/(?P<pk>\d+)$', PersonaEditar.as_view(), name='persona_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', PersonaEliminar.as_view(), name='persona_eliminar'),
]
