import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.bicycle import Bicycle as BicycleModel


class Bicycle(SQLAlchemyObjectType):
    class Meta:
        model = BicycleModel
        interfaces = (graphene.relay.Node,)


class CreateBicycle(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)
        starting_bid = graphene.Float(required=True)

    bicycle = graphene.Field(lambda: Bicycle)

    def mutate(self, info, name, description, starting_bid):
        bicycle = BicycleModel(
            name=name, description=description, starting_bid=starting_bid
        )
        db_session = info.context["session"]
        db_session.add(bicycle)
        db_session.commit()
        return CreateBicycle(bicycle=bicycle)


class Query(graphene.ObjectType):
    bicycles = graphene.List(Bicycle)

    def resolve_bicycles(self, info):
        query = Bicycle.get_query(info)
        return query.all()


class Mutation(graphene.ObjectType):
    create_bicycle = CreateBicycle.Field()
