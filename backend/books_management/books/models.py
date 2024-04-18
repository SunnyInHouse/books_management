"""Database settings of the 'Books' application."""

from typing import Iterable
from django.core.validators import RegexValidator
from django.db import models

from books.validators import IntegerValidator
from core.constants import COLUMNS, FIELD_LIMITS_BOOKS_APP, FIELD_REGEXES_BOOKS_APP


class Book(models.Model):
    """Model Book."""

    name = models.CharField(
        "book name",
        help_text="book name",
        max_length=FIELD_LIMITS_BOOKS_APP["book_name_max_char"],
        unique=True,
        validators=(RegexValidator(FIELD_REGEXES_BOOKS_APP["book_name"]),),
    )
    title = models.CharField(
        "book title",
        help_text="book title",
        max_length=FIELD_LIMITS_BOOKS_APP["book_title_max_char"],
        blank=True,
        validators=(RegexValidator(FIELD_REGEXES_BOOKS_APP["book_title"]),),
    )
    author = models.CharField(
        "book author",
        help_text="book author",
        max_length=FIELD_LIMITS_BOOKS_APP["book_author_max_char"],
        validators=(RegexValidator(FIELD_REGEXES_BOOKS_APP["book_author"]),),
    )
    description = models.TextField(
        "book description",
        help_text="book description",
        max_length=FIELD_LIMITS_BOOKS_APP["book_description_max_char"],
        blank=True,
    )
    price = models.PositiveIntegerField(
        "book price",
        help_text="book price",
        validators=(
            IntegerValidator(
                max_digits=FIELD_LIMITS_BOOKS_APP["book_price_max_digits"]
            ),
        ),
    )

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Profile(models.Model):
    """Model Profile."""

    column_name = models.CharField(
        "name of column",
        choices=COLUMNS,
        unique=True,
    )
    is_visible = models.BooleanField(
        "visible status of column",
    )

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profilies"
        ordering = ("id",)

    def __str__(self):
        return f"{self.column_name} visibility is {self.is_visible}"
