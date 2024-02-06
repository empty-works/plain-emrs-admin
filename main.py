from typing import Annotated, Union
import datetime
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    first_name: str
    middle_initial: Union[str, None] = None
    last_name: str
    date_of_birth: datetime
    email: Union[str, None] = None
    date_created: datetime
    facility_id: str
    enabled: bool

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", 
        email="cinnar@fakeemail.com",
        first_name="Cinnar",
        last_name="Rennir",
        date_created=datetime.datetime.now(),
        facility_id="fakefacility",
        enabled=True
    )

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
