from graphene_django import DjangoObjectType
import graphene
from polls.models import Question as QuestionModel

class Question(DjangoObjectType):
    class Meta:
        model = QuestionModel

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    questions = graphene.List(Question)

schema = graphene.Schema(query=Query)
