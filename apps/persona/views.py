from django.views.generic import ListView, CreateView
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from apps.persona.models import Persona

from apps.persona.forms import PersonaForm

class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/persona_list.html'

class PersonaCreate(CreateView):
    model = Persona
    template_name = 'persona/persona_create.html'
    form_class= PersonaForm
    success_url = reverse_lazy('persona:Persona-list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))