from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *


class Category(models.Model):
    category_name = models.CharField(max_length=20)


class Images (models.Model):
    img = models.ImageField(upload_to="HomePage/static/image/")


class Tag (models.Model):
    tag_name = models.CharField(max_length=10)


class Projects (models.Model):
    project_title = models.CharField(max_length=40)
    project_details = models.TextField(default=' ')
    total_donation = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    c = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    project_img = models.ForeignKey(
        Images, on_delete=models.CASCADE, null=False)


class Comment (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    comment_content = models.TextField(default=' ')


class Donation (models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_amount = models.IntegerField()



class Rate (models.Model):
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rate_content=models.TextField(default=' ')
    rate_number = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])


class FeaturedProject (models.Model):
    proj = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.proj.title)

