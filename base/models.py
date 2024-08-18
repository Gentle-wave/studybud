from django.db import models
from django.contrib.auth.models import User
import uuid


class Topic (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return super().__str__() + self.name



# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    room_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    room_name = models.CharField(max_length=10)
    room_description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__() + f" {self.room_number}"

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__() + f" {self.message[0:50]}"