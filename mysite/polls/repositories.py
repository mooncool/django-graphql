from typing import List
from .entities import StudyPlan, Participant
from .models import User as UserModel
from .models import StudyPlan as StudyPlanModel
from .models import UserStudyPlanRelationship as UserStudyPlanRelationshipModel

class StudyPlanRepository:
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

    def gets_by_user(self, user_id: int) -> List[StudyPlan]:
        study_plans = StudyPlanModel.objects.get(user_id=user_id)
        # StudyPlanModel.objects.filter(user__in=study_plans)
        # user_ids = set(study_plan.user_id for study_plan in study_plans)
        relations = UserStudyPlanRelationshipModel.objects.filter(studyplan__in=study_plans)
        relation_dict = {}
        for relation in relations:
            if relation_dict[relation.study_plan_id] is None:
                relation_dict[relation.study_plan_id] = []
            relation_dict[relation.study_plan_id].append(relation.user_id)
        users = UserModel.objects.filter(pk__in=set(relation.user_id for relation in relations))
        user_dict = {}
        for user in users:
            user_dict[user.id] = user
        results = []
        for study_plan in study_plans:
            participants = []
            for user_id in relation_dict[study_plan.id]:
                participant = self._convert_user_model_to_participant_entity(user_dict[user_id])
                participants.append(participant)

            entity = StudyPlan(
                id=study_plan.id,
                name=study_plan.name,
                participants=participants
            )
            results.append(entity)

        return results
