from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def admin_ping() -> dict[str, str]:
    return {"module": "admin", "status": "ready"}


@router.get("/verification-queue")
def verification_queue() -> dict[str, list[dict[str, str]] | str]:
    return {
        "items": [],
        "message": "Admin verification queue placeholder.",
    }
