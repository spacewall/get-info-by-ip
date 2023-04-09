import requests
from pyfiglet import Figlet as fi
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[INTERNET PROVIDER]': response.get('isp'),
            '[COUNTRY]': response.get('country'),
            '[REGION]': response.get('regionName'),
            '[CITY]': response.get('city'),
            '[ZIP CODE]': response.get('zip'),
            '[LAT]': response.get('lat'),
            '[LON]':response.get('lon')
        }

        coordinates = [response.get('lat'), response.get('lon')]
        name_for_map = [
            response.get("query"),
            response.get("country"),
            response.get("regionName"),
            response.get("city")
        ]

        for key, body in data.items():
            print(f'{key} : {body}')
        
        return name_for_map, coordinates 
    except requests.exceptions.ConnectionError:
        print("[!] Bad connection please check your connection")

def get_map(data):
    name_for_map = data[0]
    coordinates = data[1]
    try:
        answer = input("Do you want to create a map? Print y/n: ")
        if answer == 'y':
            print("Map creating...")
            location = folium.Map(location=coordinates, zoom_start=8)
            folium.Marker(location=coordinates, popup = "Target mark", icon=folium.Icon(color = 'gray')).add_to(location)
            location.save(outfile=f'{name_for_map[0]}, {name_for_map[1]}, {name_for_map[2]}, {name_for_map[3]}.html')
            print("The map have been create!")
        elif answer == 'n':
            pass
        else:
            print("[!] Unknown command")
    except:
        print("[!] A map can't be created")

def main():
    preview_text = fi(font='slant')
    print(preview_text.renderText('INFO BY IP'))

    ip = input("Please enter a target IP: ")
    get_map(get_info_by_ip(ip))

if __name__ == '__main__':
    main()