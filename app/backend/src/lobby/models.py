import uuid

from django.db import models

from account.models import Account
from video.models import VideoPlayer


class Lobby(models.Model):
    """
    Лобби с юзерами в которых просматриваются видео
    """
    users = models.ManyToManyField(Account)
    unique_id = models.UUIDField(verbose_name='Уникальный ID', default=uuid.uuid4, editable=False)
    video_player = models.ForeignKey(VideoPlayer, null=True, on_delete=models.SET_NULL)

