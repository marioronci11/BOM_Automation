#The script that will modify the excel sheet and part number
# from flask import Flask
# app = Flask(__name__)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "BOM Automation Tool is Running!"}
