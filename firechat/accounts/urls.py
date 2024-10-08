from django.urls import path
from firechat.accounts.views import (
    login_view,
    logout_view,
    registration_view,
    profile_view,
    users_profile_view,
    force_logout_view,
)
from firechat.utils.constants import Urls

urlpatterns = [
    path("login/", login_view, name=Urls.LOGIN_REVERSE.value),
    path("logout/", logout_view, name=Urls.LOGOUT_REVERSE.value),
    path("force_logout/", force_logout_view, name=Urls.FORCE_LOGOUT_REVERSE.value),
    path("signup/", registration_view, name=Urls.REGISTER_REVERSE.value),
    path("profile/<int:pk>", profile_view, name=Urls.PROFILE_REVERSE.value),
    path("<str:username>", users_profile_view, name=Urls.USER_PROFILE_REVERSE.value),
]
