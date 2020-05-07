import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Sentence


class SentenceType(DjangoObjectType):
    class Meta:
        model = Sentence


class Query(graphene.ObjectType):
    sentences = graphene.List(SentenceType, search=graphene.String())

    def resolve_sentences(self, info, id=None, **kwargs):
        if id:
            filter = (
                Q(id__icontains=id)
            )
            return Sentence.objects.filter(filter)
        return Sentence.objects.all()
