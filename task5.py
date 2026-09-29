from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Movie Collection API")


# Movie model
class Movie(BaseModel):
    name: str
    rating: int = Field(..., ge=1, le=10)


# In-memory movie collection
movies = []


# 1. Add a movie
@app.post("/addmovie")
def add_movie(movie: Movie):
    movies.append(movie)
    return {
        "message": "Movie added successfully",
        "movie": movie
    }


# 2. Get all movies
@app.get("/getmovies")
def get_movies():
    return movies


# 3. Update a movie
@app.put("/updatemovie/{index}")
def update_movie(index: int, movie: Movie):
    if index < 0 or index >= len(movies):
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    movies[index] = movie

    return {
        "message": "Movie updated successfully",
        "movie": movie
    }


# 4. Delete a movie
@app.delete("/deletemovie/{index}")
def delete_movie(index: int):
    if index < 0 or index >= len(movies):
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    deleted_movie = movies.pop(index)

    return {
        "message": "Movie deleted successfully",
        "movie": deleted_movie
    }