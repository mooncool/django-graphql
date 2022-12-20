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
