from api.src.heroes.repository import HeroRepository
from api.src.heroes.schemas import HeroCreate, HeroResponse, HeroUpdate


class HeroService:
    """Service layer for hero operations."""

    def __init__(self, repository: HeroRepository):
        self.repository = repository

    async def create_hero(self, hero_data: HeroCreate) -> HeroResponse:
        """Create a new hero.

        Args:
            hero_data: Hero creation data

        Returns:
            HeroResponse: Created hero data
        """
        hero = await self.repository.create(hero_data)
        return HeroResponse.model_validate(hero)

    async def get_hero(self, hero_id: int) -> HeroResponse:
        """Get hero by ID.

        Args:
            hero_id: Hero ID

        Returns:
            HeroResponse: Hero data
        """
        hero = await self.repository.get_by_id(hero_id)
        return HeroResponse.model_validate(hero)

    async def get_all_heroes(self) -> list[HeroResponse]:
        """Get all heroes.

        Returns:
            List[HeroResponse]: List of all heroes
        """
        heroes = await self.repository.get_all()
        return [HeroResponse.model_validate(hero) for hero in heroes]

    async def update_hero(self, hero_id: int, hero_data: HeroUpdate) -> HeroResponse:
        """Update hero by ID.

        Args:
            hero_id: Hero ID
            hero_data: Hero update data

        Returns:
            HeroResponse: Updated hero data
        """
        hero = await self.repository.update(hero_id, hero_data)
        return HeroResponse.model_validate(hero)

    async def delete_hero(self, hero_id: int) -> None:
        """Delete hero by ID.

        Args:
            hero_id: Hero ID
        """
        await self.repository.delete(hero_id)
