from pydantic import BaseModel, Field
from typing import Optional


class ErrorResponse(BaseModel):
    message: str = Field(description="Human-readable error message")
    code: Optional[int] = Field(default=None, description="Application-specific error code")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"message": "Not implemented", "code": 501},
                {"message": "User not found", "code": 404},
            ]
        }
    }
