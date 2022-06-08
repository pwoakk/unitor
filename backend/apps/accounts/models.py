from datetime import date

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "OTHER"
    GENDER_STATUS = (
        (GENDER_MALE, 'мужской'),
        (GENDER_FEMALE, 'женский'),
        (GENDER_OTHER, 'другое'),
    )
    username = None
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    date_birth = models.DateField('Дата рождения', default=date.today())
    gender = models.CharField(
        'Пол',
        max_length=7,
        choices=GENDER_STATUS,
        default=GENDER_OTHER,
    )
    email = models.EmailField("Email", unique=True)
    avatar = models.ImageField("Фото", upload_to="user_images/", null=True, blank=True)
    phone = models.CharField(
        'Номер телефона',
        null=True,
        max_length=10
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()