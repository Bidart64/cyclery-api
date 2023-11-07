import pytest
from app.main import create_app
from app.models.bicycle import Bicycle

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_get_bicycle(client):
    response = client.get('/bicycles/1')
    assert response.status_code == 200
    assert 'bicycle' in response.get_json()

def test_create_bicycle(client):
    bicycle_data = {
        'name': 'Test Bicycle',
        'description': 'This is a test bicycle',
        'starting_bid': 100,
    }
    response = client.post('/bicycles', json=bicycle_data)
    assert response.status_code == 201
    assert 'bicycle' in response.get_json()

def test_update_bicycle(client):
    bicycle_data = {
        'name': 'Updated Test Bicycle',
        'description': 'This is an updated test bicycle',
        'starting_bid': 150,
    }
    response = client.put('/bicycles/1', json=bicycle_data)
    assert response.status_code == 200
    assert 'bicycle' in response.get_json()

def test_delete_bicycle(client):
    response = client.delete('/bicycles/1')
    assert response.status_code == 204

def test_place_bid(client):
    bid_data = {
        'amount': 200,
    }
    response = client.post('/bicycles/1/bids', json=bid_data)
    assert response.status_code == 201
    assert 'bid' in response.get_json()