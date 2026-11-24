# Praemunio Python SDK

> Client officiel pour l'API Praemunio — Python

## 📦 Installation

```bash
pip install praemunio-sdk
```

Ou avec Poetry :

```bash
poetry add praemunio-sdk
```

## 🚀 Quick Start (5 minutes)

### 1. Obtenir vos clés API

Récupérez vos clés depuis le [dashboard Praemunio](https://dashboard.praemunio.io) :
- **Public Key** : `pk_test_...` (sandbox) ou `pk_live_...` (production)
- **Secret Key** : `sk_test_...` (sandbox) ou `sk_live_...` (production)

### 2. Initialiser le client

```python
from praemunio_sdk import PraemunioClient

# Mode sandbox (tests)
client = PraemunioClient.sandbox('pk_test_xxx', 'sk_test_xxx')

# Mode production
# client = PraemunioClient.live('pk_live_xxx', 'sk_live_xxx')
```

### 3. S'authentifier

```python
client.authenticate()

print(f"Access token: {client.get_access_token()}")
print(f"Refresh token: {client.get_refresh_token()}")
```

### 4. Premier appel API

```python
api = client.create_api()

# Lister les workspaces
result = api.workspaces_drive_get()
print(f"Workspaces: {result}")
```

### 5. Exemple complet

```python
from praemunio_sdk import PraemunioClient

# Initialiser le client (sandbox)
client = PraemunioClient.sandbox('pk_test_xxx', 'sk_test_xxx')

# Authentification
client.authenticate()
print("Authentifié avec succès !")

# Premier appel API
api = client.create_api()
workspaces = api.workspaces_drive_get()

print(f"Workspaces: {workspaces}")
```

## 🔐 Authentification

Le SDK gère automatiquement l'authentification et le refresh des tokens :

```python
# Authentification initiale
client.authenticate()

# Le token est renouvelé automatiquement lors des appels API
# Vous pouvez aussi forcer le refresh :
client.refresh()
```

## 🌍 Environnements

| Environnement | URL | Utilisation |
|---------------|-----|-------------|
| **Sandbox** | `https://sandbox-api.praemunio.org/api/v1` | Tests et développement |
| **Live** | `https://api.praemunio.org/api/v1` | Production |

```python
# Sandbox (par défaut)
client = PraemunioClient.sandbox(public_key, secret_key)

# Production
client = PraemunioClient.live(public_key, secret_key)
```

## 📚 Documentation complète

- [Documentation officielle Python](https://docs.praemunio.io/sdk/python)
- [Référence API](https://docs.praemunio.io/api-reference)
- [Guide d'authentification](https://docs.praemunio.io/authentication)
- [Exemples](https://docs.praemunio.io/sdk/python/examples)

## 📋 Endpoints principaux

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `POST` | `/auth/auth-token` | Authentification |
| `GET` | `/workspaces/drive` | Lister les workspaces |
| `POST` | `/teams/create` | Créer une équipe |
| `GET` | `/folders/{id}` | Détails d'un dossier |
| `POST` | `/documents/archive` | Archiver un document |

## 🤝 Support

- 📖 [Documentation](https://docs.praemunio.io)
- 🐛 [Signaler un bug](https://github.com/praemunio/sdks/issues)
- 💬 [Discord](https://discord.gg/praemunio)
- 📧 [Email](mailto:support@praemunio.org)