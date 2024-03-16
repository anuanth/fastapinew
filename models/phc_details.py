from database.database import Base
from sqlalchemy import Column, String, Integer, TIMESTAMP,Text,ForeignKey,func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

class Phc_detailsDB(Base):
    __tablename__ = "phc_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    zone_ID = Column(Integer, ForeignKey("zones.id"), default=None)
    phc_name = Column(String(255), nullable=False)
    remarks = Column(Text, nullable=True)
    status = Column(Integer, default=0)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    user = relationship("UsersDB", back_populates="phc_details")

    phc_domain_details = relationship('Phc_domain_detailsDB', back_populates='phc_details')

    zones= relationship("ZoneDB",back_populates="phc_details")

    phc_tbc_user_details = relationship("Phc_tbc_user_detailsDB", back_populates="phc_details")
    
    phc_tbc_code=relationship("Phc_tbc_codeDB",back_populates="phc_details")
