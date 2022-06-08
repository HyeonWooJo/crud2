from django.urls import path, include



urlpatterns = [
    path('movies', include('movies.urls')),
    path('owners', include('owners.urls')),
]