import app, json

def test_get_all_directors_route():
    client = app.connex_app.app.test_client()
    url = '/api/directors'

    response = client.get(url)
    assert response.status_code == 200

def test_get_one_director_route():
    client = app.connex_app.app.test_client()
    url = '/api/directors/4775'

    response = client.get(url)
    assert response.status_code == 200

def test_get_one_director_by_name_route():
    client = app.connex_app.app.test_client()
    url = '/api/directors/name/Jotaro'

    response = client.get(url)
    assert response.status_code == 200

'''
    postnya jalan tapi kecommit ikut create methodnya
'''
# def test_create_director_route():
#     client = app.connex_app.app.test_client()
#     url = '/api/directors'

#     mock_create_data = {
#         "department": "directing",
#         "gender": 2,
#         "name": "Jotaro Kujo",
#         "uid": 1000
#     }

    # headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

    # response = client.post(url, data=json.dumps(mock_create_data), headers=headers)
    # assert response.status_code == 201

def test_update_director_route():
    client = app.connex_app.app.test_client()
    url = '/api/directors/7111'

    mock_update_data = {
        "department": "directing",
        "gender": 2,
        "name": "Jotaro Kujo",
        "uid": 1000
    }

    headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

    response = client.put(url, data=json.dumps(mock_update_data), headers=headers)
    assert response.status_code == 200

    # print(response)

def test_get_all_movies_route():
    client = app.connex_app.app.test_client()
    url = '/api/movies'

    response = client.get(url)
    assert response.status_code == 200

def test_get_all_movies_route():
    client = app.connex_app.app.test_client()
    url = '/api/movies'

    response = client.get(url)
    assert response.status_code == 200

def test_get_one_movie_route():
    client = app.connex_app.app.test_client()
    url = '/api/movies/48400'

    response = client.get(url)
    assert response.status_code == 200


if __name__ == "__main__":
    test_get_all_directors_route()
    test_get_one_director_route()
    # test_create_director_route()
    test_get_one_director_by_name_route()
    test_update_director_route()
    test_get_all_movies_route()
    test_get_one_movie_route()
    print("Everything Passed")