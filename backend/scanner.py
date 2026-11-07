
import socket
import ipaddress
import time

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP Proxy"
}


def scan_target(target_ip, start_port, end_port, allowed_targets):
    # Validate the target IP
    ip = ipaddress.ip_address(target_ip)

    # Only scan explicitly approved targets
    if str(ip) not in allowed_targets:
        raise PermissionError("This IP address is not an authorized scan target.")

    if not (1 <= start_port <= end_port <= 65535):
        raise ValueError("Invalid port range.")

    results = []
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                status = sock.connect_ex((str(ip), port))

                if status == 0:
                    port_status = "OPEN"
                else:
                    port_status = "CLOSED"

                results.append({
                    "port": port,
                    "service": COMMON_SERVICES.get(port, "Unknown"),
                    "status": port_status
                })

        except OSError:
            results.append({
                "port": port,
                "service": COMMON_SERVICES.get(port, "Unknown"),
                "status": "ERROR"
            })

    return {
        "target": str(ip),
        "total_scanned": len(results),
        "open_ports": sum(
            1 for result in results if result["status"] == "OPEN"
        ),
        "duration": round(time.time() - start_time, 2),
        "results": results
    }
