import requests, socket, sys
import csv

sock = socket.socket() # Define socket for tcp conection
param1 = sys.argv[1]   # Get the parameter

# ----[ colors ]----
r = '\033[31m'          # Red
g = '\033[32m'          # Green
b = '\033[34m'          # Blue
c = '\033[36m'          # Cyan
m = '\033[35m'          # Magent
y = '\033[33m'          # Yellow
b = '\033[30m'          # Black
w = '\033[37m'          # White
o = '\033[0;0m'         # Original

def main():
    if param1 == "-h":
        print("""
SysTest 2.0 (https://github.com/MaykonDev/SysTest)
Usage: python SysTest [options] [hostname] [port]

    -h -- Mode help of tool
    -a -- Search vulnerabilies on a host [Example: python SysTest -d https://example.com]
    -i -- Start scanner of vulnerabilies in a IP [Example: python SysTest -i 192.0.0.1]
    """)

    elif param1 == "-a":
        host = sys.argv[2]
        if host == False:
            print("Please, insert a host as parameter")
        
        elif host:
            if "https" in host or "http" in host:
                print("Starting the function, wait!")
                dorks = ["/robots.txt", "/php=id?1", "/admin", "/php.mysql_", "/home.php?", "/index.php?", "/main.php"]
                for line in dorks:
                    url = f"{host}{line}"
                    req = requests.get(url)
                    responses = {404: "OFF - Bad Requests", 200: "ON", 401: "Não Autorizado", 403: "Sem Permissão", 409: "Conflito", 202: "ON"}
                    if req.status_code in responses:
                        print(f" {url} --[ STATUS ] -- {responses.get(req.status_code)}")

            else:
                print("Starting the function, wait!")
                print("adding https in the typed url!")
                new_host = f"https://{host}"
                dorks = ["/robots.txt", "/php=id?1", "/admin", "php.mysql_", "/home.php?", "/index.php?", "/main.php"]
                for line in dorks:
                    url = f"{new_host}{line}"
                    req = requests.get(url)
                    responses = {404: "OFF - Bad Requests", 200: "ON", 401: "Não Autorizado", 403: "Sem Permissão", 409: "Conflito", 202: "ON"}
                    if req.status_code in responses:
                        print(f" {url} --[ STATUS ] -- {responses.get(req.status_code)}")

    elif param1 == "-i":
        IpAddress = sys.argv[2]
        print(f"Starting the port scanner in ip address: {IpAddress}")

        choice = input("verification: would you like to continue the port scanner?\n[1] Yes\n[2] No\n[-] your choice: ")

        if choice == "1":
            print("Scan completed, starting port scanner, please wait!")
            print(f"""
        ------------------------[ CHOICE ]----------------------------\n
        ----[ 1 ]--[ Port Scanner in all ports (65535) ]-----
        ----[ 2 ]--[ Select ports for starting the port scanner ]-----
            """)
            user = input("----[ Your choice ]--> ")
            if user == "1":
                print(f"starting the port scanner in all ports of host: {IpAddress}")
                for ports in range(1, 65535):
                    if sock.connect_ex((IpAddress, ports)) == 0:
                        print(f"----[ Port {ports} open! ]--")
                    else:
                        print(f"----[ Port {ports} close! ]--")
                        sock.close()

            elif user == "2":
                print("----[ Input the ports no commas ]--")
                new_ports = []
                ports_scan = input("---[your ports]--> ")
                for port in ports_scan:
                    new_ports.append(port)
                    for ports in new_ports:
                        if sock.connect_ex((IpAddress, ports)) == 0:
                            print(f"----[ Port {ports} open! ]--")
                        else:
                            print(f"----[ Port {ports} close! ]--")
                            sock.close()

        elif choice == "2":
            new_address = input("----[ Input a IpAddress ]--> ")
            print("\nScan completed, starting port scanner, please wait!")
            print("""
        ------------------------[ CHOICE ]----------------------------\n
        ----[ 1 ]--[ Port Scanner in all ports (65535) ]-----\n
        ----[ 2 ]--[ Select ports for starting the port scanner ]-----
            """)
            type_scan = input("----[ Your choice ]--> ")
            if type_scan == "1":
                print(f"starting the port scanner in all ports of host: {IpAddress}")
                for ports in range(1, 65535):
                    if sock.connect_ex((new_address, ports)) == 0:
                        print(f"----[ Port {ports} open! ]--")
                    else:
                        print(f"----[ Port {ports} close! ]--")
                        sock.close()

            elif type_scan == "2":
                print("----[ Input the ports no commas ]--")
                new_ports = []
                ports_scan = input("---[your ports]--> ")
                for port in ports_scan:
                    new_ports.append(port)
                    for ports in new_ports:
                        if sock.connect_ex((new_address, ports)) == 0:
                            print(f"----[ Port {ports} open! ]--")
                        else:
                            print(f"----[ Port {ports} close! ]--")
                            sock.close()

main()