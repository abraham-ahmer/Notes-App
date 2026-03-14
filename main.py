from fastapi import FastAPI
from database import engine
from database_models import Base
from routers import signup, login
import crud

app = FastAPI(title="Notes App")
Base.metadata.create_all(bind=engine)


app.include_router(signup.router)
app.include_router(login.router)
app.include_router(crud.router)


@app.get("/")
def hello():
    return {"message":"Hello User"}










