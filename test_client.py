from openapi_client.praemunio_client import PraemunioClient

client = PraemunioClient.sandbox(
    "public_key",
    "secret_key",
)

client.authenticate()
print("AUTH OK", client.get_access_token()[:30])

api = client.create_api()
result = api.workspaces_drive_get()
print("DRIVE:", result.get("success"), result.get("message"))
