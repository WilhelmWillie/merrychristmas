from django.conf.urls import patterns, url

from cardcreator import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^card/(?P<card_slug>\d+)/$', views.card, name='card')
)