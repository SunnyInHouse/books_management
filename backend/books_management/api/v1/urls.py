"""URLs configuration of 'Api' application v1."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import BookViewset, ProfileViewset

router_v1 = DefaultRouter()

router_v1.register("book", BookViewset, basename="book")
router_v1.register("profile", ProfileViewset, basename="profile")


urlpatterns = [
    path("", include(router_v1.urls)),
]
