import pytest
from .models import User, StudyPlan
from .repositories import StudyPlanRepository

@pytest.mark.django_db
class TestStudyPlanManager:
    def test_init_data(self):
        # create data fixtures
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
        user_1.refresh_from_db()
        user_2.refresh_from_db()
        user_3.refresh_from_db()
        study_plan_1.refresh_from_db()
        study_plan_2.refresh_from_db()
        # asserts
        assert user_1.id == 1
        assert user_2.id == 2
        assert user_3.id == 3
        assert study_plan_1.id == 1
        assert study_plan_2.id == 2

    def test_get_study_plan(self):
        # create data fixtures
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
        user_1.refresh_from_db()
        user_2.refresh_from_db()
        user_3.refresh_from_db()
        study_plan_1.refresh_from_db()
        study_plan_2.refresh_from_db()
        # fetch data
        study_plan = StudyPlan.objects.get_by_id(1)
        assert study_plan.id == 1
        assert study_plan.name == "study_plan_1"

    def test_get_study_plan_by_user(self):
        # create data fixtures
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
        user_1.refresh_from_db()
        user_2.refresh_from_db()
        user_3.refresh_from_db()
        study_plan_1.refresh_from_db()
        study_plan_2.refresh_from_db()
        # fetch data
        study_plans = StudyPlanRepository.gets_by_user(1)
        assert len(study_plans) == 1
        assert study_plans[0].id == 1

        study_plans = StudyPlanRepository.gets_by_user(2)
        assert len(study_plans) == 2
        assert study_plans[0].id == 1
        assert study_plans[1].id == 2
        assert len(study_plans[0].participants) == 2
        assert study_plans[0].participants[0].id == 1
        assert study_plans[0].participants[1].id == 2
        assert len(study_plans[1].participants) == 2
        assert study_plans[1].participants[0].id == 2
        assert study_plans[1].participants[1].id == 3

