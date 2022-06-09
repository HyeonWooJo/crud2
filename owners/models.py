from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=200) 
    # default="a" default를 넣으면 아무것도 넣지 않을 경우 a가 들어감
    age = models.IntegerField()

    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name="dogs") 
    # 역참조: related_name : related_name="dogs" 로 models.py 에서 지정했을 경우 owner.dogs.all()
    # 스트링으로 Table을 작성할 경우 위에서 Table이 먼저 만들어지지 않아도 선언 가능
    name = models.CharField(max_length=45)
    age = models.IntegerField()

    class Meta:
        db_table = 'dogs'
