#The script that will modify the excel sheet and part number

import pandas as pd
from sqlalchemy.orm import Session
from .models import SubAssembly

# Function to process and save BOM data from an uploaded file
def process_and_save_bom(file, user_id: int, db: Session):
    # Read the Excel file using pandas
    try:
        df = pd.read_excel(file)
    except Exception as e:
        raise ValueError(f"Error reading file: {str(e)}")

    # Insert data into the SubAssembly table, associating it with the user_id
    try:
        for _, row in df.iterrows():
            bom_entry = SubAssembly(
                name=row['name'],
                cost=row['cost'],
                lead_time=row['lead_time'],
                notes=row['notes'],
                supplier_id=row['supplier_id'],
                manufacturer_id=row['manufacturer_id'],
                uploaded_by_user_id=user_id  # Associate the data with the authenticated user
            )
            db.add(bom_entry)
        db.commit()
    except Exception as e:
        db.rollback()
        raise ValueError(f"Error inserting data: {str(e)}")
