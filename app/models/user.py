from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = Field(default=None)
    primary_phone: Optional[str] = Field(default=None)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"email": "alice@example.com", "full_name": "Alice Smith", "primary_phone": "+1234567890"}
            ]
        }
    }


class UserCreate(UserBase):
    password: str = Field(min_length=8)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "alice@example.com",
                    "full_name": "Alice Smith",
                    "password": "P@ssw0rd!23",
                    "primary_phone": "+1234567890",
                }
            ]
        }
    }


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = Field(default=None, min_length=8)
    primary_phone: Optional[str] = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"full_name": "Alice A. Smith"},
                {"email": "alice+new@example.com"},
                {"primary_phone": "+1234567890"},
                {"password": "P@ssw0rd!23"},
            ]
        }
    }


class User(UserBase):
    id: str

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "examples": [
                {
                    "id": "7e98a8f7-0e22-4f4a-9f3e-5a2d7c6f9e11",
                    "email": "alice@example.com",
                    "full_name": "Alice Smith",
                    "primary_phone": "+1234567890",
                }
            ]
        },
    }
