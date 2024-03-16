from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,func,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

class SpecializationDB(Base):
    __tablename__ = "specializations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    speciality_name = Column(String(255), nullable=False)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    phc_tbc_user_details = relationship("Phc_tbc_user_detailsDB", back_populates="specializations")
    
    user = relationship("UsersDB", back_populates="specializations")
    
