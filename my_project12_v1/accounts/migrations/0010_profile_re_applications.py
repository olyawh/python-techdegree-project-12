# Generated by Django 3.0.8 on 2020-08-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_application'),
        ('accounts', '0009_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='re_applications',
            field=models.ManyToManyField(to='projects.Application'),
        ),
    ]