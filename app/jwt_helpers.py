from dotenv import load_dotenv
import jwt
from models import UserAuth
from datetime import datetime, timezone,timedelta
from pydantic_settings import BaseSettings

from vault_helpers import VaultHelpers


class JwtHelpers:

    def __init__(self,settings:BaseSettings,v_helpers:VaultHelpers):
        load_dotenv()
        self.settings = settings
        self.v_helpers = v_helpers

    def encode_jwt(self,usr:UserAuth):
        to_encode = usr.model_dump().copy()

        to_encode.update(
            exp=datetime.now(tz=timezone.utc)+timedelta(hours=self.settings.auth_jwt.expires_at)
        )
        secret = self.v_helpers.get_private_secret()
        if secret is None:
            return None

        encoded = jwt.encode(to_encode, secret, algorithm="RS256")

        return encoded

    def decode_jwt(self,token:str):
        decoded = jwt.decode(token, self.v_helpers.get_public_secret(), algorithms=["RS256"])
        return decoded
