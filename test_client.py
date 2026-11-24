from openapi_client.praemunio_client import PraemunioClient

client = PraemunioClient.sandbox(
    "pk_test_e8c105991515c9c980b6a478f65ad441",
    "sk_test_8b2f6cd9d2d8faf7bfb6fa9fc86e43f064d1e748d252779f9921ff3f75964fdc",
)

client.authenticate()
print("AUTH OK", client.get_access_token()[:30])

api = client.create_api()
result = api.workspaces_drive_get()
print("DRIVE:", result.get("success"), result.get("message"))
