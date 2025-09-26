from fastapi import FastAPI
from src.web import recipe
from src.web import user


app = FastAPI()

app.include_router(user.router)
app.include_router(recipe.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)