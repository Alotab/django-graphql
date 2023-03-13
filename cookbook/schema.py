import graphene
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredients


class CategoryType(DjangoObjectType):
    class Meta:
        models = Category
        fields = ('id', 'name', 'ingredients')


class IngredientsType(DjangoObjectType):
    class Meta:
        models = Ingredients
        fields = ('id', 'name', 'notes', 'category')


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientsType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(self, info):
        return Ingredients.objects.select_related('category').all()
    
    def resolve_category_by_name(self, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
        
schema = graphene.Schema(query=Query)

