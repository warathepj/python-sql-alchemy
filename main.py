from fastapi import FastAPI, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from sqlalchemy.orm import Session
from typing import List
from database import engine, Base, User, Address, Session as SessionLocal
from pydantic import BaseModel

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure templates
templates = Jinja2Templates(directory="templates")


# Add this new route at the beginning of your routes
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Pydantic models for request/response
class AddressBase(BaseModel):
    email_address: str


class AddressCreate(AddressBase):
    pass


class AddressResponse(AddressBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    name: str
    fullname: str
    nickname: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    addresses: List[AddressResponse] = []

    class Config:
        from_attributes = True


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users", response_class=HTMLResponse)
async def users_page(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse(
        "users.html", {"request": request, "users": users}
    )


@app.get("/users/", response_model=List[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/users/{user_id}/addresses/", response_model=AddressResponse)
def create_address(user_id: int, address: AddressCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_address = Address(**address.model_dump(), user_id=user_id)
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


@app.get("/addresses/", response_model=List[AddressResponse])
def read_addresses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    addresses = db.query(Address).offset(skip).limit(limit).all()
    return addresses


@app.get("/addresses", response_class=HTMLResponse)
async def addresses_page(request: Request, db: Session = Depends(get_db)):
    addresses = db.query(Address).all()
    return templates.TemplateResponse(
        "addresses.html", {"request": request, "addresses": addresses}
    )
