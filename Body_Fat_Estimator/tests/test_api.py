import pytest
from flask import json
from app import app 

# def test_health():
#     # url = '/'
#     response = app.test_client().get('/')
#     assert response.get_data() == b'All good'
#     assert response.status_code == 200

def test_app():  

    test_data = {
        'density':1.0372,
        'abdomen':113.8,
        'weight':219.15,
        'chest':117.6,
        'hip':111.8
    }

    # test_data = {('density', '1.0372'), ('abdomen', '219.15'), 
    # ('chest', '117.6'), ('weight', '89.7'), ('hip', '121.0')}

    # json.dumps(test_data)

    response = app.test_client().post(
        '/',
        data=test_data,
        #content_type='application/json',
    )

    # data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    #assert data['sum'] == 3
