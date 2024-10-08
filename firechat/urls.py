from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from schema_graph.views import Schema
from firechat.utils.constants import Urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/chat/"), name=Urls.INDEX_REVERSE.value),
    path("chat/", include("firechat.chat.urls")),
    path("accounts/", include("firechat.accounts.urls")),
    path("schema/", Schema.as_view()),
] + debug_toolbar_urls()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
