from django.db import models

class Card(models.Model):
  to_recepient = models.CharField(max_length=36) # Name of the recepient
  from_sender = models.CharField(max_length=36) # Name of the sender
  message = models.CharField(max_length=560) # The message of the card
  img = models.CharField(max_length=36) # Stores image file name without extension