import graphene

class Participant(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Participants(graphene.ObjectType):
    participants = graphene.List(Participant)

class StudyPlan(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    # participants = graphene.List(Participant)
    participants = graphene.Field(Participants)
