from typing import List
from .entities import StudyPlan, Participant
from .models import User as UserModel
from .models import StudyPlan as StudyPlanModel
from .models import UserStudyPlanRelationship as UserStudyPlanRelationshipModel

class StudyPlanRepository:
    @staticmethod
    def _convert_user_model_to_participant_entity(user_model):
        return Participant(
            id=user_model.id,
            name=user_model.name,
        )

    def _convert_study_plan_model_to_study_plan_entity(study_plan_model):
        pass

    def get_by_id(id: int) -> StudyPlan:
        study_plan = StudyPlanModel.objects.get_by_id(id=id)
        relations = UserStudyPlanRelationshipModel.objects.filter(study_plan_id=study_plan.id)
        users = UserModel.objects.filter(id__in=[relation.user_id for relation in relations])
        participants = []
        for user in users:
            participant = Participant(
                id=user.id,
                name=user.name,
            )
            participants.append(participant)
        return StudyPlan(
            id=study_plan.id,
            name=study_plan.name,
            participants=participants,
        )

    def gets_by_user(user_id: int) -> List[StudyPlan]:
        relations = UserStudyPlanRelationshipModel.objects.filter(user_id=user_id)
        study_plan_ids = set(relation.study_plan_id for relation in relations)
        study_plans = StudyPlanModel.objects.filter(id__in=study_plan_ids)
        study_plan_ids = set(study_plan.id for study_plan in study_plans)
        relations = UserStudyPlanRelationshipModel.objects.filter(study_plan_id__in=study_plan_ids)
        user_ids = set(relation.user_id for relation in relations)
        relation_dict = {}
        for relation in relations:
            if relation.study_plan_id not in relation_dict:
                relation_dict[relation.study_plan_id] = []
            relation_dict[relation.study_plan_id].append(relation.user_id)
        users = UserModel.objects.filter(id__in=user_ids)
        user_dict = {}
        for user in users:
            user_dict[user.id] = user

        results = []
        for study_plan in study_plans:
            participants = []
            for user_id in relation_dict[study_plan.id]:
                participant = StudyPlanRepository._convert_user_model_to_participant_entity(user_dict[user_id])
                participants.append(participant)

            entity = StudyPlan(
                id=study_plan.id,
                name=study_plan.name,
                participants=participants
            )
            results.append(entity)

        return results
