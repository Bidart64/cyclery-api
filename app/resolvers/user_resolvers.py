from ariadne import QueryType, MutationType
from app.models.user import User
from app.schemas.user import UserSchema

query = QueryType()
mutation = MutationType()


@query.field("getUser")
def resolve_get_user(_, info, id):
    user = User.query.get(id)
    if user is None:
        return None
    return UserSchema().dump(user)


@query.field("getAllUsers")
def resolve_get_all_users(_, info):
    users = User.query.all()
    return UserSchema(many=True).dump(users)


@mutation.field("createUser")
def resolve_create_user(_, info, input):
    user = User(**input)
    db.session.add(user)
    db.session.commit()
    return UserSchema().dump(user)


@mutation.field("updateUser")
def resolve_update_user(_, info, id, input):
    user = User.query.get(id)
    if user is None:
        return None
    for key, value in input.items():
        setattr(user, key, value)
    db.session.commit()
    return UserSchema().dump(user)


@mutation.field("deleteUser")
def resolve_delete_user(_, info, id):
    user = User.query.get(id)
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return UserSchema().dump(user)


@query.field("getUserBicycles")
def resolve_get_user_bicycles(_, info, id):
    user = User.query.get(id)
    if user is None:
        return None
    return BicycleSchema(many=True).dump(user.bicycles)
