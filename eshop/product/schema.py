import graphene
from graphene_django.types import DjangoObjectType

from eshop.product.models import Category, Product


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ProductType(DjangoObjectType):
    class Meta:
        model = Product


class Query(object):
    category = graphene.Field(CategoryType,
                              id=graphene.Int(),
                              name=graphene.String())
    all_categories = graphene.List(CategoryType)

    product = graphene.Field(ProductType,
                                id=graphene.Int(),
                                name=graphene.String())
    all_products = graphene.List(ProductType)

    def resolve_all_categories(self, args, **kwargs):
        return Category.objects.all()

    def resolve_all_products(self, args, **kwargs):
        # We can easily optimize query count in the resolve method
        return Product.objects.select_related('category').all()

    def resolve_category(self, args, **kwargs):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_product(self, args, **kwargs):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return Product.objects.get(pk=id)

        if name is not None:
            return Product.objects.get(name=name)

        return None
