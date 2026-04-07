from pydantic import BaseModel
from typing import List, Optional

class Observation(BaseModel):
    task: str
    data: dict
    step_count: int

class Action(BaseModel):
    action_type: str
    payload: dict

class Reward(BaseModel):
    score: float
    feedback: str