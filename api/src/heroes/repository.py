from sqlalchemy import delete, select, update
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from api.core.exceptions import AlreadyExistsException, NotFoundException
from api.src.heroes.models import Hero
from api.src.heroes.schemas import HeroCreate, HeroUpdate


class HeroRepository:
    """Repository for handling hero database operations."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, hero_data: HeroCreate) -> Hero:
        """Create a new hero.

        Args:
            hero_data: Hero creation data

        Returns:
            Hero: Created hero

        Raises:
            AlreadyExistsException: If hero with same alias already exists
        """
        hero = Hero(**hero_data.model_dump())
        try:
            self.session.add(hero)
            await self.session.commit()
            await self.session.refresh(hero)
            return hero
        except IntegrityError:
            await self.session.rollback()
            raise AlreadyExistsException(
                f"Hero with alias {hero_data.alias} already exists"
            )

    async def get_by_id(self, hero_id: int) -> Hero:
        """Get hero by ID.

        Args:
            hero_id: Hero ID

        Returns:
            Hero: Found hero

        Raises:
            NotFoundException: If hero not found
        """
        query = select(Hero).where(Hero.id == hero_id)
        result = await self.session.execute(query)
        hero = result.scalar_one_or_none()

        if not hero:
            raise NotFoundException(f"Hero with id {hero_id} not found")
        return hero

    async def get_all(self) -> list[Hero]:
        """Get all heroes.

        Returns:
            List[Hero]: List of all heroes
        """
        query = select(Hero)
        result = await self.session.execute(query)
        return list(result.scalars().all())

    async def update(self, hero_id: int, hero_data: HeroUpdate) -> Hero:
        """Update hero by ID.

        Args:
            hero_id: Hero ID
            hero_data: Hero update data

        Returns:
            Hero: Updated hero

        Raises:
            NotFoundException: If hero not found
        """
        update_data = hero_data.model_dump(exclude_unset=True)
        if not update_data:
            raise ValueError("No fields to update")

        query = update(Hero).where(Hero.id == hero_id).values(**update_data)
        result = await self.session.execute(query)

        if result.rowcount == 0:
            raise NotFoundException(f"Hero with id {hero_id} not found")

        await self.session.commit()
        return await self.get_by_id(hero_id)

    async def delete(self, hero_id: int) -> None:
        """Delete hero by ID.

        Args:
            hero_id: Hero ID

        Raises:
            NotFoundException: If hero not found
        """
        query = delete(Hero).where(Hero.id == hero_id)
        result = await self.session.execute(query)

        if result.rowcount == 0:
            raise NotFoundException(f"Hero with id {hero_id} not found")

        await self.session.commit()
