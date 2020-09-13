from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

from projects.models import Application


class UserManager(BaseUserManager):

    def create_user(self, email, username, display_name=None, password=None):
        if not email:
            raise ValueError("You should enter an email address")
        if not display_name:
            display_name = username

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            display_name=display_name
        )    
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, display_name, password):
        user = self.create_user(
            email,
            username,
            display_name,
            password
        )    
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    '''A user model'''
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    display_name = models.CharField(max_length=140)
    bio = models.CharField(max_length=140, blank=True, default='')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(default='default.png', upload_to='profile_pics')
    skills = models.ManyToManyField('Skill')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['display_name', 'username']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.display_name

    @property
    def is_admin(self):
        return self.is_staff


class Skill(models.Model):
    '''A model for skills'''
    JS = 'JavaScript'
    SQL = 'SQL'
    PYTHON = 'Python'  
    CSS = 'CSS'  
    DESIGN = 'Design'
    UX = 'UX'
    SKILLS_LIST = (
        (JS , "JavaScript"),
        (SQL , "SQL Databases"),
        (PYTHON, "Python"),
        (CSS, 'CSS'),
        (DESIGN, 'Design'),
        (UX, 'User experience'),
    )

    name = models.CharField(choices=SKILLS_LIST, max_length=10, default=JS)

    def __str__(self):
        return self.name.title()
 
      
class Profile(models.Model):
    '''Profile model'''
    user = models.OneToOneField(
        User, 
        on_delete = models.CASCADE,

    )
    bio = models.CharField(max_length=140, blank=True, default='')
    avatar = models.ImageField(default='default.png', upload_to='profile_pics')
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()  

        img = Image.open(self.avatar.path)  

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)        
