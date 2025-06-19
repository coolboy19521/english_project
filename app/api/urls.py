from django.urls import path
from .views import getRoutes, getQuestionsAll, getQuestionsCount

urlpatterns = [
    path('', getRoutes),
    path('questions/', getQuestionsAll),
    path('questions/<int:count>', getQuestionsCount)
]