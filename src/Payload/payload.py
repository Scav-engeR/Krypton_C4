import requests

def http_get_payload(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"HTTP GET payload sent to {url}")
        else:
            print(f"HTTP GET payload failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP GET payload failed: {e}")