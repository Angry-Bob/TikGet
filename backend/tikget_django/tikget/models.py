from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)  
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='customuser_groups',  # Change this line
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_permissions',  # Change this line
        related_query_name='user',
    )

    def __str__(self):
        return self.username

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    description = models.TextField()
    seating_info = models.TextField()
    facilities = models.TextField()
    contact_phone = models.CharField(max_length=20)
    contact_email = models.EmailField()
    website = models.URLField()
    image = models.ImageField(upload_to='venue_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    date_time = models.DateTimeField(default=datetime.now)
    description = models.TextField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name
