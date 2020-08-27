from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()

# 시리얼라이즈(Serialize) : 장고 모델 데이터를 JSON타입으로 바꿔주는 직렬화 코드