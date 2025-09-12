from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models, schemas

# CREATE
def create_measurement(db: Session, measurement: schemas.MeasurementCreate):
    db_measurement = models.WeatherMeasurement(
        station_id=measurement.station_id,
        datetime=measurement.datetime,
        temperature=measurement.temperature,
        humidity=measurement.humidity,
        wind_speed=measurement.wind_speed,
        wind_direction=measurement.wind_direction,
        rainfall=measurement.rainfall,
    )
    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    return db_measurement


# READ (all or filtered by station/date)
def get_measurements(db: Session, station_ids: list[int] = None, start_date=None, end_date=None):
    query = db.query(models.WeatherMeasurement)

    if station_ids:
        query = query.filter(models.WeatherMeasurement.station_id.in_(station_ids))

    if start_date:
        query = query.filter(models.WeatherMeasurement.datetime >= start_date)
    if end_date:
        query = query.filter(models.WeatherMeasurement.datetime <= end_date)

    return query.all()


# UPDATE (only values, not station_id/datetime)
def update_measurement(db: Session, station_id: int, datetime, updates: schemas.MeasurementUpdate):
    measurement = db.query(models.WeatherMeasurement).filter(
        and_(
            models.WeatherMeasurement.station_id == station_id,
            models.WeatherMeasurement.datetime == datetime
        )
    ).first()

    if not measurement:
        return None

    # Update only value fields
    measurement.temperature = updates.temperature
    measurement.humidity = updates.humidity
    measurement.wind_speed = updates.wind_speed
    measurement.wind_direction = updates.wind_direction
    measurement.rainfall = updates.rainfall

    db.commit()
    db.refresh(measurement)
    return measurement
