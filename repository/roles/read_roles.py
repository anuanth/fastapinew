from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.roles import RolesDB

def read_roles_all(db: Session, user_id: int):
    try:
        roles = db.query(RolesDB).filter(
            RolesDB.user_id == user_id
        ).all()

        for role in roles:
            role.user_id = str(role.user_id)
        return roles

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
