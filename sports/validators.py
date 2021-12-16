from django.core.exceptions import ValidationError


def validate_field_number(value: int) -> None:
    if not value >= 1:
        raise ValidationError('Field number can\'t be less than 1')


def validate_id_center(value: int) -> None:
    if not value >= 1:
        raise ValidationError('Id Center field can not be -ve')


def validate_center_name(value: str) -> None:
    if len(value) < 3:
        raise ValidationError('Center name can\'t be blank')
    elif len(value) > 100:
        raise ValidationError('Center name\'s length can\'t be more than 100')


def validate_phone_number(value: int) -> None:
    if value < 500:
        raise ValidationError('Are you sure that is a phone number ?')


def validate_length(value: str) -> None:
    if len(value) == 0:
        raise ValidationError("Field must not be empty")


def validate_id(value: int) -> None:
    if value <= 0:
        raise ValidationError("The ID must be non-negative")


def validate_price(value: int) -> None:
    if not value >= 0:
        raise ValidationError('Price can\'t be negative')
    if not value <= 500:
        raise ValidationError('Price can\'t be greater than 1,000,000.00')