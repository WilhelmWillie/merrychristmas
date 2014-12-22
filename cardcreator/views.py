from django.shortcuts import render, get_object_or_404

from cardcreator.models import Card

def index(request):
  return render(request, 'home.html')

def card(request, card_slug):
  c = get_object_or_404(Card, slug=card_slug)
  return render(request, 'card.html', {'card': c})