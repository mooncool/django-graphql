from abc import ABCMeta, abstractmethod
from typing import List
from polls.models import Question
from polls.repositories import IQuestionRepository

class IQuestionService(metaclass=ABCMeta):
    def __init__(self, question_repo: IQuestionRepository):
        self.question_repo = question_repo

    @abstractmethod
    def get_by_id(self, id) -> Question:
        pass

    @abstractmethod
    def get_all(self) -> List[Question]:
        pass

class QuestionServiceImpl(IQuestionService):
    def get_by_id(self, id) -> Question:
        question = self.question_repo.get_by_id(id)
        return question

    def get_all(self) -> List[Question]:
        questions = self.question_repo.get_all()
        return questions
