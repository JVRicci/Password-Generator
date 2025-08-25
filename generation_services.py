from fastapi import FastAPI, Query, HTTPException
import random
import string

def generate_pass(length: int, upper: bool, number: bool, symbols: bool):
    """ Gera senha com base nos paramtros selecionados """
    characters = string.ascii_lowercase

    if upper:
        characters += string.ascii_uppercase
    if number:
        characters += string.digits
    if symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/"

    if not characters:
        raise HTTPException(status_code=400, detail="Nenhum conjunto de caracteres selecionado")

    return {"password": "".join(random.choice(characters) for _ in range(length))}