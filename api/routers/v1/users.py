from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session

from adapters.postgres_db import get_db
from repos.users_repository import UsersRepository
from services.trino_users import TrinoUserService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

service = TrinoUserService()

@router.get("/dwh-users")
def get_dwh_users():
    return service.fetch_users_from_dwh()

def get_users_repo(db: Session = Depends(get_db)):
    return UsersRepository(db)

@router.post("/")
async def create_user(request: Request, repo: UsersRepository = Depends(get_users_repo)):
    data = await request.json()
    if "name" not in data or "email" not in data:
        raise HTTPException(status_code=400, detail="Missing 'name' or 'email'")
    
    existing_user = repo.get_user_by_name(data["name"])
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = repo.create(**data)
    return {
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }

@router.get("/")
def get_users(repo: UsersRepository = Depends(get_users_repo)):
    users = repo.db_session.query(repo.model).all()
    return [
        {"id": user.id, "name": user.name, "email": user.email}
        for user in users
    ]

@router.get("/{user_id}")
def get_user(user_id: int, repo: UsersRepository = Depends(get_users_repo)):
    user = repo.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "name": user.name, "email": user.email}

@router.delete("/{user_id}")
def delete_user(user_id: int, repo: UsersRepository = Depends(get_users_repo)):
    user = repo.delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User {user_id} deleted"}
