from json import dumps

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from django.db.utils import OperationalError

from .models import ZldMain

# Create your views here.
class HomePageView(View):
    def get(self, request, **kwargs):
        try:
            data = dumps([[o.rocnik, o.status] for o in ZldMain.objects.all()])
        except OperationalError:
            if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.mysql':
                raise
            data = dumps([])

        return HttpResponse(data, content_type='application/json')
