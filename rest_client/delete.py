import requests

if __name__ == "__main__":
    res = requests.delete(
        url='http://127.0.0.1:8080/resource/t1'
    )

    print(res.status_code)
    print(res.json())