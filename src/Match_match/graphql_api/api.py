import graphene
from graphene_federation import build_schema

from .places.schema import PlacesQuery


class Query (PlacesQuery, graphene.ObjectType):
    pass


schema = build_schema(query=Query)

