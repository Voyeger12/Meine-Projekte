import socket
import tkinter as tk
from tkinter import scrolledtext
from concurrent.futures import ThreadPoolExecutor
import threading

# Standardports für den Scan
STANDARD_PORTS = [21, 22, 80, 443, 8080, 3306, 53, 25]

def scan_port(ip, port, result_text):
    """Scannt einen einzelnen Port auf dem angegebenen IP und gibt das Ergebnis in der GUI aus."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout für langsam reagierende Ports
            result = s.connect_ex((ip, port))
            if result == 0:
                result_text.insert(tk.END, f"[+] Port {port} ist offen\n")
            else:
                result_text.insert(tk.END, f"[-] Port {port} ist geschlossen\n")
    except socket.error as e:
        result_text.insert(tk.END, f"Fehler beim Scannen von Port {port}: {e}\n")
    result_text.yview(tk.END)  # Scrollt zum letzten Eintrag

def scan_ports_multithreaded(ip, ports, result_text, status_label):
    """Scannt Ports parallel mittels Thread-Pool und gibt Ergebnisse in die GUI aus."""
    status_label.config(text="Scan läuft...")
    with ThreadPoolExecutor(max_workers=10) as executor:  # Thread-Pool mit maximal 10 gleichzeitigen Threads
        futures = [executor.submit(scan_port, ip, port, result_text) for port in ports]
        for future in futures:
            try:
                future.result()  # Warte auf den Abschluss des Scanvorgangs
            except Exception as e:
                result_text.insert(tk.END, f"Fehler beim Scannen: {e}\n")
                result_text.yview(tk.END)
    status_label.config(text="Scan abgeschlossen.")

def start_scan(result_text, status_label):
    """Startet den Scan basierend auf den Benutzereingaben in der GUI, Standardports automatisch aktivieren."""
    target_ip = ip_entry.get()
    if not target_ip:
        result_text.insert(tk.END, "Bitte eine Ziel-IP eingeben.\n")
        return

    # Portauswahl aus dem Dropdown-Menü
    selected_ports = port_var.get()

    # Falls "Alle Ports (1-1024)" ausgewählt wurde, scanne alle Ports
    if selected_ports == "Alle Ports (1-1024)":
        ports = list(range(1, 1025))  # Alle Ports von 1 bis 1024
    else:
        # Extrahieren der Portnummer aus der Auswahl, indem wir den Text teilen
        try:
            port_number = int(selected_ports.split()[0])  # Extrahiere die Portnummer aus der Auswahl
            ports = [port_number]  # Erstelle eine Liste mit dem ausgewählten Port
        except ValueError:
            result_text.insert(tk.END, f"Ungültige Portauswahl: {selected_ports}\n")
            return

    result_text.delete(1.0, tk.END)  # Löscht vorherige Ergebnisse
    result_text.insert(tk.END, f"Scanne {target_ip}...\n")
    # Starten des Scans im Hintergrund (damit die GUI nicht blockiert)
    threading.Thread(target=scan_ports_multithreaded, args=(target_ip, ports, result_text, status_label), daemon=True).start()

# GUI mit Tkinter
root = tk.Tk()
root.title("Portscanner")

# Eingabefelder
ip_label = tk.Label(root, text="Ziel-IP:")
ip_label.grid(row=0, column=0, padx=10, pady=10)
ip_entry = tk.Entry(root, width=30)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

# Dropdown-Menü für die Portauswahl
port_label = tk.Label(root, text="Wählen Sie einen Port oder einen Bereich:")
port_label.grid(row=1, column=0, padx=10, pady=10)

# Optionen für das Dropdown-Menü
port_options = [
    "21 (FTP)", "22 (SSH)", "80 (HTTP)", "443 (HTTPS)", 
    "8080 (HTTP-Alternative)", "3306 (MySQL)", "53 (DNS)", "25 (SMTP)", 
    "Alle Ports (1-1024)"
]
port_var = tk.StringVar(root)
port_var.set(port_options[0])  # Standardwert setzen

port_menu = tk.OptionMenu(root, port_var, *port_options)
port_menu.grid(row=1, column=1, padx=10, pady=10)

# Scan Button
scan_button = tk.Button(root, text="Scan starten", command=lambda: start_scan(result_text, status_label))
scan_button.grid(row=2, column=0, columnspan=2, pady=20)

# Ergebnisfenster
result_text = scrolledtext.ScrolledText(root, width=50, height=20)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Statuslabel
status_label = tk.Label(root, text="Bereit", fg="green")
status_label.grid(row=4, column=0, columnspan=2, pady=10)

# GUI starten
root.mainloop()
