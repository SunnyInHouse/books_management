"""A module containing custom validators for Django model fields."""

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class IntegerValidator:
    """Validates integer values."""

    def __init__(self, max_digits: int) -> None:
        self.max_digits = max_digits

    def __call__(self, integer_value: int):
        if self.max_digits is not None:
            self.__validate_max_digits(integer_value, self.max_digits)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, IntegerValidator)

    def __validate_max_digits(self, value: int, max_digits: int) -> None:
        """Сheck the number of digits in a number."""
        value_digits = len(str(value))
        if value_digits > max_digits:
            raise ValidationError(
                f"The max digits in number is {max_digits}."
                f"Current max digits is {value_digits}."
            )
