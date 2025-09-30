import uuid
from typing import Dict, List, Optional

from app.models.user import User, UserCreate, UserUpdate


class InMemoryUserService:
    def __init__(self, logger):
        self.logger = logger
        self.users: Dict[str, Dict] = {}

    def list_users(self) -> List[User]:
        return [User(**user) for user in self.users.values()]

    def get_user(self, user_id: str) -> Optional[User]:
        data = self.users.get(user_id)
        return User(**data) if data else None

    def create_user(self, payload: UserCreate) -> User:
        user_id = str(uuid.uuid4())
        user = {
            "id": user_id,
            "email": payload.email,
            "full_name": payload.full_name,
            "primary_phone": payload.primary_phone,
        }
        # NOTE: Do not store plaintext passwords; this is a placeholder for demo
        self.users[user_id] = user
        self.logger.info("user_created", user_id=user_id)
        return User(**user)

    def update_user(self, user_id: str, payload: UserUpdate) -> Optional[User]:
        existing = self.users.get(user_id)
        if not existing:
            return None
        if payload.email is not None:
            existing["email"] = payload.email
        if payload.full_name is not None:
            existing["full_name"] = payload.full_name
        if payload.primary_phone is not None:
            existing["primary_phone"] = payload.primary_phone
        self.users[user_id] = existing
        self.logger.info("user_updated", user_id=user_id)
        return User(**existing)

    def delete_user(self, user_id: str) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            self.logger.info("user_deleted", user_id=user_id)
            return True
        return False
