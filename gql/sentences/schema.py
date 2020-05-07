import graphene
from graphene_django import DjangoObjectType

from .models import Sentence


class SentenceType(DjangoObjectType):
    class Meta:
        model = Sentence


class Query(graphene.ObjectType):
    sentences = graphene.List(SentenceType)

    def resolve_sentences(self, info, **kwargs):
        return Sentence.objects.all()
