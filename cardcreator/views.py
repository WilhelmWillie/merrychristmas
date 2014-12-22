from django.shortcuts import render

from django.http import HttpResponse

def index(request):
  return render(request, 'home.html')

def card(request, card_slug):
  return HttpResponse("Card: " + card_slug)