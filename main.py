from fastapi import FastAPI, Query
from generation_services import generate_pass

app = FastAPI()

@app.get("/api/generate")
def generate_pass_route(
    length = Query(12, ge=4, le=100),
    upper: bool = True,
    number: bool = True,
    symbols: bool = True
):
    return generate_pass(length, upper, number, symbols)