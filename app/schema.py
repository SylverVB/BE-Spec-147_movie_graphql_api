import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Movie as MovieModel
from app import db

class MovieType(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie_by_id = graphene.Field(MovieType, id=graphene.ID(required=True))
    search_movies = graphene.List(MovieType, title=graphene.String(), genre=graphene.String())

    def resolve_all_movies(root, info):
        query = db.select(MovieModel)
        return db.session.scalars(query)

    def resolve_movie_by_id(root, info, id):
        movie = db.session.get(MovieModel, id)
        return movie

    def resolve_search_movies(root, info, title=None, genre=None):
        query = db.select(MovieModel)
        if title:
            query = query.where(MovieModel.title.ilike(f"%{title}%"))
        if genre:
            query = query.where(MovieModel.genre.ilike(f"%{genre}%"))
        return db.session.scalars(query)
    
class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        director = graphene.String(required=True)
        release_year = graphene.Int(required=True)
        genre = graphene.String(required=True)
        rating = graphene.Float(required=True)

    movie = graphene.Field(MovieType)

    def mutate(root, info, title, director, release_year, genre, rating):
        new_movie = MovieModel(title=title, director=director, release_year=release_year, genre=genre, rating=rating)
        db.session.add(new_movie)
        db.session.commit()
        return CreateMovie(movie=new_movie)

class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        director = graphene.String()
        release_year = graphene.Int()
        genre = graphene.String()
        rating = graphene.Float()

    movie = graphene.Field(MovieType)

    def mutate(root, info, id, title=None, director=None, release_year=None, genre=None, rating=None):
        # Query for the movie with that id
        movie = db.session.get(MovieModel, id)
        # If that movie does not exist, return None
        if movie is None:
            return None
        #If there is a title arg
        if title:
            # Set the movie's title to this
            movie.title = title
        # If there is a director arg
        if director:
            # Set the movie's director to this
            movie.director = director
        # If there is a release_year arg
        if release_year:
            # Set the movie's release_year to this
            movie.release_year = release_year
        if genre:
            movie.genre = genre
        if rating:
            movie.rating = rating
        # Commit the changes to the database
        db.session.commit()
        # Return the updated movie as the "movie" field output
        return UpdateMovie(movie=movie)

class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    message = graphene.String()

    def mutate(root, info, id):
        # Get the movie with that id
        movie = db.session.get(MovieModel, id)
        # If there is no movie with that ID
        if movie is None:
            return DeleteMovie(message=f"Movie with ID {id} does not exist")
        # remove from the database
        db.session.delete(movie)
        db.session.commit()
        return DeleteMovie(message='Movie has been deleted')
    
class Mutation(graphene.ObjectType):
    create_movie = CreateMovie.Field()
    update_movie = UpdateMovie.Field()
    delete_movie = DeleteMovie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
    
