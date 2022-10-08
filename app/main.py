from fastapi import FastAPI
import prime
import inverting_picture

app = FastAPI()


@app.get("/v1/prime/{number}")
async def prime(number: int):
    return prime.prime_check(number)


@app.get("/v1/picture/invert")
async def invert():
    return inverting_picture.invert()


