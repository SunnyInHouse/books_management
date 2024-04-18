"""Constants for models of 'Books' application."""

COLUMNS = [
    ("name", "name"),
    ("title", "title"),
    ("author", "author"),
    ("description", "description"),
    ("price", "price"),
]

FIELD_LIMITS_BOOKS_APP = {
    "book_name_max_char": 20,
    "book_title_max_char": 30,
    "book_author_max_char": 30,
    "book_description_max_char": 512,
    "book_price_max_digits": 5,
}

FIELD_REGEXES_BOOKS_APP = {
    "book_name": r"^[a-zA-Zа-яА-ЯёЁ0-9 _'\"()\-]+$",
    "book_author": r"^[a-zA-Zа-яА-ЯёЁ \-]+$",
    "book_title": r"^[a-zA-Zа-яА-ЯёЁ0-9 _'\"()<>[\]-]+$",
}
