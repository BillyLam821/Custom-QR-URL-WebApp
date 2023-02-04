from src import create_app

# test if shorten can be found
def test_shorten(client):
    response = client.get('/')
    assert b'Shorten' in response.data