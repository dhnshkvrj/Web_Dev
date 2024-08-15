from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Todo(BaseModel):
    id:int
    item:str    