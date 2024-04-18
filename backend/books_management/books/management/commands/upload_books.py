"""Django-admin command to upload books to database from csv."""

import csv

from django.core.management.base import BaseCommand

from books.models import Book


class Command(BaseCommand):
    """Command to upload books to database from csv."""

    help = "Upload books to database from csv"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        file_path = options["file"]

        with open(file_path, "r") as csv_file:
            for row in csv.reader(csv_file):
                print(row)
                _, created = Book.objects.get_or_create(
                    name=row[0],
                    title=row[1],
                    author=row[2],
                    description=row[3],
                    price=row[4],
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(f'Book "{row[0]}" has been created.')
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f'Book "{row[0]}" already exists.')
                    )

        self.stdout.write(self.style.SUCCESS("Books have been loaded successfully."))
