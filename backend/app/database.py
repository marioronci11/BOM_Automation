from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Limited user connection for backend services
DATABASE_URL = "postgresql://engineer_user:engineer_password@database:5432/prisma"

# Create the engine to connect to the database using the restricted engineer_user
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in the database (if they don't exist already)
def init_db():
    Base.metadata.create_all(bind=engine)