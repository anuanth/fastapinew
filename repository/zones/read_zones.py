from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.zones import ZoneDB

def read_zones(db: Session, user_id: int):
    try:
        zones = db.query(ZoneDB).filter(
            ZoneDB.user_id == user_id
        ).all()

        for zone in zones:
            zone.user_id = str(zone.user_id)

        return zones

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
