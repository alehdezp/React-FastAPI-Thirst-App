from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
CRYPTSCHEMA = "bcrypt"
ACCESS_TOKEN_DURATION = 1  # in minutes
SECRET = "f737cc2a55494d5651e8436c3766cca7d89efd526f0643e7cd100f20ea22ab81"
router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=[CRYPTSCHEMA])


class User(BaseModel):
    id: int
    username: str
    mail: str


class UserInDB(User):
    password: str


# --uri "mongodb+srv://aleyadri:password@drink-api.zahpxpn.mongodb.net/?retryWrites=true&w=majority" --collection users --drop --file src/users.json --jsonArray
users_db = {
    "admin": {
        "id": 0,
        "username": "admin",
        "mail": "admin@gmail.com",
        "password": "$2a$12$k5KG6BzXRshTHy8bozsMd.UPdQ6tnxTGOlQgJ0ZlgWmcRAdRX4UyO",
    },
    "adrihp06": {
        "id": 1,
        "username": "adrihp06",
        "mail": "adrihp06@gmail.com",
        "password": "adrihp06",
    },
}


def search_user_db(username: str):
    username_db = users_db.get(username, None)
    if username_db:
        return UserInDB(**users_db[username])


def search_user(username: str):
    username_db = users_db.get(username, None)
    if username_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception

    return search_user(username)


async def get_current_user(user: User = Depends(auth_user)):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials user",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user = search_user_db(form.username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid user")

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password"
        )

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)

    access_token = {"sub": user.username, "exp": expire}
    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
        "token_type": "bearer",
    }


@router.get("/users/me")
async def read_users_me(user: User = Depends(get_current_user)):
    return user
