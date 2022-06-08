import json

from pkgutil import ModuleInfo
from django.http import JsonResponse
from django.views import View

from .models import Actor, ActorMovie, Movie

class ActorView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            movie_objects = ActorMovie.objects.filter(actor_id=actor.id)
            movie_ids = [movie_objects[i].movie_id for i in range(len(movie_objects))]
            movie_list = [Movie.objects.get(id=movie_ids[i]).title for i in range(len(movie_ids))]
            results.append(
                {
                    "1. actor_first_name" : actor.first_name,
                    "2. actor_last_name" : actor.last_name,
                    "3. actor_date_of_birth" : actor.date_of_birth,
                    "4. movie_title" : movie_list
                }
            )

        return JsonResponse({"results" : results}, status=200)


class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []

        for movie in movies:
            movie_objects = ActorMovie.objects.filter(movie_id=movie.id)
            movie_ids = [movie_objects[i].actor_id for i in range(len(movie_objects))]
            actor_list = [Actor.objects.get(id=movie_ids[i]).first_name for i in range(len(movie_ids))]
            
            results.append(
                {
                    "1. movie_title" : movie.title,
                    "2. movie_running_time" : movie.running_time,
                    "3. actors" : actor_list
                }
            )


        
        return JsonResponse({"results" : results}, status=200)