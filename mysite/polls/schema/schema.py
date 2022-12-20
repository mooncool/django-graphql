import graphene
from ..entities import StudyPlan
from ..repositories import StudyPlanRepository

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    study_plans = graphene.List(StudyPlan, user_id=graphene.Int(required=True))
    study_plan = graphene.Field(StudyPlan, id=graphene.Int(required=True))

    def resolve_study_plans(
        root, info,
        user_id,
    ):
        return StudyPlanRepository.gets_by_user(user_id)

    def resolve_study_plan(
        root, info, id,
    ):
        return StudyPlanRepository.get_by_id(id)

schema = graphene.Schema(query=Query)
