from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r"^998[378]{2}|9[01345789]\d{7}$",
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        if not phone:
            raise TypeError('Invalid phone number')
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        if not password:
            raise TypeError('password no')
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=350)
    last_name = models.CharField(max_length=132, null=True, blank=True)
    phone = models.CharField(validators=[phone_regex], max_length=12, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone'

    def __str__(self):
        return self.phone
