 # helloworld/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

from django.db.utils import OperationalError

from .models import ZldMain

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        try:
            return str([[o.rocnik, o.status] for o in ZldMain.objects.all()])
        except OperationalError:
            return []
