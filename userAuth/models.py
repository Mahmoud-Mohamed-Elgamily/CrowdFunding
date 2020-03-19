from django.db import models
from django.core.validators import RegexValidator


class UserPhone (models.Model):
    phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
    user_phone = models.CharField(validators=[phone_regex], max_length=11)


class User (models.Model):
    user_fname = models.CharField(max_length=10)
    user_lname = models.CharField(max_length=10)
    user_picture = models.ImageField(upload_to="user_images/")
    user_password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_fname


class UserPhone (models.Model):
    phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
    user_phone = models.CharField(validators=[phone_regex], max_length=11)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id.user_fname}'s phone number {self.user_phone}"
