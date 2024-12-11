from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.core.database import get_session
from api.core.logging import get_logger
from api.core.security import get_current_user
from api.src.heroes.repository import HeroRepository
from api.src.heroes.schemas import HeroCreate, HeroResponse, HeroUpdate
from api.src.heroes.service import HeroService
from api.src.users.models import User

# Set up logger for this module
logger = get_logger(__name__)

router = APIRouter(prefix="/heroes", tags=["heroes"])


def get_hero_service(session: AsyncSession = Depends(get_session)) -> HeroService:
    """Dependency for getting hero service instance."""
    repository = HeroRepository(session)
    return HeroService(repository)


@router.get("/", response_model=list[HeroResponse])
async def get_all_heroes(
    service: HeroService = Depends(get_hero_service),
    current_user: User = Depends(get_current_user),
) -> list[HeroResponse]:
    """Get all heroes."""
    logger.debug("Fetching all heroes")
    try:
        heroes = await service.get_all_heroes()
        logger.info(f"Retrieved {len(heroes)} heroes")
        return heroes
    except Exception as e:
        logger.error(f"Failed to fetch heroes: {str(e)}")
        raise


@router.get("/{hero_id}", response_model=HeroResponse)
async def get_hero(
    hero_id: int,
    service: HeroService = Depends(get_hero_service),
    current_user: User = Depends(get_current_user),
) -> HeroResponse:
    """Get hero by ID."""
    logger.debug(f"Fetching hero {hero_id}")
    try:
        hero = await service.get_hero(hero_id)
        logger.info(f"Retrieved hero {hero_id}")
        return hero
    except Exception as e:
        logger.error(f"Failed to fetch hero {hero_id}: {str(e)}")
        raise


@router.post("/", response_model=HeroResponse, status_code=status.HTTP_201_CREATED)
async def create_hero(
    hero_data: HeroCreate,
    service: HeroService = Depends(get_hero_service),
    current_user: User = Depends(get_current_user),
) -> HeroResponse:
    """Create a new hero."""
    logger.debug("Creating new hero")
    try:
        hero = await service.create_hero(hero_data)
        logger.info(f"Created hero {hero.id}")
        return hero
    except Exception as e:
        logger.error(f"Failed to create hero: {str(e)}")
        raise


@router.patch("/{hero_id}", response_model=HeroResponse)
async def update_hero(
    hero_id: int,
    hero_data: HeroUpdate,
    service: HeroService = Depends(get_hero_service),
    current_user: User = Depends(get_current_user),
) -> HeroResponse:
    """Update hero by ID."""
    logger.debug(f"Updating hero {hero_id}")
    try:
        hero = await service.update_hero(hero_id, hero_data)
        logger.info(f"Updated hero {hero_id}")
        return hero
    except Exception as e:
        logger.error(f"Failed to update hero {hero_id}: {str(e)}")
        raise


@router.delete("/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(
    hero_id: int,
    service: HeroService = Depends(get_hero_service),
    current_user: User = Depends(get_current_user),
) -> None:
    """Delete hero by ID."""
    logger.debug(f"Deleting hero {hero_id}")
    try:
        await service.delete_hero(hero_id)
        logger.info(f"Deleted hero {hero_id}")
    except Exception as e:
        logger.error(f"Failed to delete hero {hero_id}: {str(e)}")
        raise
