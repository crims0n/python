import requests, json, argparse

parser = argparse.ArgumentParser(description="Gets US weather data from weather.gov")
parser.add_argument('-ll',
                    '--long-lat',
                    type=int,
                    nargs=2,
                    metavar=('lat', 'long'),
                    help="Latitude and Longitude"
                    )
args = parser.parse_args()

if (args.long_lat):
    pointsRequestURL =f"https://api.weather.gov/points/{args.long_lat[0]},{args.long_lat[1]}"
    print(pointsRequestURL)


apiRequest = 'https://api.weather.gov/gridpoints/RAH/86,62/forecast'

try:
    r = requests.get(apiRequest)
except:
    print("Warning: Unable to Poll API")

def main():
    if r.status_code == 200:
        j = r.json()
        now = j['properties']['periods'][0]['name']
        nowForcast = j['properties']['periods'][0]['detailedForecast']
        later = j['properties']['periods'][1]['name']
        laterForcast = j['properties']['periods'][1]['detailedForecast']
        print(f"{now}: {nowForcast}")
        print(f"{later}: {laterForcast}")
    elif r.status_code == 503:
        j = r.json()
        print(f"{j['title']}: {j['detail']}")
    else:
        print(f"Error: Status Code {r.status_code} Received!")

if __name__ == '__main__':
    main()

