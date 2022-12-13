from fastapi import BackgroundTasks, APIRouter, HTTPException

router = APIRouter(
    prefix="/microprint",
    tags=["Microprint"],
)
