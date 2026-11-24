# Praemunio Python SDK

Python client for the Praemunio public API.

## Installation

```bash
pip install praemunio-sdk
```

## Quick start

```python
from openapi_client.praemunio_client import PraemunioClient

client = PraemunioClient.sandbox(
    "pk_test_...",
    "sk_test_..."
)

client.authenticate()

api = client.create_api()
result = api.workspaces_drive_get()
print(result)
```

## Environments

```python
client = PraemunioClient.sandbox(public_key, secret_key)
client = PraemunioClient.live(public_key, secret_key)
```

## Authentication

The SDK exchanges `publicKey` and `secretKey` for an access token.

```python
client.authenticate()
```

## Build / Test

```bash
pip install -r requirements.txt
python test_client.py
```

