import uuid

from django.db import models

from account.models import Account


class Video(models.Model):
    """
    Видео
    """
    unique_id = models.UUIDField(verbose_name='Уникальный ID', default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Название', max_length=255)
    author = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL)
    description = models.TextField(verbose_name='Описание')
    duration = models.IntegerField(verbose_name='Длительность')  # В секундах
    date_upload = models.DateTimeField(verbose_name='Дата загрузки', auto_created=True)


class VideoPlayer(models.Model):
    """
    Видео-плеер
    """
    video = models.ForeignKey(Video, null=True, on_delete=models.CASCADE)
    time_code = models.IntegerField(verbose_name='Тайм код')

    class Meta:
        abstract = True


class UserVideoPlayer(VideoPlayer):
    watcher = models.ForeignKey(Account, on_delete=models.CASCADE)


class LobbyVideoPlayer(VideoPlayer):
    watcher = models.OneToOneRel()


class Comment(models.Model):
    """
    Комментарий
    """
    author = models.ForeignKey(Account, on_delete=models.SET_NULL)
    text = models.TextField(verbose_name='Текст')
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    is_deleted = models.BooleanField()
