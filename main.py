
from fastapi import FastAPI, Path, Query
from  typing import Annotated
from database import Base, engine
from schemas import UserSchema
import models

app = FastAPI(title="My First API")
Base.metadata.create_all(bind=engine)

@app.get(path='/users/{user_id}/')
async def first_view(user_id: Annotated[int, Path(ge=0)]):
    return {"Message": "My first", "user_id": user_id}

