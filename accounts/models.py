from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.forms import ValidationError
# Create your models here.


class AccountManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have a name.')
        if not phone:
            raise ValueError('Users must have a phone.')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            phone=phone,
            name=name
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


def phone_valid(value):
    if len(str(value)) != 10:
        raise ValidationError("Phone must be 10 digits.")


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=120)
    phone = models.IntegerField(validators=[phone_valid])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'phone']

    objects = AccountManager()

    class Meta:
        db_table = 'account'

    def ___str__(self):
        return self.email
