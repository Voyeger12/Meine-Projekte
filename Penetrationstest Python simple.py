import socket
import threading

def scan_port(ip, port):
    """Scannt einen einzelnen Port auf dem angegebenen IP."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout für langsam reagierende Ports
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} ist offen")
            else:
                print(f"[-] Port {port} ist geschlossen")
    except socket.error as e:
        print(f"Fehler beim Scannen von Port {port}: {e}")

def scan_ports_multithreaded(ip, ports):
    """Scannt Ports parallel mittels Multithreading."""
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()
    
    # Warten, dass alle Threads fertig sind
    for thread in threads:
        thread.join()

def log_results(log_file, ip, port, status):
    """Protokolliert Ergebnisse in eine Datei."""
    with open(log_file, "a") as f:
        f.write(f"{ip}:{port} - {status}\n")

# Beispiel-Scan
target_ip = "scanme.nmap.org"  # Oder eine eigene Test-IP
ports = [21, 22, 80, 443, 8080]  # Typische Ports
log_file = "scan_results.txt"  # Log-Datei für Ergebnisse

print(f"Scanne {target_ip}...")

# Beginnt den parallelen Scan
scan_ports_multithreaded(target_ip, ports)

# Loggen der Ergebnisse nach Abschluss
for port in ports:
    # Hier würdest du die tatsächlichen Status der Ports speichern
    log_results(log_file, target_ip, port, "offen" if socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((target_ip, port)) == 0 else "geschlossen")

print(f"Scan abgeschlossen. Ergebnisse sind in {log_file} gespeichert.")
