# books/schema.py

import graphene
from graphene_django.types import DjangoObjectType
from .models import Author, Book

# Define the AuthorType for GraphQL
class AuthorType(DjangoObjectType):
    class Meta:
        model = Author

# Define the BookType for GraphQL
class BookType(DjangoObjectType):
    class Meta:
        model = Book



# Define Queries to fetch authors and books
class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_books = graphene.List(BookType)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int())
    book_by_id = graphene.Field(BookType, id=graphene.Int())
    search_authors = graphene.List(AuthorType, name=graphene.String(required=True))
    # all_Books_By_Author_Name = graphene.List(BookType, author_name=graphene.String(required=True))
    allBooksByAuthorName = graphene.List(BookType, author_name=graphene.String(required=True))


    def resolve_all_authors(self, info):
        return Author.objects.all()

    def resolve_all_books(self, info):
        return Book.objects.all()

    def resolve_author_by_id(self, info, id):
        return Author.objects.get(pk=id)

    def resolve_book_by_id(self, info, id):
        return Book.objects.get(pk=id)

    def resolve_search_authors(self, info, name):
        return Author.objects.filter(name__icontains=name)
    
    # def resolve_all_books_by_author_name(self, info, author_name):
    #     try:
    #         author = Author.objects.filter(name__icontains=author_name)
    #         print("-----",author)
    #         return Book.objects.filter(author=author)
    #     except Author.DoesNotExist:
    #         print("+++++")
    #         return [] 
    def resolve_allBooksByAuthorName(self, info, author_name):
        try:
            # Get the authors based on the author name
            author = Author.objects.filter(name__icontains=author_name).first()  # Use .first() to avoid multiple results

            if not author:
                return []  # If no author is found, return an empty list

            # Return books for the found author
            return Book.objects.filter(author=author)

        except Author.DoesNotExist:
            # If the author is not found, return an empty list
            return [] 

# Define Mutations to create authors and books
class CreateAuthor(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    author = graphene.Field(AuthorType)

    def mutate(self, info, name):
        author = Author(name=name)
        author.save()
        return CreateAuthor(author=author)

class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        author_id = graphene.Int()

    book = graphene.Field(BookType)

    def mutate(self, info, title, author_id):
        author = Author.objects.get(id=author_id)
        book = Book(title=title, author=author)
        book.save()
        return CreateBook(book=book)

# Create the Mutation class to register mutations
class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    create_book = CreateBook.Field()

# Create the Schema object with Query and Mutation
schema = graphene.Schema(query=Query, mutation=Mutation)
