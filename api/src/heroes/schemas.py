from pydantic import BaseModel, ConfigDict, Field


class HeroBase(BaseModel):
    """Base schema for Hero data.

    Attributes:
        name: Hero's real name
        alias: Hero's superhero name
        powers: Description of hero's powers
    """

    name: str = Field(..., min_length=1, max_length=100, description="Hero's real name")
    alias: str = Field(
        ..., min_length=1, max_length=100, description="Hero's superhero name"
    )
    powers: str | None = Field(None, description="Description of hero's powers")


class HeroCreate(HeroBase):
    """Schema for creating a new hero."""


class HeroUpdate(BaseModel):
    """Schema for updating an existing hero.

    All fields are optional since updates might be partial.
    """

    name: str | None = Field(None, min_length=1, max_length=100)
    alias: str | None = Field(None, min_length=1, max_length=100)
    powers: str | None = None


class HeroResponse(HeroBase):
    """Schema for hero responses.

    Includes all base fields plus the id.
    """

    model_config = ConfigDict(from_attributes=True)
    id: int
