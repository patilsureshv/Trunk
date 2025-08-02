import json
import pytest
from swiggy_clone.app import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_restaurants(client):
    """Test the /restaurants endpoint."""
    response = client.get('/restaurants')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    # Check for expected keys in the first restaurant object
    assert "id" in data[0]
    assert "name" in data[0]
    assert "cuisine" in data[0]
    assert "rating" in data[0]
