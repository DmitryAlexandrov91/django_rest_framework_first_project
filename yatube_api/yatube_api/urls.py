"""Эндпоинты проекта."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'api/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='docs'
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
