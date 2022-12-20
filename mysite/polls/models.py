from django.db import models
from .managers import UserManager, StudyPlanManager

class User(models.Model):
    name = models.CharField(max_length=200)

    objects = UserManager()

class StudyPlan(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)

    objects = StudyPlanManager()

class UserStudyPlanRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'user_study_plan'
