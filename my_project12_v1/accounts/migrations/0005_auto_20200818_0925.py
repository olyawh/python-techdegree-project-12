# Generated by Django 3.0.8 on 2020-08-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200810_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='skills',
            field=models.ManyToManyField(to='accounts.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(choices=[('js', 'JavaScript Developer'), ('sql', 'SQL Database Specialist'), ('python', 'Python Developer'), ('ux', 'UX Designer'), ('ui', 'UI Specialist'), ('css', 'CSS Developer'), ('django', 'Django Developer')], max_length=100),
        ),
    ]
