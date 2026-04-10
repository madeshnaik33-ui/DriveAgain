from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def seller_ping() -> dict[str, str]:
    return {"module": "seller", "status": "ready"}


@router.get("/listings")
def seller_listings() -> dict[str, list[dict[str, str]] | str]:
    return {
        "items": [],
        "message": "Seller listings placeholder.",
    }
