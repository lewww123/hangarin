from django.apps import AppConfig
from django.views.generic import TemplateView

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

class HomePageView(TemplateView):
    template_name = "home.html"

class AircraftListView(TemplateView):
    template_name = "aircraft_list.html"

class AircraftCreateView(TemplateView):
    template_name = "aircraft_form.html"