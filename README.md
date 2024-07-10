# GraphQL Flask Example

This repository contains a simple example of how to use GraphQL with Flask. GraphQL is a query language for your API and a server-side runtime for executing queries by using a type system you define for your data. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data.

## Quick Explanation of GraphQL

GraphQL is a powerful tool that allows clients to request exactly the data they need, and nothing more. It enables declarative data fetching, where a client can specify not only the data they want but also the format of the response. This can lead to more efficient data retrieval and reduce the amount of data transferred over the network.

Key benefits of GraphQL:
- **Declarative Data Fetching:** Clients can specify exactly what data they need.
- **Single Endpoint:** Unlike REST, which often requires multiple endpoints, GraphQL typically uses a single endpoint.
- **Strongly Typed:** GraphQL schemas are strongly typed, which makes it easier to validate and understand the data.

## Required Pip Installs

To set up the environment for this project, you need to install several Python packages. Here is a list of the required pip installs:

```sh
pip install flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install graphene
pip install --pre graphene-sqlalchemy
pip install "graphql-server[flask]"
pip install setuptools
```

# Movie Database GraphQL Schema

## Objective:
Create a GraphQL schema for a movie database using `graphene` and `graphene-sqlalchemy`. The schema should include queries to retrieve all movies, retrieve a movie by its ID, and search for movies by title. Additionally, include mutations to create, update, and delete movies.

## Database Model:

**Movie**
- `id: ID!`
- `title: String!`
- `genre: String!`
- `releaseYear: Int!`
- `director: String!`
- `rating: Float`

## Requirements:

### Queries:

- `allMovies`: Retrieve all movies.
- `movieById(id: ID!): Movie`: Retrieve a movie by its ID.
- `searchMovies(title: String!): [Movie]`: Search for movies by title.

### Mutations:

- `createMovie(title: String!, genre: String!, releaseYear: Int!, director: String!, rating: Float): Movie`: Create a new movie.
- `updateMovie(id: ID!, title: String, genre: String, releaseYear: Int, director: String, rating: Float): Movie`: Update an existing movie.
- `deleteMovie(id: ID!): Boolean`: Delete a movie by its ID.


# GraphQL Movies Project

## Overview

This project is a fork of the original [GraphQL Movies Project](https://github.com/SylverVB/BE-Spec-147_movie_graphql_api.git). It is a GraphQL API for managing a movie database, allowing you to retrieve, create, update, and delete movie entries. The backend is built with Flask, SQLAlchemy, and Graphene for GraphQL support.


## Features

- Retrieve all movies
- Retrieve a movie by its ID
- Search for movies by title or genre
- Create a new movie
- Update an existing movie
- Delete a movie by its ID

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7+
- pip (Python package installer)

### Installation Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/SylverVB/BE-Spec-147_movie_graphql_api.git
   cd BE-Spec-147_movie_graphql_api
   ```

2. **Create a virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   ```sh
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the application:**

   ```sh
   flask --debug run
   ```

   The API will be available at `http://127.0.0.1:5000`.

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schema.py
│   └── __pycache__
├── instance
│   └── movies.db
├── migrations
├── venv
├── .gitignore
├── README.md
└── requirements.txt
```

### Detailed Description of Files

- **`__init__.py`**: Initializes the Flask application, sets up the database and GraphQL schema.
- **`database.py`**: Contains the SQLAlchemy database instance and configuration.
- **`models.py`**: Defines the Movie model for the database.
- **`schema.py`**: Contains the GraphQL schema, including queries and mutations.
- **`requirements.txt`**: Lists the Python packages required for the project.

## GraphQL Queries and Mutations

### Queries

1. **Retrieve all movies:**

   ```graphql
   query {
     allMovies {
       id
       title
       genre
       releaseYear
       director
       rating
     }
   }
   ```

2. **Retrieve a movie by its ID:**

   ```graphql
   query {
     movieById(id: "1") {
       id
       title
       genre
       releaseYear
       director
       rating
     }
   }
   ```

3. **Search for movies by title or genre:**

   ```graphql
   query {
     searchMovies(title: "Inception", genre: "Sci-Fi") {
       id
       title
       genre
       releaseYear
       director
       rating
     }
   }
   ```

### Mutations

1. **Create a new movie:**

   ```graphql
   mutation {
     createMovie(title: "Inception", director: "Christopher Nolan", releaseYear: 2010, genre: "Sci-Fi", rating: 8.8) {
       movie {
         id
         title
         genre
         releaseYear
         director
         rating
       }
     }
   }
   ```

2. **Update an existing movie:**

   ```graphql
   mutation {
     updateMovie(id: "1", title: "Inception", director: "Christopher Nolan", releaseYear: 2010, genre: "Sci-Fi", rating: 9.0) {
       movie {
         id
         title
         genre
         releaseYear
         director
         rating
       }
     }
   }
   ```

3. **Delete a movie by its ID:**

   ```graphql
   mutation {
     deleteMovie(id: "1") {
       message
     }
   }
   ```

## License

This project was completed by [Victor Bondaruk](https://github.com/SylverVB) 