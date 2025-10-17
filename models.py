from pydantic import BaseModel

class UserAuth(BaseModel):
    username: str
    password: str

class Tok(BaseModel):
    tok:str