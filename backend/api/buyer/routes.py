from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def buyer_ping() -> dict[str, str]:
    return {"module": "buyer", "status": "ready"}


@router.get("/vehicles")
def list_vehicles() -> dict[str, list[dict[str, str]] | str]:
    return {
        "items": [],
        "message": "Buyer vehicle feed placeholder.",
    }
