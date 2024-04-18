"""This module provides application administration functionality."""

from django.contrib import admin


class ListBooksManagementAdminSite(admin.AdminSite):
    """Custom admin site."""

    site_header = "BooksManagement project."
    site_title = "Books Management project'."
