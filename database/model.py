from database.db import Base
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, BLOB
# from sqlalchemy.orm import relationship

class Criminals(Base):
    __tablename__ = "Criminal_details"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), index=True, nullable=False)
    father_name = Column(String(length=50), index=True)
    mother_name = Column(String(length=50), index=True)
    gender = Column(String(length=30), index=True, nullable=False)
    age = Column(Integer, index=True)
    nationality = Column(String(length=50), index=True, nullable=False)
    crime = Column(Text(length=100), nullable=False)

     # children = relationship("Criminal_img", back_populates="parent", uselist=False)

# class Criminal_img(Base):
#     __tablename__ = "Criminal_image"
#     id = Column(Integer, primary_key=True)
#     img_id = Column(Integer, ForeignKey("Criminal_details.id"))
#     image_data = Column(BLOB(length=2**32-1), nullable=False)

#     parent = relationship("Criminals", back_populates="children")
