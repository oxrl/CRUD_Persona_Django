from django.conf.urls import url
from apps.persona.views import PersonaListView,PersonaCreate

urlpatterns = [
    url(r'^listar$', PersonaListView.as_view(), name='Persona-list'),
    url(r'^create$', PersonaCreate.as_view(), name='Persona-create'),
]