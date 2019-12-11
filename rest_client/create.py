import requests

if __name__ == "__main__":
    res = requests.post(
        url='http://localhost:8080/resource_creation',
        data={
            'sensor_id': 't555',
            'temperature': 33.0,
            'datetime': '2019-10-02 09:10:00',
            'location': '2nd Floor, 4th Engineering Building, KoreaTech'
        }
    )

    print(res.status_code)
    print(res.json())