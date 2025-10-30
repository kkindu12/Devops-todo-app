import pytest
import os
import tempfile
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        with app.app.app_context():
            app.init_db()
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'DevOps Todo Application' in response.data

def test_add_todo(client):
    response = client.post('/add', data={'task': 'Test Task'})
    assert response.status_code == 302  # Redirect

def test_toggle_todo(client):
    client.post('/add', data={'task': 'Test Task'})
    response = client.get('/toggle/1')
    assert response.status_code == 302