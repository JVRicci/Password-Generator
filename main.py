from fastapi import FastAPI, Query, HTTPException
import random
import string

app = FastAPI()

@app.get("/api/generate")
def generate_pass_route(
    length = Query(12, ge=4, le=100),
    upper: bool = True,
    number: bool = True,
    symbols: bool = True
):
    characters= string.ascii_lowercase

    if upper:
        characters += string.ascii_uppercase

    if number:
        characters += string.digits

    if symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if not characters:
        raise HTTPException(status_code= 400, detail= "Nenhum conjunto de caracteres selecionado" )

    return { "password": "".join(random.choice(characters) for _ in range(length)) }