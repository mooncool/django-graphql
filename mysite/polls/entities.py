from graphene_django import DjangoObjectType, DjangoListField
from dataclasses import dataclass
from typing import List
from .models import Choice as ChoiceModel
from .models import Question as QuestionModel

@dataclass
class Choice(DjangoObjectType):
    class Meta:
        model = ChoiceModel
        fields = ('id', 'choice_text')

@dataclass
class Question(DjangoObjectType):
    class Meta:
        model = QuestionModel
        fields = ('id', 'question_text', 'pub_date')

@dataclass
class QuestionWithChoices(DjangoObjectType):
    class Meta:
        model = QuestionModel
        fields = ('id', 'question_text', 'pub_date')

    def resolve_choices(self, info):
        return ChoiceModel.objects.filter(question__id=self.id)
