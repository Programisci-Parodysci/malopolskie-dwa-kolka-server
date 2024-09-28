import requests


def register_user(email, password):
    url = 'http://localhost:5000/register'
    data = {
        'email': email,
        'password': password
    }

    response = requests.post(url, json=data)
    print(response.json())


def login_user(email, password):
    url = 'http://localhost:5000/login'
    data = {
        'email': email,
        'password': password
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        token = response.json()['token']
        print(f'Zalogowano. Token: {token}')
        return token
    else:
        print(response.json())
        return None


def add_gpx(token, gpx_content):
    url = 'http://localhost:5000/add_gpx'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'gpx_file': gpx_content
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())


def get_gpx(token):
    url = 'http://localhost:5000/get_gpx'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        gpx_files = response.json().get('gpx_files', [])
        print("Pobrane pliki GPX:")
        for gpx in gpx_files:
            print(gpx)
    else:
        print(response.json())


# Główna logika
email = 'marekbetoniarek@kurczaczek.pl'
password = 'tereferekuku'

# Rejestracja
register_user(email, password)

# Logowanie
token = login_user(email, password)

# Dodanie pliku GPX, jeśli logowanie było udane
if token:
    gpx_content = """<?xml version="1.0" encoding="UTF-8"?>
    <gpx version="1.1" creator="GPSBabel - http://www.gpsbabel.org">
      <wpt lat="48.8566" lon="2.3522">
        <name>Point 1</name>
      </wpt>
      <wpt lat="51.5074" lon="-0.1278">
        <name>Point 2</name>
      </wpt>
    </gpx>"""

    add_gpx(token, gpx_content)

    # Pobranie plików GPX
    get_gpx(token)
