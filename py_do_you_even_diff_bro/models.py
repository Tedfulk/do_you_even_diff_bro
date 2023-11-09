from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator

from py_do_you_even_diff_bro.utils import StrEnum


class BroMode(StrEnum):
    CHILL = "chill"
    MID = "mid"
    CHAD = "chad"


class BugBase(BaseModel):
    bug_id: str
    description: str

    @validator("bug_id")
    def validate_bug_id(cls, v):
        if not v.startswith("B") or not v[1:].isdigit():
            raise ValueError("bug_id must start with B followed by numbers")
        return v


class BugReport(BugBase):
    pass


class BugImprovement(BugBase):
    improvements: str
    code: str


class SeverityReports(BaseModel):
    high: Optional[List[BugReport]] = []
    medium: Optional[List[BugReport]] = []
    low: Optional[List[BugReport]] = []


class SeverityImprovements(BaseModel):
    high: Optional[List[BugImprovement]] = []
    medium: Optional[List[BugImprovement]] = []


class MetaData(BaseModel):
    timestamp: Optional[datetime] = Field(default_factory=datetime.utcnow)
    session_id: Optional[str]
    user_info: Optional[dict]


class ErrorModel(BaseModel):
    error_message: Optional[str]
    error_code: Optional[int]


class CodeReview(BaseModel):
    summary: str
    severities: SeverityReports
    suggestions: SeverityImprovements
    metadata: Optional[MetaData] = Field(default_factory=MetaData)
    error: Optional[ErrorModel]
