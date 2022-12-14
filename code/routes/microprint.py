from fastapi import BackgroundTasks, APIRouter, Request, status
import os
import aiofiles
from uPrintGen import SVGMicroprintGenerator
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/microprint",
    tags=["Microprint"],
)


@router.post("/generate",
             summary="Requests microprint generation.",
             description=("Generates a microprint of a text file with uPrintGen. Returns svg file of the generated microprint"))
async def generate_microprint(request: Request):
    body = b''
    try:
        async for chunk in request.stream():
            body += chunk
    except Exception:
        return {"message": "There was an error uploading the file"}

    microprint_generator = SVGMicroprintGenerator(
        output_filename="/tmp/microprint.svg", text=body.decode())

    microprint_generator.render_microprint()

    return FileResponse("/tmp/microprint.svg")
