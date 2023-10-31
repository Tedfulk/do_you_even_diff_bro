from pydantic import BaseModel

from py_do_you_even_diff_bro.utils import StrEnum


class GPTRequest(BaseModel):
    code_snippet: str


class BroMode(StrEnum):
    CHILL = "chill"
    MID = "mid"
    CHAD = "chad"
