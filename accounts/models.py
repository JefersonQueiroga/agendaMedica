from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser
from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models


class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, cpf, password=None):
        if not email:
            raise ValueError("Users must have email address")
        if not username:
            raise ValueError("Users must have username")
        if not cpf:
            raise ValueError("Users must have CPF")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            cpf=cpf
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, cpf, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            cpf=cpf
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=100, db_index=True)
    username = models.CharField(max_length=30, unique=True, help_text="Username",blank=True)
    telefone=models.CharField(max_length=14, null=True, blank=True, help_text="Phone number", validators=[
                                RegexValidator(regex='[0-9]{10}', message="Enter a valid Phone Number", code="invalid_phoneNum")])
    dataNascimento = models.DateField(null=True)
    cpf = models.CharField(max_length=30)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True,null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','cpf']

    objects = UsuarioManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(elf, app_label):
        return True