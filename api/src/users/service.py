from datetime import timedelta

from sqlalchemy.ext.asyncio import AsyncSession

from api.core.config import settings
from api.core.exceptions import UnauthorizedException
from api.core.logging import get_logger
from api.core.security import create_access_token, verify_password
from api.src.users.models import User
from api.src.users.repository import UserRepository
from api.src.users.schemas import LoginData, Token, UserCreate

logger = get_logger(__name__)


class UserService:
    """Service for handling user business logic."""

    def __init__(self, session: AsyncSession):
        self.session = session
        self.repository = UserRepository(session)

    async def create_user(self, user_data: UserCreate) -> User:
        """Create a new user."""
        return await self.repository.create(user_data)

    async def authenticate(self, login_data: LoginData) -> Token:
        """Authenticate user and return token."""
        # Get user
        user = await self.repository.get_by_email(login_data.email)

        # Verify credentials
        if not user or not verify_password(
            login_data.password, str(user.hashed_password)
        ):
            raise UnauthorizedException(detail="Incorrect email or password")

        # Create access token
        access_token = create_access_token(
            data={"sub": str(user.id)},
            expires_delta=timedelta(minutes=settings.JWT_EXPIRATION),
        )

        logger.info(f"User authenticated: {user.email}")
        return Token(access_token=access_token)

    async def get_user(self, user_id: int) -> User:
        """Get user by ID."""
        return await self.repository.get_by_id(user_id)
