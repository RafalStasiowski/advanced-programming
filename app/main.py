from fastapi import FastAPI, File, UploadFile

from app.inverting_picture import inverting_picture
from app.prime.prime import check_prime
from app.time_encode import time_encode

app = FastAPI()


@app.get("/")
async def root():
    return {}


@app.get("/v1/prime/{number}")
async def prime_checker(number: int):
    return {"result": check_prime(number)}


@app.post("/v1/picture/invert")
async def invert_picture(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {inverting_picture.invert(file)}"}


@app.get("/v1/time")
async def get_time():
    return time_encode.get_time()
