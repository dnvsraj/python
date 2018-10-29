from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(model.Model):
    first_player = models.ForeignKey(User,related_name="games_first_player")
    second_player = models.ForeignKey(User, related_name="games_second_player")
class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_lenght=300, blank=True)
    by_first_player = models.BooleanField()
