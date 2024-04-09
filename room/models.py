from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField(default=0, blank=True)
    
    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.guest_name} - {self.room} ({self.check_in_date} to {self.check_out_date})"