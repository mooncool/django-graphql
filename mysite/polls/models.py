from django.db import models
from .managers import UserManager, StudyPlanManager, UserStudyPlanRelationshipManager

class User(models.Model):
    name = models.CharField(max_length=200)

    objects = UserManager()

class StudyPlan(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(
        User, through='UserStudyPlanRelationship', blank=True
    )

    objects = StudyPlanManager()

class UserStudyPlanRelationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)

    objects = UserStudyPlanRelationshipManager()

    class Meta:
        db_table = 'user_study_plan'
