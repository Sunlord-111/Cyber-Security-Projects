import socket 
import datetime
import sys
COMMON_SERVICES = {
    21 : "FTP",
    22 : "SSH",
    23 : "Telnet",
    25 : "SMTP",
    53 : "DNS",
    80 : "HTTP",
    110 : "POP3",
    143 : "IMAP",
    443 : "HTTPS",
    445 : "SMB",
    3306 : "MySQL",
    3389 : "RDP",
    5900 : "VNC",
    8080 : "HTTP-Alt",
    8443 : "HTTPS-Alt"
}

def get_service(port):
    return COMMON_SERVICES.get(port, "Unknown")

def resolve_host(target):
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print(f"Error : Cannot resolve hostname '{target}'")
        sys.exit(1)

def scan_port(ip, port):
    try:
        #Creating a socket object
        #AF_INET = IPv4, SOCK_STREAM = TCP Connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Setting timeout - 1 second 
        sock.settimeout(1)

        # 0 if connected, 1 if not
        result = sock.connect_ex((ip,port))

        #closing connection
        sock.close()

        if result == 0:
            return True
        else:
            return False

    except socket.error as e:
        return False

def scan_range(ip, start_port, end_port):

    open_ports = []
    total = end_port - start_port + 1

    for i, port in enumerate(range(start_port, end_port + 1)):
        #Progress indicator
        progress = (i+1)/total*100
        print(f"Progress : {progress: .1f}% | Scanning port {port}")

        if scan_port(ip,port):
            open_ports.append(port)

        print(" " * 60, end="\r")   #Clear Progress line
        return open_ports

def print_banner():
    print("=" * 55)
    print("         NETWORK PORT SCANNER")
    print("         Built by Sahil | CyberSec Projects")
    print("=" * 55)

def main():
    print_banner()

    #Get user input
    target = input("\nEnter target IP or hostname: ").strip()
    start_port = int(input("Start port (e.g. 1):").strip())
    end_port = int(input("End port (e.g. 1000): ").strip())

    #Resolve hostname to IP
    ip = resolve_host(target)

    print(f"\nTarget : {target} ({ip})")
    print(f"Port Range : {start_port} - {end_port}")
    print(f"Started : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 55)
    print(f"{'PORT':<10} {'SERVICE':<20} {'STATUS'}")
    print("-" * 55)

    open_ports = []
    total = end_port - start_port + 1

    for i, port in enumerate(range(start_port, end_port + 1)):
        progress = (i + 1) / total * 100
        print(f"Scanning... {progress: .1f}%", end = "\r")

        if scan_port(ip, port):
            service = get_service(port)
            print(f"{port:<10} {service:<20} OPEN")
            open_ports.append(port)

    print("-" * 55)
    print(f"\nScan complete at {datetime.datetime.now().strftime('%H:%M:%S')}")
    print(f"Total open ports found: {len(open_ports)}")

    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")

if __name__ == "__main__":
    main()
              