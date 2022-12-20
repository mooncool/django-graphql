from django.db import models
from typing import List
from .entities import StudyPlan


class UserManager(models.Manager):
    def get_by_id(self, id: int):
        return self.get(id=id)

    def gets_by_ids(self, ids: List[int]):
        return self.get(ids=ids)

class StudyPlanManager(models.Manager):

    def get_by_id(self, id: int):
        return self.get(id=id)

    def get_users(self, study_plan, study_plan_id: int):
        plan = study_plan.objects.filter(study_plan_id=study_plan_id)

        return StudyPlan(
            id=plan.id,
            name=plan.name,
        )
