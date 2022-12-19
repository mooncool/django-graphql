from dependency_injector import containers, providers
from .repositories import QuestionRepositoryImpl
from .services import QuestionServiceImpl
from .models import Question

class Container(containers.DeclarativeContainer):

    question_repository = providers.Singleton(
        QuestionRepositoryImpl,
        Question,
    )

    question_service = providers.Factory(
        QuestionServiceImpl,
        question_repo=question_repository,
    )
