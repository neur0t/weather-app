import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

client = TestClient(app)

# Setup / Teardown DB for tests
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Recreate schema before each test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


def test_create_measurement():
    response = client.post(
        "/measurements/",
        headers={"x-token": "mysecrettoken"},
        json={
            "datetime": "2025-09-12T10:00:00+00:00",
            "station_id": 1,
            "temperature": 25.3,
            "humidity": 70,
            "wind_speed": 12.5,
            "wind_direction": "N",
            "rainfall": 0.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["station_id"] == 1
    assert data["temperature"] == 25.3


def test_get_measurements():
    # Insert first
    client.post(
        "/measurements/",
        headers={"x-token": "mysecrettoken"},
        json={
            "datetime": "2025-09-12T10:00:00+00:00",
            "station_id": 1,
            "temperature": 20.0,
            "humidity": 60,
            "wind_speed": 10.0,
            "wind_direction": "E",
            "rainfall": 5.0
        }
    )

    response = client.get(
        "/measurements/",
        headers={"x-token": "mysecrettoken"},
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["station_id"] == 1


def test_update_measurement():
    # Insert first
    client.post(
        "/measurements/",
        headers={"x-token": "mysecrettoken"},
        json={
            "datetime": "2025-09-12T10:00:00+00:00",
            "station_id": 1,
            "temperature": 22.0,
            "humidity": 65,
            "wind_speed": 8.0,
            "wind_direction": "S",
            "rainfall": 2.0
        }
    )

    response = client.put(
        "/measurements/?station_id=1&datetime=2025-09-12T10:00:00%2B00:00",
        headers={"x-token": "mysecrettoken"},
        json={
            "temperature": 30.0,
            "humidity": 55,
            "wind_speed": 9.5,
            "wind_direction": "NE",
            "rainfall": 1.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["temperature"] == 30.0
    assert data["humidity"] == 55
