from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    avatar: str

    model_config = {"from_attributes": True}
