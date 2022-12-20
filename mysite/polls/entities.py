import graphene

class Participant(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class StudyPlan(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    participants = graphene.List(Participant)
