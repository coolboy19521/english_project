from django.urls import path
from .views import home, select_game, game, winner, add_question, update_question

urlpatterns = [
    path('', home, name = 'home'),
    path('select_game/', select_game, name = 'select_game'),
    path('game/', game, name = 'game'),
    path('winner/<int:index>', winner, name = 'winner'),
    path('add_question/', add_question, name = 'add_question'),
    path('update_question/', update_question, name = 'update_question')
]