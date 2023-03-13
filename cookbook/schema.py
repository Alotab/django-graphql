import graphene
from graphene_django import DjangoObjectType
from ingredients.models import Category, Ingredients


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name', 'ingredients')


class IngredientsType(DjangoObjectType):
    class Meta:
        model = Ingredients
        fields = ('id', 'name', 'notes', 'category')


class Query(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientsType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredients.objects.select_related('category').exclude(name="")
    
    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None


class CreateCategory(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class arguements:
        name = graphene.String() 
    
    def mutate(self, info, name):
        category = Category(name=name)
        category.save()

        return CreateCategory(id=category.id, name=category.name)
    



class CreateIngredient(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    notes = graphene.String()
    category = graphene.Field(CategoryType)

    class Arguements:
        name = graphene.String()
        notes = graphene.String()
        category = graphene.Field(CategoryType)

    def mutate(self, info, name, category, notes):
        ingredients = Ingredients(name=name, notes=notes, category=category)
        ingredients.save()

        return CreateIngredient(id=ingredients.id, name=ingredients.name, notes=ingredients.notes, category=ingredients.category,)

class Mutation(graphene.ObjectType):
    createcategory = CreateCategory.Field()

class Mutation(graphene.ObjectType):
    createingredients = CreateIngredient.Field()
        
schema = graphene.Schema(query=Query, mutation=Mutation)