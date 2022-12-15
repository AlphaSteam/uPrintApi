from fastapi import BackgroundTasks, APIRouter, Request, status, File
import os
import aiofiles
from uPrintGen import SVGMicroprintGenerator
from fastapi.responses import FileResponse

router = APIRouter(
    prefix="/microprint",
    tags=["Microprint"],
)


def print_files(path):
    l_files = os.listdir(path)

    # Iterating over all the files
    for file in l_files:

        # Instantiating the path of the file
        file_path = f'{path}\\{file}'

        # Checking whether the given file is a directory or not
        if os.path.isfile(file_path):
            try:
                # Printing the file pertaining to file_path
                os.startfile(file_path, 'print')
                print(f'Printing {file}')
            except:
                # Catching if any error occurs and alerting the user
                print(f'ALERT: {file} could not be printed! Please check\
                the associated softwares, or the file type.')
        else:
            print(f'ALERT: {file} is not a file, so can not be printed!')

    print('Task finished!')


def save_file(file, filename):
    try:
        contents = file.file.read()
        with open(os.path.join("tmp", filename), 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file(s)"}
    finally:
        print_files("tmp")
        print_files("tmp/")
        file.file.close()


@router.post("/generate",
             summary="Requests microprint generation.",
             description=("Generates a microprint of a text file with uPrintGen. Returns svg file of the generated microprint"))
async def generate_microprint(log=File(...), config=File(...)):
    save_file(log, "microprint.txt")
    save_file(config, "config.json")

    microprint_generator = SVGMicroprintGenerator.from_text_file(
        file_path=os.path.join("tmp", "microprint.txt"),
        config_file_path=os.path.join("tmp", "config.json"),
        output_filename="/tmp/microprint.svg"
    )

    microprint_generator.render_microprint()

    print_files("tmp")
    print_files("tmp/")

    return FileResponse("/tmp/microprint.svg")
