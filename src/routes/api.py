from fastapi import APIRouter

from src.routes import root, store, topic, generic

router = APIRouter()
router.include_router(root.router, tags=["root"])
router.include_router(store.router, tags=["store"])
router.include_router(topic.router, tags=["topic"])
router.include_router(generic.router, tags=["generic"])