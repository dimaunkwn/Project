from datetime import datetime

import jwt
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth, username and password.
        """
        if not email:
            raise TypeError('Users must have an email address.')
        if not username:
            raise TypeError('Users must have a username.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth, username and password.
        """
        if not email:
            raise TypeError('Users must have an email address.')
        if not username:
            raise TypeError('Users must have a username.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            password=password,
            is_staff=True,
            is_active=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    FEMALE = 0
    MALE = 1
    CHOICES_GENDER = (
        (FEMALE, 'Female'),
        (MALE, 'Male')

    )
    # Базовая информация
    username = models.CharField(verbose_name='Никнейм', db_index=True, null=False, max_length=255, unique=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True, default=None)
    phone_number = models.CharField(verbose_name='Номер телефона', db_index=True, max_length=11, null=True,
                                    blank=True, default=None, unique=True)
    email = models.EmailField(verbose_name='Почта', db_index=True, max_length=255, null=False, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=128, null=False, unique=False)
    firstname = models.CharField(verbose_name='Имя', max_length=255, null=True, blank=True, default=None)
    lastname = models.CharField(verbose_name='Фамилия', max_length=255, null=True, blank=True, default=None)
    gender = models.IntegerField(verbose_name='Пол', choices=CHOICES_GENDER, null=True, blank=True, default=-1)
    #  nation = models.CharField(max_length=2, choices=CHOICES_NATION, unique=False)

    # Техническая информация
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='Дата регистрации', auto_now_add=True)

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth', 'email']

    def __str__(self):
        """Для принта в консоль"""
        return self.email

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token().
        """
        return self.__generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return f'{self.firstname} {self.lastname}'

    def get_short_name(self):
        return self.username

    def get_email(self):
        # The user is identified by their email address
        return self.email

    def __generate_jwt_token(self):
        dt = datetime.now() + settings.JWT_AUTH.get('JWT_EXPIRATION_DELTA')

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
