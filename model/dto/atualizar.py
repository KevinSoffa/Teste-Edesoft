from pydantic.dataclasses import dataclass
from pydantic import Field, HttpUrl


@dataclass
class AtualizarDTO:
    title: str = Field(None)
    price: float = Field(None)
    description: str = Field(None)
    image: HttpUrl = Field(None)
    category: str = Field(None)
