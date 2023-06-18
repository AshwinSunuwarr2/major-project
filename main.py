from fastapi import FastAPI, Depends
from typing import Optional, List, Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database.db import Base, engine, SessionLocal
from database.model import Criminals
import sys

print(sys.path)


Base.metadata.create_all(bind=engine)
app = FastAPI(title="Criminal Face Recognition API")

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class CriminalSchema(BaseModel):
    name: str
    father_name: Optional[str] = None
    mother_name: Optional[str] = None
    gender: str
    age: Optional[int] = None
    nationality: str
    crime: str

    class Config:
        orm_mode = True

# class CriminalImgSchema(BaseModel):
#     img_id: int
#     image_data: bytes
    
#     class Config:
#         orm_mode=True

@app.get("/get-criminals", response_model=List[CriminalSchema])
def get_criminals(db: Session=Depends(get_db)):
    return db.query(Criminals).all() 

@app.post("/add-criminals", response_model=CriminalSchema)
def add_criminals(c: CriminalSchema, db: Session=Depends(get_db)):
    criminal = Criminals(name=c.name, father_name=c.father_name, mother_name=c.mother_name, 
                         age=c.age, gender=c.gender.lower() if c.gender else None, nationality=c.nationality, 
                         crime=c.crime)
    
    db.add(criminal)
    db.commit()

    return criminal



# @app.post("/add-image/{id_img}", response_model=CriminalImgSchema)
# async def add_image(
#     file: UploadFile, id_img: int = Path(..., gt=0), db: Session = Depends(get_db)
# ):
#     try:
#         existing_criminal = db.query(Criminals).filter(Criminals.id == id_img).first()
#         if not existing_criminal:
#             raise HTTPException(status_code=404, detail="Criminal ID not found.")

#         existing_image = db.query(Criminal_img).filter(Criminal_img.img_id == id_img).first()
#         if existing_image:
#             raise HTTPException(status_code=400, detail="Image ID already exists.")

#         image_data = await file.read()
#         image_data_base64 = b64encode(image_data).decode("utf-8")  # Convert bytes to base64-encoded string

#         img = Criminal_img(img_id=id_img, image_data=image_data_base64.encode("utf-8"))  # Explicitly encode image_data
#         db.add(img)
#         db.commit()

#         return {"img_id": img.img_id, "image_data": img.image_data}
#     except IntegrityError as e:
#         raise HTTPException(status_code=400, detail=f"IntegrityError: {e}")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to add image: {e}")





# @app.put("/update-criminal/{c_id}", response_model=CriminalSchema)
# def update_criminal(crim: CriminalSchema, c_id: int, db: Session=Depends(get_db)):
#     try: 
#         i = db.query(Criminals).filter(Criminals.id == c_id).first()
#         i.name = crim.name
#         i.father_name = crim.father_name
#         i.mother_name = crim.mother_name
#         i.gender = crim.gender
#         i.nationality = crim.nationality
#         i.age = crim.age
#         i.crime = crim.crime

#         db.add(i)
#         db.commit()
#         return i
#     except:
#         raise HTTPException(status_code=404, detail="ID not found.")
    

# @app.delete("/delete-criminal/{c_id}", response_class=JSONResponse)
# def delete_criminal(c_id: int, db: Session=Depends(get_db)):
#     try:
#         c = db.query(Criminals).filter(c_id == Criminals.id).first()
#         db.delete(c)
#         db.commit()
#         return f"Criminal of id {c_id} has been deleted."
#     except:
#         raise HTTPException(status_code=404, detail="ID not found.")
