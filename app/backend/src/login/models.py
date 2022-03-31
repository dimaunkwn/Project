from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Create your models here.


class UserModel(AbstractBaseUser):
    FEMALE = 0
    MALE = 1
    CHOICES_GENDER = (
        (FEMALE, 'FEMALE'),
        (MALE, 'MALE')

    )

    date_of_birth = models.DateField()
    # phone_number = models.IntegerField(min_lenght=11, max_length=11, unique=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(min_length=8, max_length=25, unique=False)
    firstname = models.CharField(max_length=255, unique=False)
    lastname = models.CharField(max_length=255, unique=False)
    gender = models.IntegerField(choices=CHOICES_GENDER)
    #  nation = models.CharField(max_length=2, choices=CHOICES_NATION, unique=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth', 'email']

    def get_email(self):
        # The user is identified by their email address
        return self.email

    def get_full_name(self):
        # The user is identified by their username
        return self.username

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth, username and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth, username and password.
        """
        user = self.create_user(email,
                                username=username,
                                password=password,
                                date_of_birth=date_of_birth
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user
