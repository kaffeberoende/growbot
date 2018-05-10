# Gets weather data from SMHI
import requests, json, datetime, logcontroller

# parameter 1 = lufttemperatur varje timme
# Lund 53430
# Lund Lth 53440
# Malmoe: 52350
base_url = "https://opendata-download-metobs.smhi.se/api/version/latest/"
rest_url = "parameter/1/station/52350/period/latest-day/data.json"

headers = {
    'Cache-Control': "no-cache",
    }

weather = "weather"


def get_current_temp():
    response = requests.request("GET", base_url + rest_url, headers=headers)
    parsed_response = json.loads(response.text)
    values = parsed_response["value"]
    readable = [parsed_response["station"]["name"], values[-1]["value"],
                datetime.datetime.fromtimestamp(values[-1]["date"]/1000)]
    logcontroller.append_row(weather, readable)
    # TODO parse latest temperature, or perhaps average?
    return readable
