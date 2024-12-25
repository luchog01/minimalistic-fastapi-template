from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from api.core.database import get_session
from api.core.logging import get_logger
from api.core.security import get_current_user
from api.src.users.models import User
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
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: AsyncSession = Depends(get_session),
) -> Token:
    """Authenticate user and return token."""
    login_data = LoginData(email=form_data.username, password=form_data.password)
    logger.debug(f"Login attempt: {login_data.email}")
    return await UserService(session).authenticate(login_data)


@router.get("/me", response_model=UserResponse)
async def get_me(user: User = Depends(get_current_user)) -> UserResponse:
    """Get current authenticated user."""
    return user
