import requests

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error: Failed to fetch data. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to connect to the API. {e}")
    return None

# Sample usage
api_url = "https://api.example.com/data"
data = fetch_data_from_api(api_url)
if data:
    print("Fetched data from API:", data)
