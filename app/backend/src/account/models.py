from django.db import models
from django.contrib.auth import get_user_model


class Account(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', max_length=255, db_index=True)

    is_blocked = models.BooleanField()
    is_verified = models.BooleanField()
