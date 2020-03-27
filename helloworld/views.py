 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ZldMain

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return str([[o.rocnik, o.status] for o in ZldMain.objects.all()])
