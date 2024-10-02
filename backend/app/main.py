
# main.py

from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, init_db
from .models import Supplier
from .bom_automation import process_and_save_bom

# Initialize the database (create tables if not already created)
init_db()

app = FastAPI()

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to add a supplier
@app.post("/add_supplier/")
def add_supplier(name: str, db: Session = Depends(get_db)):
    new_supplier = Supplier(name=name)
    db.add(new_supplier)
    db.commit()
    return {"message": "Supplier added successfully"}

# Endpoint to upload BOM data
@app.post("/upload_bom/")
async def upload_bom(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Call the function from bom_automation.py to process the file
        process_and_save_bom(file.file, user_id, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    return {"message": "Upload successful"}
