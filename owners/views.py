import email
import json

from django.http import JsonResponse
from django.views import View

from .models import Dog, Owner

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner_name = data['owner_name']
        owner_email = data['owner_email']
        owner_age = data['owner_age']
        

        owner = Owner.objects.create(
            name = owner_name,
            email = owner_email,
            age = owner_age
        )

        return JsonResponse({'message': 'created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:
            dog_list = Dog.objects.filter(owner_id=owner.id)
            dogs_name = [dog_list[i].name for i in range(len(dog_list))]
            dogs_age = [dog_list[i].age for i in range(len(dog_list))]
            results.append(
                {
                    "owner_name" : owner.name,
                    "owner_age" : owner.age,
                    "owner_email" : owner.email,
                    "dog_name" : list(dogs_name),
                    "dog_age" : list(dogs_age)
                }
            )
        
        return JsonResponse({"results" : results}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        dog_name = data['dog_name']
        dog_age = data['dog_age']
        owner_id = data['owner_id']
        

        Dog.objects.create(
            owner_id = owner_id,
            name = dog_name,
            age = dog_age
        )

        return JsonResponse({'message': 'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    "name" : dog.name, 
                    "age" : dog.age, 
                    "owner" : dog.owner.name
                }
            )
        
        return JsonResponse({'results' : results}, status=200)
