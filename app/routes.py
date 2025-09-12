from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from . import schemas, crud, database, auth

router = APIRouter(
    prefix="/measurements",
    tags=["measurements"],
    dependencies=[Depends(auth.verify_token)],  # require token on all endpoints
)


# CREATE (POST)
@router.post("/", response_model=schemas.MeasurementResponse)
def create_measurement(
    measurement: schemas.MeasurementCreate,
    db: Session = Depends(database.get_db),
):
    return crud.create_measurement(db, measurement)


# READ (GET with optional filters)
@router.get("/", response_model=List[schemas.MeasurementResponse])
def get_measurements(
    station_ids: Optional[List[int]] = Query(None),
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    db: Session = Depends(database.get_db),
):
    return crud.get_measurements(db, station_ids, start_date, end_date)


# UPDATE (PUT)
@router.put("/", response_model=schemas.MeasurementResponse)
def update_measurement(
    station_id: int,
    datetime: datetime,
    updates: schemas.MeasurementUpdate,
    db: Session = Depends(database.get_db),
):
    measurement = crud.update_measurement(db, station_id, datetime, updates)
    if not measurement:
        raise HTTPException(status_code=404, detail="Measurement not found")
    return measurement
