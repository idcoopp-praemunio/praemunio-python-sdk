from openapi_client.api.default_api import DefaultApi
from openapi_client.configuration import Configuration
from openapi_client.api_client import ApiClient
from openapi_client.models.authenticate_request import AuthenticateRequest

SANDBOX_URL = "https://sandbox-api.praemunio.org/api/v1"
LIVE_URL = "https://api.praemunio.org/api/v1"


class WorkspacesApi:
    """Workspaces API wrapper."""

    def __init__(self, api: DefaultApi):
        self._api = api

    def list(self, team_id: str = None):
        """List all workspaces, optionally filtered by team."""
        return self._api.workspaces_get(team_id=team_id)

    def drive(self):
        """Get the drive (root folders) for the authenticated user."""
        return self._api.workspaces_drive_get()

    def teams(self, team_id: str = None):
        """Get teams associated with workspaces."""
        return self._api.workspaces_teams_get(team_id=team_id)

    def details(self, workspace_id: str = None):
        """Get workspace details."""
        return self._api.workspaces_details_get(workspace_id=workspace_id)

    def create(self, workspace_create_request):
        """Create a new workspace."""
        return self._api.workspaces_create_post(workspace_create_request)

    def update(self, workspace_update_request):
        """Update a workspace."""
        return self._api.workspaces_update_put(workspace_update_request)

    def delete(self, workspace_delete_request):
        """Delete a workspace."""
        return self._api.workspaces_delete_delete(workspace_delete_request)


class TeamsApi:
    """Teams API wrapper."""

    def __init__(self, api: DefaultApi):
        self._api = api

    def list(self):
        """List all teams."""
        return self._api.teams_get()

    def dashboard(self):
        """Get teams dashboard data."""
        return self._api.teams_dashboard_get()

    def info(self, body=None, team_id=None):
        """Get team information."""
        return self._api.teams_info_get(body=body, team_id=team_id)

    def workspaces(self, team_id: str = None):
        """Get workspaces associated with teams."""
        return self._api.teams_workspaces_get(team_id=team_id)

    def logs(self, team_id=None, page=None, limit=None):
        """Get team logs."""
        return self._api.teams_logs_get(team_id=team_id, page=page, limit=limit)

    def create(self, team_create_request):
        """Create a new team."""
        return self._api.teams_create_post(team_create_request)

    def update(self, team_update_request):
        """Update a team."""
        return self._api.teams_update_put(team_update_request)

    def delete(self, team_delete_request):
        """Delete a team."""
        return self._api.teams_delete_delete(team_delete_request)


class TeamsMembersApi:
    """Teams Members API wrapper."""

    def __init__(self, api: DefaultApi):
        self._api = api

    def list(self, team_id: str = None, page: int = None, limit: int = None):
        """List team members with pagination."""
        return self._api.teams_members_get(team_id=team_id, page=page, limit=limit)

    def add(self, team_member_add_request):
        """Add a member to a team."""
        return self._api.teams_members_add_post(team_member_add_request)


class FoldersApi:
    """Folders API wrapper."""

    def __init__(self, api: DefaultApi):
        self._api = api

    def list(self, workspace_id: str):
        """List folders in a workspace."""
        return self._api.folders_get(workspace_id=workspace_id)

    def content(self, folder_id=None):
        """Get folder content."""
        return self._api.folders_content_get(folder_id=folder_id)

    def details(self, folder_id: str = None):
        """Get folder details."""
        return self._api.folders_details_get(folder_id=folder_id)

    def create(self, folder_create_request):
        """Create a new folder."""
        return self._api.folders_create_post(folder_create_request)

    def update(self, folder_update_request):
        """Update a folder."""
        return self._api.folders_update_put(folder_update_request)

    def move(self, folder_delete_request):
        """Move a folder."""
        return self._api.folders_move_post(folder_delete_request)

    def delete(self, folder_delete_request):
        """Delete a folder."""
        return self._api.folders_delete_delete(folder_delete_request)


class DocumentsApi:
    """Documents API wrapper."""

    def __init__(self, api: DefaultApi):
        self._api = api

    def list(self, workspace_id: str = None):
        """List documents in a workspace."""
        return self._api.documents_get(workspace_id=workspace_id)

    def details(self, document_id: str = None):
        """Get document details."""
        return self._api.documents_details_get(document_id=document_id)

    def upload(self, workspace_id=None, folder_id=None, file1=None, file2=None):
        """Upload a document."""
        return self._api.documents_upload_post(
            workspace_id=workspace_id,
            folder_id=folder_id,
            file1=file1,
            file2=file2
        )

    def stream(self, body, document_id=None):
        """Stream a document."""
        return self._api.documents_stream_get(body=body, document_id=document_id)

    def archive(self, document_archive_request):
        """Archive a document."""
        return self._api.documents_archive_post(document_archive_request)

    def restore(self, document_restore_request):
        """Restore an archived document."""
        return self._api.documents_restore_post(document_restore_request)

    def move(self, document_move_request):
        """Move a document."""
        return self._api.documents_move_post(document_move_request)

    def update(self, document_update_request):
        """Update a document."""
        return self._api.documents_update_put(document_update_request)

    def delete(self, document_delete_request):
        """Delete a document."""
        return self._api.documents_delete_delete(document_delete_request)


class PraemunioClient:
    def __init__(self, public_key: str, secret_key: str, base_url: str = SANDBOX_URL):
        self.public_key = public_key
        self.secret_key = secret_key
        self.base_url = base_url.rstrip("/")
        self.access_token = None
        self.refresh_token = None
        self._workspaces = None
        self._teams = None
        self._teams_members = None
        self._folders = None
        self._documents = None

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

    @property
    def workspaces(self) -> WorkspacesApi:
        """Get the Workspaces API."""
        if self._workspaces is None:
            self._workspaces = WorkspacesApi(self.create_api())
        return self._workspaces

    @property
    def teams(self) -> TeamsApi:
        """Get the Teams API."""
        if self._teams is None:
            self._teams = TeamsApi(self.create_api())
        return self._teams

    @property
    def teams_members(self) -> TeamsMembersApi:
        """Get the Teams Members API."""
        if self._teams_members is None:
            self._teams_members = TeamsMembersApi(self.create_api())
        return self._teams_members

    @property
    def folders(self) -> FoldersApi:
        """Get the Folders API."""
        if self._folders is None:
            self._folders = FoldersApi(self.create_api())
        return self._folders

    @property
    def documents(self) -> DocumentsApi:
        """Get the Documents API."""
        if self._documents is None:
            self._documents = DocumentsApi(self.create_api())
        return self._documents

    def get_access_token(self):
        return self.access_token

    def get_refresh_token(self):
        return self.refresh_token