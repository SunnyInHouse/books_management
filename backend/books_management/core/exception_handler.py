"""Api exception handler of the 'books_management' application."""

from django.conf import settings
from rest_framework import exceptions, status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def api_exception_handler(exc, context):
    """Handle of API Exception."""

    response = exception_handler(exc, context)

    if response is None:
        response = Response(
            data="InternalServerError",
            content_type="application/json",
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    else:
        response.data = ""

    return _handle_generic_error(exc, context, response)


def _handle_generic_error(exc, context, response):
    """Generate response from all handlers."""
    if "message" not in response.data:
        response.data = {"message": response.data}

    debug_info = (
        str(exc) if (not exc.__dict__ or "detail" not in exc.__dict__) else exc.detail
    )

    if settings.DEBUG is True:
        response.data.update(
            {
                "debug_information": debug_info,
            }
        )

    headers = {}
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

    return Response(response.data, status=response.status_code, headers=headers)
