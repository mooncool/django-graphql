from django.http import HttpResponse
from .models import User, StudyPlan

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def init_data(request):
    user_1 = User.objects.create(
        name="user_1",
    )
    user_2 = User.objects.create(
        name="user_2",
    )
    user_3 = User.objects.create(
        name="user_3",
    )
    study_plan_1 = StudyPlan.objects.create(
        name="study_plan_1",
    )
    study_plan_1.users.add(user_1)
    study_plan_1.users.add(user_2)
    study_plan_2 = StudyPlan.objects.create(
        name="study_plan_2",
    )
    study_plan_2.users.add(user_2)
    study_plan_2.users.add(user_3)
    # save to database
    user_1.save()
    user_2.save()
    user_3.save()
    study_plan_1.save()
    study_plan_2.save()
    return HttpResponse("init data success.")
