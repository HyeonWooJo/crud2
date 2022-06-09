import email
import json

from django.http import JsonResponse
from django.views import View

from .models import Dog, Owner

class OwnerView(View):
    """
    목적: 주인의 정보를 저장

    1. 클라이언트로 부터 주인 정보 받음
    2. 받은 정보를 DB에 저장
    """
    def post(self, request):
        """
        request.body = {
            "owner_name" : "kang",
            "owner_email" : "111@gmail.com",
            "owner_age" : 22
        }
        """
        data = json.loads(request.body) # json.loads(): json 타입을 dict 타입으로 변환

        owner_name = data['owner_name']
        owner_email = data['owner_email']
        owner_age = data['owner_age']
        
        # objects: ORM을 사용할 수 있게 해주는(manage) 클래스
        owner = Owner.objects.create(
            name = owner_name,
            email = owner_email,
            age = owner_age
        )

        return JsonResponse({'message': 'created'}, status=201)

    def get(self, request):
        """
        목적: 주인들의 정보를 가져오는 것

        1. DB에 있는 모든 주인들의 정보를 조회
        2. 조회한 정보들을 client가 볼 수 있도록 가공
        """

        owners = Owner.objects.all() # 반환값: QuerySet, Table 안에 Row가 하나 더라도 QuerySet으로 반환됨
        results = []

        """
        역참조
        1. class(소문자로)_set : Dog면 dog_set / onwer.dog_set.all()
        2. related_name : related_name="dogs" 로 models.py 에서 지정했을 경우 owner.dogs.all()

        """
        
        for owner in owners:
            #dog_list = Dog.objects.filter(owner_id=owner.id)
            #역참조 사용시 : dog_list = owner.dog_set.all() / owner.dogs.all()
            dogs = owner.dogs.all()
            #dogs_name = [dog_list[i].name for i in range(len(dog_list))]
            #dogs_age = [dog_list[i].age for i in range(len(dog_list))]
            results.append(
                {
                    "1. owner_name" : owner.name,
                    "2. owner_age" : owner.age,
                    "3. owner_email" : owner.email,
                    #"dog_name" : list(dogs_name), #[dog.name for dog in dog_list]
                    #"dog_age" : list(dogs_age) #[dog.age for dog in dog_list],
                    "4. dog_name" : [dog.name for dog in dogs],
                    "5. dog_age" : [dog.age for dog in dogs]
                
                }
            )
        
        return JsonResponse({"results" : results}, status=200)

class DogView(View):
    def post(self, request):

        
        # 1. Post로 받은 owner가 DB 내에 주인 정보가 있는지 먼저 확인
        try:
            data = json.loads(request.body)
            owner = Owner.objects.get(name=data['owner'])

            Dog.objects.create(
                name = data['name'],
                age = data['age'],
                owner = owner
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)
        except Owner.DoesNotExist:
            return JsonResponse({'message': 'Bad Request'}, status=400)
        

        """
        2. Post로 바로 owner_id를 DB에 넣는 경우 (비추천)

        data = json.loads(request.body)
        dog_name = data['dog_name']
        dog_age = data['dog_age']
        owner_id = data['owner_id']
        

        Dog.objects.create(
            owner_id = owner_id,
            name = dog_name,
            age = dog_age
        )
        """
        return JsonResponse({'message': 'created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:
            results.append(
                {
                    "1. name" : dog.name, 
                    "2. age" : dog.age, 
                    "3. owner" : dog.owner.name
                }
            )
        
        return JsonResponse({'results' : results}, status=200)
