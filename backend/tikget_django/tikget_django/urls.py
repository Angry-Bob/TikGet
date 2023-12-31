"""
URL configuration for tikget_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tikget.views import user_login, signup, venue_list, venue_detail, event_list, event_detail, CustomUserAPIView



urlpatterns = [
    path('users/', CustomUserAPIView.as_view(), name='user-list'),
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('signup/', signup, name='signup'),
    path('venues/', venue_list, name='venue-list'),
    path('venues/<int:venue_id>/', venue_detail, name='venue-detail'),
    path('events/', event_list, name='event-list'),
    path('events/<int:event_id>/', event_detail, name='event-detail'),

]
