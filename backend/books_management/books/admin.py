"""Admin site settings of the 'Books' application."""

from django.contrib import admin

from books.models import Book, Profile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Settings for presenting 'Book' model on the admin site."""

    list_display = ("id", "name", "author", "price")
    search_fields = (
        "name",
        "author",
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Settings for presenting 'Book' model on the admin site."""

    list_display = ("id", "column_name", "is_visible")
    search_fields = ("column_name",)
