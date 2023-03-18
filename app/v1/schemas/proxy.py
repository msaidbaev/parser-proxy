from pydantic import BaseModel


class GetRequest(BaseModel):
    """Proxy get request scheme."""

    url: str
    headers: dict | None


class PostRequest(BaseModel):
    """Proxy post request scheme."""

    url: str
    data: dict | str
    headers: dict | None


class ImageRequest(BaseModel):
    """Proxy image request scheme."""

    url: str
    headers: dict | None
