from django.db import models
from .manager import CustomManager
from api.v1.utile.models import CustomAbstractModel
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser



class User(AbstractBaseUser, PermissionsMixin, CustomAbstractModel):
    ROLE = (
        ("admin", "Admin"),
        ("user", "User"),
    )
    REGION = (
    ('Qoraqalpog‘iston Respublikasi', 'Qoraqalpog‘iston Respublikasi'), 
    ('Andijon viloyati', 'Andijon viloyati'),
    ('Buxoro viloyati', 'Buxoro viloyati'),
    ('Jizzax viloyati', 'Jizzax viloyati'), 
    ('Qashqadaryo viloyati', 'Qashqadaryo viloyati'), 
    ('Navoiy viloyati', 'Navoiy viloyati'), 
    ('Namangan viloyati', 'Namangan viloyati'), 
    ('Samarqand viloyati', 'Samarqand viloyati'), 
    ('Surxandaryo viloyati', 'Surxandaryo viloyati'), 
    ('Sirdaryo viloyati', 'Sirdaryo viloyati'), 
    ('Toshkent viloyati', 'Toshkent viloyati'), 
    ('Farg‘ona viloyati', 'Farg‘ona viloyati'), 
    ('Xorazm viloyati', 'Xorazm viloyati'), 
    ('Toshkent shahri', 'Toshkent shahri'))
    address = models.CharField(max_length=100, choices=REGION, default=REGION[13][1], blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, choices=ROLE, default=ROLE[1][1], blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
