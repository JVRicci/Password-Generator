from fastapi import FastAPI, Query, HTTPException
from generation_services import generate_pass

app = FastAPI()

@app.get("/api/generate")
def generate_pass_route(
    length: int = Query(12),
    upper: bool = True,
    number: bool = True,
    symbols: bool = True
):
    if length > 25 or length <= 1:
        raise HTTPException(status_code=400, detail="Tamanho de senha inválido") 
    
    return generate_pass(length, upper, number, symbols)