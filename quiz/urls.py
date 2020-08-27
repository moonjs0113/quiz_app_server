#quiz app에 대한 url 관리
#quizapi에 있는건 전체 프로젝트에 대한 url 관리

from django.urls import path, include
from .views import helloAPI, randomQuiz, flowerFall

urlpatterns = [
    path("hello/", helloAPI),
    path('<int:id>/',randomQuiz),
    path('flowerFall/',flowerFall),
]