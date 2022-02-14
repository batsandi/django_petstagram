from django.core.exceptions import ValidationError


def only_letters_validator(value):
    # if not value.isalpha():
    #     raise ValidationError('value can only contain letters')

    for ch in value:
        if not ch.isalpha():
            raise ValidationError('This can contain only letters')