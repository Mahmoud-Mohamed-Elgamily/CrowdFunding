# Generated by Django 3.0.4 on 2020-03-19 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200319_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='c',
            new_name='category_id',
        ),
    ]
