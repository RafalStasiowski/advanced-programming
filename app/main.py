from fastapi import FastAPI
import prime.prime as prime
import inverting_picture.inverting_picture as inverting_picture
import time_encode.time_encode as time

app = FastAPI()


@app.get("/")
async def root():
    return {}


@app.get("/v1/prime/{number}")
async def prime_checker(number: int):
    return {"result": prime.check_prime(number)}


@app.get("/v1/picture/invert")
async def invert_picture():
    return inverting_picture.invert()


@app.get("/v1/time")
async def get_time():
    return time.get_time()
