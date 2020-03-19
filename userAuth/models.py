from django.db import models
from django.core.validators import RegexValidator


# class UserPhone(models.Model):
#     phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
#     user_phone = models.CharField(validators=[phone_regex], max_length=11)
#
#     def __str__(self):
#         return self.user_id__user_fname
#
#
# class User(models.Model):
#     user_fname = models.CharField(max_length=10)
#     user_lname = models.CharField(max_length=10)
#     user_picture = models.ImageField(upload_to="user_images/", default="user_images/default.jpg")
#     user_password = models.CharField(max_length=50)
#     phone_id = models.ForeignKey(UserPhone, on_delete=models.CASCADE)
#     bith_date = models.DateField(null=True)
#     country = models.TextField(max_length=20, null=True)
#     fb_url_regex = RegexValidator(regex=r'.+www.facebook.com\/[^\/]+$')
#     facebook_url = models.TextField(null=True, max_length=300, validators=[fb_url_regex])
#
#     def __str__(self):
#         return self.user_fname
