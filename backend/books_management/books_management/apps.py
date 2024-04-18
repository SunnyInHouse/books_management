"""Configuration of 'Admin' application."""

from django.contrib.admin.apps import AdminConfig


class DevBridgeUsersServerAdminConfig(AdminConfig):
    default_site = "books_management.admin.ListBooksManagementAdminSite"
