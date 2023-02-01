import requests

apikey_new = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'


def get_static(**params):
    url = 'https://static-maps.yandex.ru/1.x/?'
    response = requests.get(url, params=params)
    return response.content


def geocode(adress):
    url = f"https://geocode-maps.yandex.ru/1.x/?"
    params = {
        'apikey': '40d1649f-0493-4b70-98ba-98533de7710b',
        'geocode': adress,
        'format': 'json'
    }

    response = requests.get(url, params=params)
    if not response:
        # обработка ошибочной ситуации
        pass
    return response.json()


def get_spn_from_toponym(toponym):
    long1, lat1 = map(float, toponym['boundedBy']['Envelope']['lowerCorner'].split())
    long2, lat2 = map(float, toponym['boundedBy']['Envelope']['upperCorner'].split())
    spn = long2 - long1, lat2 - lat1
    return spn


def get_relevant_toponym(json_response):
    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    return toponym


def get_coord_toponym(toponym):
    toponym_coordinates = toponym["Point"]["pos"]
    toponym_coordinates = map(float, toponym_coordinates.split(" "))
    return list(toponym_coordinates)


def search_maps(**params):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    params['apikey'] = params.get('apikey', apikey_new)
    params['lang'] = params.get('lang', 'ru_RU')

    response = requests.get(search_api_server, params=params)
    if not response:
        pass

#
