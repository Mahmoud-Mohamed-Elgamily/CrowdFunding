from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
# User model.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=10)
    user_lname = models.CharField(max_length=10)
    user_picture = models.ImageField(upload_to="user_images/")
    user_password = models.CharField(max_length=50)


# User phone mode.

class UserPhone(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
    user_phone = models.CharField(validators=[phone_regex], max_length=11)
