from django.urls import path
from .views import *
urlpatterns = [
    path('',tweet_list,name='tweet_list'),
    path('create/',tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/',tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/',tweet_delete,name='tweet_delete'),

] 