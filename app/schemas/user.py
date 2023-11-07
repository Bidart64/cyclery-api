import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.user import User as UserModel
from app.schemas.bicycle import Bicycle as BicycleSchema


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (graphene.relay.Node,)

    bicycles = graphene.List(BicycleSchema)

    def resolve_bicycles(self, info):
        return self.bicycles
