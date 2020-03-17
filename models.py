from django.db import models
from django.core.validators import RegexValidator

# Create your models here.



#user model
class User (models.Model):
    # user_id = models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=10)
    user_lname = models.CharField(max_length=10)
    user_picture = models.ImageField(upload_to="user_images/")
    user_password = models.CharField(max_length=50)



#User phone mode
class UserPhone (models.Model):
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^[+-]?[0-9]+$')
    user_phone=models.CharField(validators=[phone_regex],max_length=11)




# category model
class Category(models.Model):
    # category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)



#tag model
class Tag (models.Model):

    # tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=10)



#image class
class Images (models.Model):
    # img_id = models.AutoField(primary_key = True,null=False)
    img = models.ImageField(upload_to="images/")

# hena f class img
# da mlosh lzam by default django bt3ml id


#projects model
class Projects (models.Model):

    # project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=40)
    project_details = models.TextField(default=' ')
    total_donation = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    project_img = models.ForeignKey(Images, on_delete=models.CASCADE , null=False)

# el moshklda hna ?




#comment model
class Comment (models.Model):
    # comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects , on_delete=models.CASCADE)
    comment_content = models.TextField(default=' ')





#donation model
class Donation (models.Model):
    # donation_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE)
    donation_amount = models.IntegerField()





