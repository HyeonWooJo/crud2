from django.db import models

class Actor2(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()

    class Meta:
        db_table = "actors2"


class Movie2(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    actor = models.ManyToManyField("Actor2")

    class Meta:
        db_table = "movies2"