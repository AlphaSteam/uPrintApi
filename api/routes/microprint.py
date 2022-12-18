from fastapi import BackgroundTasks, APIRouter, Request, status, File
import os
import aiofiles
from uPrintGen import SVGMicroprintGenerator
from fastapi.responses import FileResponse
from json.decoder import JSONDecodeError

router = APIRouter(
    prefix="/microprint",
    tags=["Microprint"],
)


def save_file(file, filename):
    try:
        contents = file.file.read()
        with open(os.path.join("/tmp", filename), 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file(s)"}
    finally:
        file.file.close()


@router.post("/generate",
             summary="Requests microprint generation.",
             description=("Generates a microprint of a text file with uPrintGen. Returns svg file of the generated microprint"))
async def generate_microprint(text_file=File(...), config_file=File(...)):
    save_file(text_file, "microprint.txt")
    save_file(config_file, "config.json")

    try:
        microprint_generator = SVGMicroprintGenerator.from_text_file(
            file_path="/tmp/microprint.txt",
            config_file_path="/tmp/config.json",
            output_filename="/tmp/microprint.svg"
        )

        microprint_generator.render_microprint()

        return FileResponse("/tmp/microprint.svg")
    except JSONDecodeError:
        raise HTTPException(
            status_code=400, detail="Configuration file is not a valid JSON file.")
    except TypeError:
        raise HTTPException(
            status_code=400, detail="Configuration file is not a valid JSON file.")
