from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.main.validators import validate_only_letters

from petstagram.main.validators import validate_max_file_size

"""
The user must provide the following information when uploading a pet's photo in their profile:
•	Photo - the maximum size of the photo can be 5MB
•	Tagged pets - the user should tag at least one of their pets. There is no limit in the number of tagged pets
The user may provide the following information when uploading a pet's photo in their profile:
•	Description - a user can write any description about the picture, with no limit of words/chars
Other:
•	Date and time of publication - when a picture is created (only), the date and time of publication are automatically generated.
•	Likes - each picture has 0 likes at the beginning, and no one can change it. The number of likes a picture can collect is unlimited.

"""


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max([len(x) for x,_ in GENDERS]),
        choices=GENDERS,
        null=True,
        blank=True
    )


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'

    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH
    )

    type = models.CharField(
        max_length=max((len(x) for x, _ in TYPES)),
        choices=TYPES
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    MAX_IMAGE_SIZE = 5

    photo = models.ImageField(
        validators=(
            validate_max_file_size,
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    upload_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )
