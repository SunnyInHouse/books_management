"""Serializers of 'Api' application v1."""

from rest_framework import serializers

from books.models import COLUMNS, Book, Profile


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class BooksSerializer(DynamicFieldsModelSerializer):
    """Serializer for working with Book objects."""

    class Meta:
        model = Book
        fields = ("id", "name", "title", "author", "description", "price")


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for working with Profile objects."""

    column_name = serializers.ChoiceField(
        choices=COLUMNS,
        read_only=True,
    )

    class Meta:
        model = Profile
        fields = ("column_name", "is_visible")
