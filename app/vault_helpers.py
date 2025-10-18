from os import getenv
from dotenv import load_dotenv
import requests
from pydantic_settings import BaseSettings


class VaultHelpers:
    def __init__(self,settings:BaseSettings):
        load_dotenv()
        self.config_vault = settings.vault
        self.config_pvt_key = settings.vault_pvt_key
        self.config_pub_key = settings.vault_pub_key

    def get_private_secret(self):
        r = requests.get(f"{self.config_vault.url}{self.config_vault.version_prefix}{self.config_vault.engine}{self.config_pvt_key.path_to_secret}",verify=False,
                headers={"X-Vault-Token": getenv('VAULT_TOKEN')})
        if r.status_code!=200:
            return None
        payload = r.json()
        secret = payload["data"]["key"]
        return secret

    def get_public_secret(self):
        r = requests.get(f"{self.config_vault.url}{self.config_vault.version_prefix}{self.config_pub_key.path_to_secret}",verify=False,
                     headers={"X-Vault-Token": getenv('VAULT_TOKEN')})
        payload = r.json()
        secret = payload["data"]["data"]["secret"]
        return secret


