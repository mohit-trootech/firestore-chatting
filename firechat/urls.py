from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/chat/")),
    path("chat/", include("firechat.chat.urls")),
    path("accounts/", include("firechat.accounts.urls")),
]
