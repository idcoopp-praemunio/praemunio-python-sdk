from openapi_client.api.default_api import DefaultApi
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient
from openapi_client.models.authenticate_request import AuthenticateRequest

SANDBOX_URL = "https://sandbox-api.praemunio.org/api/v1"
LIVE_URL = "https://api.praemunio.org/api/v1"


class PraemunioClient:
    def __init__(self, public_key: str, secret_key: str, base_url: str = SANDBOX_URL):
        self.public_key = public_key
        self.secret_key = secret_key
        self.base_url = base_url.rstrip("/")
        self.access_token = None
        self.refresh_token = None

    @classmethod
    def sandbox(cls, public_key: str, secret_key: str):
        return cls(public_key, secret_key, SANDBOX_URL)

    @classmethod
    def live(cls, public_key: str, secret_key: str):
        return cls(public_key, secret_key, LIVE_URL)

    def authenticate(self):
        config = Configuration(host=self.base_url)
        api = DefaultApi(ApiClient(config))
        response = api.auth_auth_token_post(
            AuthenticateRequest(public_key=self.public_key, secret_key=self.secret_key)
        )

        if not response.get("success") or not response.get("result"):
            raise RuntimeError(f"Authentication failed: {response.get('message')}")

        self.access_token = response["result"]["access_token"]
        self.refresh_token = response["result"]["refresh_token"]
        return response

    def create_api(self):
        config = Configuration(host=self.base_url, access_token=self.access_token)
        return DefaultApi(ApiClient(config))

    def get_access_token(self):
        return self.access_token

    def get_refresh_token(self):
        return self.refresh_token
