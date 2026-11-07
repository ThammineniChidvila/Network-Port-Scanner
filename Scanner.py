import socket
from datetime import datetime


def show_banner():
    print("=" * 50)
    print("NETWORK PORT SCANNER")
    print("=" * 50)


def scan_port(target, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.1)

    result = scanner.connect_ex((target, port))

    scanner.close()

    return result


def save_results(target, start_time, open_ports):

    with open("results.txt", "w") as file:

        file.write("NETWORK PORT SCANNER REPORT\n")
        file.write("=" * 50 + "\n")
        file.write(f"Target: {target}\n")
        file.write(f"Scan Started: {start_time}\n")
        file.write("=" * 50 + "\n")

        if open_ports:

            for item in open_ports:
                file.write(item + "\n")

        else:
            file.write("No open ports found.\n")


# Main Program Starts Here

show_banner()

target = input("Enter Target IP Address: ")

try:

    start_port = int(input("Enter Starting Port: "))
    end_port = int(input("Enter Ending Port: "))

    if start_port < 1 or end_port > 65535:
        print("Invalid Port Range. Ports must be between 1 and 65535.")
        exit()

except ValueError:

    print("Please enter numbers only for ports.")
    exit()

start_time = datetime.now()

print("\nScanning Target:", target)
print("Scan Started:", start_time)
print("-" * 50)

services = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

open_ports = []
open_count = 0

for port in range(start_port, end_port + 1):

    result = scan_port(target, port)

    service = services.get(port, "Unknown")

    if result == 0:

      output = f"Port {port} OPEN - {service}"

      print(output)

      open_ports.append(output)

      open_count += 1

    else:

      print(f"Port {port} CLOSED - {service}")

end_time = datetime.now()

save_results(target, start_time, open_ports)

print("\n" + "=" * 50)
print("SCAN COMPLETE")
print("=" * 50)
print("Target:", target)
print("Total Open Ports:", open_count)
print("Scan Started :", start_time)
print("Scan Finished:", end_time)
print("Results saved to results.txt")