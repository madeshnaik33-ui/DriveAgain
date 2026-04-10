from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.admin.routes import router as admin_router
from api.buyer.routes import router as buyer_router
from api.seller.routes import router as seller_router

app = FastAPI(
    title="DriveAgain API",
    version="0.1.0",
    description="Backend API for buyer, seller, and admin applications.",
)

allowed_origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",
    "http://127.0.0.1:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "DriveAgain API", "docs": "/docs"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(buyer_router, prefix="/api/buyer", tags=["buyer"])
app.include_router(seller_router, prefix="/api/seller", tags=["seller"])
app.include_router(admin_router, prefix="/api/admin", tags=["admin"])
