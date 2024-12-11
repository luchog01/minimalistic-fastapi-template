from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.core.database import get_session
from api.core.logging import get_logger
from api.src.users.schemas import LoginData, Token, UserCreate, UserResponse
from api.src.users.service import UserService

logger = get_logger(__name__)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
async def register(
    user_data: UserCreate, session: AsyncSession = Depends(get_session)
) -> UserResponse:
    """Register a new user."""
    logger.debug(f"Registering user: {user_data.email}")
    return await UserService(session).create_user(user_data)


@router.post("/login", response_model=Token)
async def login(
    login_data: LoginData, session: AsyncSession = Depends(get_session)
) -> Token:
    """Authenticate user and return token."""
    logger.debug(f"Login attempt: {login_data.email}")
    return await UserService(session).authenticate(login_data)
