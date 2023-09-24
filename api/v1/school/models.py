from django.db import models
from api.v1.utile.models import CustomAbstractModel
from api.v1.user.models import User


class School(CustomAbstractModel):
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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100, choices=REGION)
    direction = models.TextField(blank=True, null=True)
    descripton = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name


class SchoolImage(CustomAbstractModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="school_images/")
    
    def __str__(self) -> str:
        return f"{self.school}"
