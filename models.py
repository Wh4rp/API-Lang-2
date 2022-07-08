from pydantic import BaseModel, Field

from enum import Enum

class Language(Enum):
    cpp = "cpp"
    python = "python"

class Code(BaseModel):
    language: Language = Field(
        ...,
        description="Language of the source code", 
        example=Language.python,
        )
    code: str = Field(
        ...,
        description="Code to be run",
        example="eCA9IGlucHV0KCkKcHJpbnQoeCk",
        )
    input_source: str = Field(
        default=None,
        description="Input source code",
        example="SSdtIGEgaW5wdXQ",
        )