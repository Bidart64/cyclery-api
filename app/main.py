from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from app.resolvers.user_resolvers import UserQuery, UserMutation
from app.resolvers.bicycle_resolvers import BicycleQuery, BicycleMutation

app = Flask(__name__)


class Query(UserQuery, BicycleQuery):
    pass


class Mutation(UserMutation, BicycleMutation):
    pass


schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == "__main__":
    app.run()
