# Generated by Django 3.0.8 on 2020-08-25 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20200825_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ACC', 'Accepted'), ('DEC', 'Declined'), ('AWA', 'Awaiting')], default='ACC', max_length=3)),
                ('date_applied', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_position', to='projects.Position')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_project', to='projects.Project')),
            ],
            options={
                'ordering': ['-date_applied'],
                'unique_together': {('applicant', 'position', 'project')},
            },
        ),
    ]