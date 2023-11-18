from django.contrib import admin
from .models import CustomUser, Venue, Event

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Venue)
admin.site.register(Event)
