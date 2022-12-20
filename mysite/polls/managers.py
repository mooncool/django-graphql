from django.db import models
from typing import List
from .entities import StudyPlan


class UserManager(models.Manager):
    def get_by_id(self, id: int):
        return self.get(id=id)

    def gets_by_ids(self, ids: List[int]):
        return self.filter(id__in=ids)

class StudyPlanManager(models.Manager):

    def get_by_id(self, id: int):
        return self.get(id=id)

    def gets_by_ids(self, ids: List[int]):
        return self.filter(id__in=ids)

class UserStudyPlanRelationshipManager(models.Manager):
    def gets_by_user_ids(self, user_ids: List[int]):
        return self.filter(user_id__in=user_ids)

    def gets_by_study_plan_ids(self, study_plan_ids: List[int]):
        return self.filter(study_plan_id__in=study_plan_ids)
