from fastapi import APIRouter

from app.v1 import proxy

router = APIRouter(prefix='/v1')
router.include_router(proxy.router)
