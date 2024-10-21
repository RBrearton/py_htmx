"""
This script contains the definition of the BaseModel class. This is the base
class for all the htmx models.
"""

from pydantic import BaseModel as PydanticBaseModel


class HtmxComponent(PydanticBaseModel):
    """
    The base class for all the htmx models.
    """
