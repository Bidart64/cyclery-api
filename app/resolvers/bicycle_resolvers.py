from ariadne import QueryType, MutationType
from app.models.bicycle import Bicycle
from app.schemas.bicycle import BicycleInput

query = QueryType()
mutation = MutationType()


@query.field("getBicycle")
def resolve_get_bicycle(_, info, id):
    bicycle = Bicycle.query.get(id)
    if bicycle is None:
        raise Exception("Bicycle not found")
    return bicycle


@query.field("getAllBicycles")
def resolve_get_all_bicycles(_, info):
    bicycles = Bicycle.query.all()
    return bicycles


@mutation.field("createBicycle")
def resolve_create_bicycle(_, info, input):
    bicycle = Bicycle(**input)
    db.session.add(bicycle)
    db.session.commit()
    return bicycle


@mutation.field("updateBicycle")
def resolve_update_bicycle(_, info, id, input):
    bicycle = Bicycle.query.get(id)
    if bicycle is None:
        raise Exception("Bicycle not found")
    for key, value in input.items():
        setattr(bicycle, key, value)
    db.session.commit()
    return bicycle


@mutation.field("deleteBicycle")
def resolve_delete_bicycle(_, info, id):
    bicycle = Bicycle.query.get(id)
    if bicycle is None:
        raise Exception("Bicycle not found")
    db.session.delete(bicycle)
    db.session.commit()
    return True


@mutation.field("placeBid")
def resolve_place_bid(_, info, id, bid):
    bicycle = Bicycle.query.get(id)
    if bicycle is None:
        raise Exception("Bicycle not found")
    if bid <= bicycle.highest_bid:
        raise Exception("Bid must be higher than current highest bid")
    bicycle.highest_bid = bid
    db.session.commit()
    return bicycle
