from pydantic import BaseModel
from utils import StrEnum


class GPTRequest(BaseModel):
    code_snippet: str


class BroMode(StrEnum):
    CHILL = "chill"
    MID = "mid"
    CHAD = "chad"
