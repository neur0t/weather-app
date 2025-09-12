from sqlalchemy import Column, Integer, Float, String, DateTime
from .database import Base

class WeatherMeasurement(Base):
    __tablename__ = "measurements"

    station_id = Column(Integer, primary_key=True)
    datetime = Column(DateTime(timezone=True), primary_key=True)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
    wind_direction = Column(String)
    rainfall = Column(Float)
