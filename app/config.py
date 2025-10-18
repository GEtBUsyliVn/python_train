from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ConfigJWT(BaseModel):
    expires_at:int = 1

class ConfigVault(BaseModel):
    url:str = 'http://172.17.0.5:8200'
    version_prefix:str = '/v1'
    engine:str= '/cubbyhole'

class ConfigPvtKey(ConfigVault):
    path_to_secret:str = '/pvt_key'
    secret_version:str = '1'

class ConfigPubKey(ConfigVault):
    path_to_secret:str = '/secret/data/pub_key'
    secret_version:str = '1'


class Settings(BaseSettings):
    auth_jwt: ConfigJWT = ConfigJWT()
    vault: ConfigVault = ConfigVault()
    vault_pvt_key: ConfigPvtKey = ConfigPvtKey()
    vault_pub_key: ConfigPubKey = ConfigPubKey()