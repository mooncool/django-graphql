# from graphene_django import DjangoObjectType
import graphene
# from mysite.polls.services import IQuestionService
# from mysite.polls.containers import Container
# from polls.models import Question as QuestionModel
import polls.entities as entities
from ..repositories import QuestionRepositoryImpl
from ..services import QuestionServiceImpl
from dependency_injector.wiring import inject, Provide


# class Question(DjangoObjectType):
#     class Meta:
#         model = QuestionModel

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    questions = graphene.List(entities.QuestionWithChoices)
    question = graphene.Field(entities.Question, id=graphene.Int(required=True))

    # @inject
    # def __init__(
    #     self, question_service: IQuestionService
    # ):
    #     self.question_service = question_service

    # @inject
    # def resolve_questions(
    #     root, info,
    #     svc: IQuestionService = Provide[Container.question_service],
    # ):
    def resolve_questions(
        root, info,
    ):
        repo = QuestionRepositoryImpl()
        svc = QuestionServiceImpl(repo)
        # print(info)
        return svc.get_all()

    # @inject
    def resolve_question(
        root, info, id,
        # svc: IQuestionService = Provide[Container.question_service],
    ):
        repo = QuestionRepositoryImpl()
        svc = QuestionServiceImpl(repo)
        try:
            return svc.get_by_id(id)
        except:
            return None

    # def resolve_choices(root, info):
    #     repo = QuestionRepositoryImpl()
    #     svc = QuestionServiceImpl(repo)
    #     return 

schema = graphene.Schema(query=Query)
