from django.urls import path
from firechat.chat.views import home_view, about_view, chat_data_view, newsletter
from firechat.utils.constants import Urls

urlpatterns = [
    path("", home_view, name=Urls.HOME_REVERSE.value),
    path("chat_data", chat_data_view, name=Urls.CHAT_DATA.value),
    path("about/", about_view, name=Urls.ABOUT_REVERSE.value),
    path("newsletter/", newsletter, name=Urls.NEWLETTER_REVERSE.value),
]
