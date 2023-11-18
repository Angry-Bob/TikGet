from django.urls import path
from . import views
from .views import venue_list, venue_detail, event_list, event_detail


urlpatterns = [
    path('venues/', venue_list, name='venue-list'),
    path('venues/<int:venue_id>/', venue_detail, name='venue-detail'),
    path('events/', event_list, name='event-list'),
    path('events/<int:event_id>/', event_detail, name='event-detail'),
]