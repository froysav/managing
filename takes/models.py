from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


class Phone(models.Model):
    name_model = models.TextField()
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    characteristics = models.TextField()

    def __str__(self):
        return self.name_model


class Telev(models.Model):
    name_model = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    characteristics = models.TextField()


class Laptop(models.Model):
    name_model = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    characteristics = models.TextField()
    memory = models.IntegerField()

    def __str__(self):
        return self.name_model


class Plan(models.Model):
    name_model = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    dogovor = models.BooleanField()
    email = models.EmailField()
    characteristics = models.TextField()
    memory = models.IntegerField()

    def __str__(self):
        return self.name_model


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    firm = models.CharField(max_length=100)
    model_product = models.CharField(max_length=100)
    ikpu_product = models.CharField(max_length=100)
    color_product = models.CharField(max_length=100)
    country_manufacture = models.CharField(max_length=100)
    price = models.IntegerField()

    phone = models.OneToOneField(Phone, null=True, blank=True, on_delete=models.CASCADE)
    laptop = models.OneToOneField(Laptop, null=True, blank=True, on_delete=models.CASCADE)
    telev = models.OneToOneField(Telev, null=True, blank=True, on_delete=models.CASCADE)
    plan = models.OneToOneField(Plan, null=True, blank=True, on_delete=models.CASCADE)

    def clean(self):
        filled_fields = 0

        if self.phone is not None:
            filled_fields += 1

        if self.laptop is not None:
            filled_fields += 1

        if self.telev is not None:
            filled_fields += 1

        if self.plan is not None:
            filled_fields += 1

        if filled_fields > 1:
            raise ValidationError("Only one field (phone, laptop, telev, plan) can be filled.")

    def __str__(self):
        return self.name
