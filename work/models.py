from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    REGULAR_USER = 'RU'
    MODERATOR = 'MO'
    YEAR_IN_SCHOOL_CHOICES = (
        (REGULAR_USER, 'Freshman'),
        (MODERATOR, 'Sophomore'),
    )
    group = models.CharField(max_length=2,
                             choices=YEAR_IN_SCHOOL_CHOICES,
                             default=REGULAR_USER)