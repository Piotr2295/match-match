import graphene


class PlacesQuery(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=PlacesQuery)
