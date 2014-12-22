from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from cardcreator.models import Card

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

    # Check if FROM and TO contain names and aren't longer than 36
    if len(data['from']) > 36 or len(data['from']) < 0:
      error_list.append("Sender name needs to be less than 36 characters in length!")
    if len(data['to']) > 36 or len(data['to']) < 0:
      error_list.append("Recipient name needs to be less than 36 characters in length!")

    # Check if MESSAGE isn't longer than 560 characters
    if len(data['message']) > 560 or len(data['message']) < 0:
      error_list.append("Message needs to be less than 560 characters in length!")

    error_list.append("and u is a bitch")

    # Check if PHOTO is valid

    # If our error_list is empty, then upload picture and create card
  else:
    return HttpResponseRedirect('/')

  return render(request, 'home.html', {
      'error_list': error_list
    })