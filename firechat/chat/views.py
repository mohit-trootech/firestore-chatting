from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from firechat.utils.constants import Templates


class HomeView(TemplateView):
    template_name = Templates.HOME.value


home_view = HomeView.as_view()


class AboutView(TemplateView):
    template_name = Templates.ABOUT.value


about_view = AboutView.as_view()
