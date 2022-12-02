from fastapi import FastAPI

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


@app.get("/v1/picture/invert")
async def invert_picture():
    return inverting_picture.invert()


@app.get("/v1/time")
async def get_time():
    return time_encode.get_time()
