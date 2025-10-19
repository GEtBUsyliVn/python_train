
from fastapi import FastAPI,HTTPException

from config import Settings
from jwt_helpers import JwtHelpers

from models import UserAuth, Tok
from vault_helpers import VaultHelpers

app = FastAPI()

settings = Settings()

v_helpers = VaultHelpers(settings)

jwt_helpers = JwtHelpers(settings, v_helpers)

@app.post("/auth")
def auth(usr:UserAuth):

    encoded = jwt_helpers.encode_jwt(usr,read_from_file=True)
    if encoded is None:
        raise HTTPException(status_code=500, detail="Error encoding token")
    return {"token":encoded}

@app.post("/auth/decode")
def decode_token(tok:Tok):
    decoded = jwt_helpers.decode_jwt(tok.tok,read_from_file=True)
    return decoded


if __name__  == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)



