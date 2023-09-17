from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from mainApp.models import CompClub
from mainApp.forms import CompClubForm
# Create your views here.


class FormPageView(CreateView):
    template_name = 'mainApp/index.html'
    model = CompClub
    form_class = CompClubForm
    success_url = reverse_lazy('dummy')


class DummyPageView(TemplateView):
    template_name = 'mainApp/dummy.html'
