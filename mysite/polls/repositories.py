from abc import ABCMeta, abstractmethod
from typing import List

from polls.models import Question
from . import entities

class IQuestionRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, id) -> Question:
        pass

    @abstractmethod
    def get_all(self) -> List[Question]:
        pass


class QuestionRepositoryImpl(IQuestionRepository):
    # def __init__(self, question_model: Question):
    #     self.question_model = question_model

    def get_by_id(self, id) -> Question:
        question = Question.objects.filter(id=id).first()
        # question = self.question_model.objects.filter(id=id)
        return question

    def get_all(self) -> List[Question]:
        return Question.objects.all()
        # return self.question_model.objects.all()
