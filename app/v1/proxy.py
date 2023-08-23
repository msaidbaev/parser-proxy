import base64
from fastapi import APIRouter

from app.v1.schemas import proxy
from app.cli.cli_httpx import Response, CliHttpx

router = APIRouter(
    prefix='/proxy',
    tags=['Proxy requests'],
)


@router.post('/get', response_model=Response)
async def get_request(body: proxy.GetRequest):
    with open('./debug.txt', 'a') as file:
        file.write(body.url)
    return await CliHttpx().get(body.url, headers=body.headers)


@router.post('/post', response_model=Response)
async def post_request(body: proxy.PostRequest):
    return await CliHttpx().post(body.url, data=body.data, headers=body.headers)


@router.post('/image', response_model=Response)
async def image_request(body: proxy.ImageRequest):
    return await CliHttpx().image(body.url, headers=body.headers)
