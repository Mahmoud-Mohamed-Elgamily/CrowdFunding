from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.


class UserPhone(models.Model):
    phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
    user_phone = models.CharField(validators=[phone_regex], max_length=11)

    def __str__(self):
        return self.user_phone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_picture = models.ImageField(upload_to='profile_pics', default='default.jpg'  )
    phone_id = models.ForeignKey(UserPhone, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    country = models.TextField(max_length=20, null=True)
    fb_url_regex = RegexValidator(regex=r'.+www.facebook.com\/[^\/]+$')
    facebook_url = models.TextField(null=True, max_length=300, validators=[fb_url_regex])

    def __str__(self):
        return f'{self.user.username} Profile'

