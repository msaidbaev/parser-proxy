import base64
import httpx
from pydantic import BaseModel


class Response(BaseModel):

    status_code: int
    text: str


class CliHttpx:
    """Async client for HTTP requests."""

    async def get(self, url: str, headers: dict | None) -> Response:
        async with httpx.AsyncClient() as cli:
            response = await cli.get(url, headers=headers)
            return Response(
                status_code=response.status_code,
                text=response.text,
            )

    async def image(self, url: str, headers: dict | None) -> Response:
        async with httpx.AsyncClient() as cli:
            response = await cli.get(url, headers=headers)
            return Response(
                status_code=response.status_code,
                text=base64.b64encode(response.content),
            )

    async def post(self, url: str, data: dict, headers: dict | None) -> Response:
        async with httpx.AsyncClient() as cli:
            response = await cli.post(url, data=data, headers=headers)
            return Response(
                status_code=response.status_code,
                text=response.text,
            )
