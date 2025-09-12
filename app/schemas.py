from pydantic import BaseModel, Field
from datetime import datetime

class MeasurementBase(BaseModel):
    temperature: float = Field(..., ge=-50, le=60)
    humidity: float = Field(..., ge=0, le=100)
    wind_speed: float = Field(..., ge=0)
    wind_direction: str
    rainfall: float = Field(..., ge=0)

class MeasurementCreate(MeasurementBase):
    station_id: int
    datetime: datetime

class MeasurementUpdate(MeasurementBase):
    pass

class MeasurementResponse(MeasurementCreate):
    class Config:
        orm_mode = True
