from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    User Model with first and last name required, and some extra fields
    """
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )

    email = models.EmailField(_('email address'), unique=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True
    )
    profile_picture = models.FileField(null=True)
