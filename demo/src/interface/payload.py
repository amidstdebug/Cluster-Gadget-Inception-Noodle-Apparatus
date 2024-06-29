from typing import Optional, List, Dict
from pydantic import BaseModel

class Payload(BaseModel):
	background: str
	goal: str
	max_depth: Optional[int] = 2
	max_nodes: Optional[int] = 2