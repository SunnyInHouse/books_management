"""Custom viewsets."""

from rest_framework import mixins, viewsets


class CreateListPatchDeleteViewset(viewsets.ModelViewSet):
    """The viewset allows methods: GET, POST, PATCH, DELETE."""

    http_method_names = (
        "get",
        "post",
        "patch",
        "delete",
    )


class UpdateViewset(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """The viewset allows methods: GET, PATCH."""

    http_method_names = (
        "get",
        "patch",
    )
