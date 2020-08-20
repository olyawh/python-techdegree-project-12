# Generated by Django 3.0.8 on 2020-08-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200818_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('js', 'JavaScript Developer'), ('sql', 'SQL Database Specialist'), ('python', 'Python Developer'), ('ux', 'UX Designer'), ('ui', 'UI Specialist'), ('css', 'CSS Developer'), ('django', 'Django Developer')], max_length=7),
        ),
    ]
