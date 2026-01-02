import requests
def get_current_time():
    url = "https://timeapi.io/api/Time/current/zone?timeZone=Asia/Kolkata"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["dateTime"]

