from django.test import TestCase
import pytest
from .models import Question
from django.utils import timezone

# Create your tests here.
@pytest.mark.django_db
class TestQuestionManagerGetById:

    # We make integration tests for the manager to validate database behaviours
    def test_get_question_by_id(self):
        question_1 = Question.objects.create(
            question_text="question 1", pub_date=timezone.now())
        question_2 = Question.objects.create(
            question_text="question 2", pub_date=timezone.now())

        question = Question.objects.get_by_id(Question, 1)

        question_1.refresh_from_db()
        question_2.refresh_from_db()
        assert question_1.id == 1
        assert question_2.id == 2
        assert question.id == 1
