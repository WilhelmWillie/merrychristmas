from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from cardcreator.models import Card

import random
import os

def index(request):
  return render(request, 'home.html')

def card(request, card_slug):
  c = get_object_or_404(Card, slug=card_slug)
  return render(request, 'card.html', {'card': c})

def create_card(request):
  if request.method == 'POST':
    error_list = []

    # Verify data
    data = request.POST
    # Check if form data includes everything we need
    if "from" in data and "to" in data and "message" in data and "photo" in request.FILES:
      photo = request.FILES['photo']
      # Check if FROM and TO aren't longer than 36 characters
      if len(data['from']) > 36:
        error_list.append("Sender name needs to be less than 36 characters in length!")
      if len(data['to']) > 36:
        error_list.append("Recipient name needs to be less than 36 characters in length!")

      # Check if MESSAGE isn't longer than 560 characters
      if len(data['message']) > 560:
        error_list.append("Message needs to be less than 560 characters in length!")

      # Check if PHOTO is valid
      valid_content_types = [
        "image/gif",
        "image/jpeg",
        "image/png"
      ]

      if photo.content_type not in valid_content_types:
        error_list.append("Your file needs to be a valid photo!")
      elif photo.size > 1000000 * 4:
        error_list.append("Your file needs to be less than 4MB!")
    else:
      error_list.append("Make sure the form is fully completed!")

    # If our error_list is empty, then upload picture and create card
    if len(error_list) == 0:
      # Write photo

      # Generate a random file name
      original_file_name, file_extension = os.path.splitext(photo.name)
      file_name = str(random.randrange(10000,99999))

      # Keep generation random file names until we found a file name that doesn't exist
      try:
        while(True):
          Card.objects.get(img=file_name + file_extension)
          file_name = str(random.randrange(10000,99999))
      except ObjectDoesNotExist:
        # The card doesn't exist, therefore we create one!
        # Write photo to uploads folder
        with open('cardcreator/static/uploads/' + file_name + file_extension, 'wb+') as destination:
          for chunk in photo.chunks():
            destination.write(chunk)

        # Create new Card model object and redirect user
        c = Card(
            to_recipient=data['to'],
            from_sender=data['from'],
            message=data['message'],
            img=file_name + file_extension,
            slug=file_name
          )
        c.save()

        return HttpResponseRedirect('/card/' + file_name)

  else:
    return HttpResponseRedirect('/')

  return render(request, 'home.html', {
      'error_list': error_list
    })