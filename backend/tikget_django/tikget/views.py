from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import Venue, Event, CustomUser
from .serializers import VenueSerializer, EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model



CustomUser = get_user_model()

class CustomUserAPIView(APIView):
    def get(self, request):
        users = CustomUser.objects.all() 
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            response_data = {'token': token, 'message': 'Registration successful'}
            return JsonResponse(response_data)

    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            
            response_data = {'token': token, 'message': 'Login successful'}
            return JsonResponse(response_data)

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def venue_list(request):
    venues = Venue.objects.all()
    serializer = VenueSerializer(venues, many=True)
    return JsonResponse(serializer.data, safe=False)


def venue_detail(request, venue_id):
    try:
        venue = Venue.objects.get(pk=venue_id)
    except Venue.DoesNotExist:
        return JsonResponse({'error': 'Venue not found'}, status=404)

    serializer = VenueSerializer(venue)
    return JsonResponse(serializer.data)



def event_list(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)



def event_detail(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        return JsonResponse({'error': 'Event not found'}, status=404)

    serializer = EventSerializer(event)
    return JsonResponse(serializer.data)



