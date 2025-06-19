from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 4096)

    variant_a = models.CharField(max_length = 4096)
    variant_b = models.CharField(max_length = 4096)
    variant_c = models.CharField(max_length = 4096)
    variant_d = models.CharField(max_length = 4096)

    correct_answer = models.IntegerField()