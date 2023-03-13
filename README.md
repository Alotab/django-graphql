# django-graphql
This repo demonstrate how to add GraphQL functionality to any Django project



## Schme and Object Types
In order to make queries to our django project, we need these few things:

`Schema with defined objects types`
`A view taking queries as input and returing result

## Create GraphQL
~ subclass the `DjangoObjectType` class which will automatically define GraphQL fields that corresponds to Django models fields

~ List those types as fields in the `Querry` class

