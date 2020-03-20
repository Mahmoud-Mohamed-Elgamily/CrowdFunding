# Generated by Django 3.0.4 on 2020-03-19 22:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='HomePage/static/image/')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=40)),
                ('project_details', models.TextField(default=' ')),
                ('total_donation', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('c', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Category')),
                ('project_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Images')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_content', models.TextField(default=' ')),
                ('rate_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='projects',
            name='tag_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Tag'),
        ),
        migrations.AddField(
            model_name='projects',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FeaturedProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_amount', models.IntegerField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField(default=' ')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Projects')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
