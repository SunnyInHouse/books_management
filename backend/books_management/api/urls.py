"""URLs configuration of the 'api' application."""

from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

app_name = "api"

urlpatterns = [
    path("v1/", include("api.v1.urls")),
    path(
        "doc/v1/download/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "doc/v1/redoc/",
        SpectacularRedocView.as_view(url_name="api:schema"),
        name="redoc",
    ),
    path(
        "doc/v1/swagger/",
        SpectacularSwaggerView.as_view(url_name="api:schema"),
        name="swagger",
    ),
]
