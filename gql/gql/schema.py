import graphene

import sentences.schema as sc


class Query(sc.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
