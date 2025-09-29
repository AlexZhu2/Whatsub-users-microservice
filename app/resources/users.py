from typing import List
from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.models.user import User, UserCreate, UserUpdate
from app.models.common import ErrorResponse
from app.services.user_service import InMemoryUserService


router = APIRouter()


def get_user_service(request: Request) -> InMemoryUserService:
    return request.app.state.user_service


@router.get(
    "/",
    response_model=List[User],
    summary="List users",
    responses={
        501: {
            "model": ErrorResponse,
            "description": "Not implemented",
            "content": {
                "application/json": {
                    "example": {"message": "Not implemented", "code": 501}
                }
            },
        }
    },
)
async def list_users(service: InMemoryUserService = Depends(get_user_service)):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Create a user",
    responses={
        501: {
            "model": ErrorResponse,
            "description": "Not implemented",
            "content": {
                "application/json": {
                    "example": {"message": "Not implemented", "code": 501}
                }
            },
        }
    },
)
async def create_user(
    payload: UserCreate, service: InMemoryUserService = Depends(get_user_service)
):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get(
    "/{user_id}",
    response_model=User,
    summary="Get a user by ID",
    responses={
        404: {
            "model": ErrorResponse,
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {"message": "User not found", "code": 404}
                }
            },
        },
        501: {
            "model": ErrorResponse,
            "description": "Not implemented",
            "content": {
                "application/json": {
                    "example": {"message": "Not implemented", "code": 501}
                }
            },
        },
    },
)
async def get_user(user_id: str, service: InMemoryUserService = Depends(get_user_service)):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.patch(
    "/{user_id}",
    response_model=User,
    summary="Update a user",
    responses={
        404: {
            "model": ErrorResponse,
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {"message": "User not found", "code": 404}
                }
            },
        },
        501: {
            "model": ErrorResponse,
            "description": "Not implemented",
            "content": {
                "application/json": {
                    "example": {"message": "Not implemented", "code": 501}
                }
            },
        },
    },
)
async def update_user(
    user_id: str, payload: UserUpdate, service: InMemoryUserService = Depends(get_user_service)
):
    raise HTTPException(status_code=501, detail="Not implemented")


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a user",
    responses={
        404: {
            "model": ErrorResponse,
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {"message": "User not found", "code": 404}
                }
            },
        },
        501: {
            "model": ErrorResponse,
            "description": "Not implemented",
            "content": {
                "application/json": {
                    "example": {"message": "Not implemented", "code": 501}
                }
            },
        },
    },
)
async def delete_user(user_id: str, service: InMemoryUserService = Depends(get_user_service)):
    raise HTTPException(status_code=501, detail="Not implemented")
