from django.core.exceptions import ValidationError


def validate_only_letters(value):
    # if not value.isalpha():
    #     raise ValidationError('value can only contain letters')

    for ch in value:
        if not ch.isalpha():
            raise ValidationError('This can contain only letters')


def validate_max_file_size(max_size):
    def validate(value):
        if value.file.size > max_size * 1024 * 1024:
            raise ValidationError(f'File size cannot exceed {max_size}MB')