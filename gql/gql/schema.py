import graphene

import links.schema as sc


class Query(sc.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
