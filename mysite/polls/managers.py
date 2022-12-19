from django.db import models
from .models import Question

class QuestionManager(models.Manager):
    def get_by_id(self, question: Question, id: int):
        return question.objects.filter(id=id).first()

