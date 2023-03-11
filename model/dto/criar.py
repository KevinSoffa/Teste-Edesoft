from pydantic.dataclasses import dataclass
from pydantic import Field, HttpUrl


@dataclass
class CriarDTO:
    title: str = Field(...)
    price: float = Field(...)
    description: str = Field(...)
    image: HttpUrl = Field(...)
    category: str = Field(...)
