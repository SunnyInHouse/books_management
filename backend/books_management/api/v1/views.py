"""Viewsets of 'Api' application v1."""

from rest_framework import viewsets

from api.v1.serializers import BooksSerializer, ProfileSerializer
from api.v1.viewsets import CreateListPatchDeleteViewset, UpdateViewset
from books.models import Book, Profile


class BookViewset(CreateListPatchDeleteViewset):
    """URL requests handler to 'Books' resource endpoints."""

    name = "Books resourse"
    description = "API endpoints to manage books."

    serializer_class = BooksSerializer
    queryset = Book.objects.all()

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            profiles = Profile.objects.filter(is_visible=True).values_list(
                "column_name"
            )
            values_fields = []
            for profile in profiles:
                values_fields.append(profile[0])
            kwargs["fields"] = values_fields
        return super().get_serializer(*args, **kwargs)


class ProfileViewset(UpdateViewset):
    """URL requests handler to 'Profile' resource endpoints"""

    name = "Profilies resource"
    description = "API endpoints to manage profilies."

    lookup_field = "column_name"
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
