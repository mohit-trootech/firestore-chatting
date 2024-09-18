from django.urls import path
from firechat.chat.views import home_view, about_view
from firechat.utils.constants import Urls

urlpatterns = [
    path("", home_view, name=Urls.HOME_REVERSE.value),
    path("about/", about_view, name=Urls.ABOUT_REVERSE.value),
]
