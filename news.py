import sqlite3
import sys
import os
import pwinput

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

print("\n" + "-" * 70 + "\n")
print("Willkommen zum IT News Netzwerk. Die Frischesten News nur für dich!")
print("\n" + "-" * 70 + "\n")

name = input("Bitte logge dich ein. Gib dazu jetzt deinen Nutzernamen ein: ").lower()
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")
sys.stdout.flush()

nachricht = "geheim"

while True:
    passwort = pwinput.pwinput(prompt="Bitte gebe das Passwort ein 🔐: ", mask="*").lower()
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.flush()

    if passwort == nachricht:
        break
    else:
        print("❌ Falsches Passwort. Versuch es nochmal.")

print("✅ Passwort korrekt! Willkommen.")
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")
sys.stdout.flush()

# Verbindung zur Datenbank herstellen
connection = sqlite3.connect("nachrichten.db")
cursor = connection.cursor()

# Tabellen (nur zum Testen - kann später raus)
cursor.execute("DROP TABLE IF EXISTS kategorien")
cursor.execute("DROP TABLE IF EXISTS nachrichten")

cursor.execute("""
CREATE TABLE IF NOT EXISTS kategorien(
    k_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS nachrichten(
    n_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nachricht TEXT,
    kategorie_id INTEGER,
    FOREIGN KEY(kategorie_id) REFERENCES kategorien(k_id)
)
""")

kategorien = ["Gaming News", "Technik News", "KI News"]
for kat in kategorien:
    cursor.execute("INSERT OR IGNORE INTO kategorien (name) VALUES (?)", (kat,))

nachrichten = [
    ("Clair obscur ist mega klasse und sieht hammer aus.", "Gaming News"),
    ("Nvidia ist ein scammer.", "Technik News"),
    ("Sql lernen ist spaßig!", "KI News"),
    ("Pax Dei Überarbeitet sein Kampfsystem!", "Gaming News"),
]

for text, kat_name in nachrichten:
    cursor.execute("SELECT k_id FROM kategorien WHERE name = ?", (kat_name,))
    k_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO nachrichten (nachricht, kategorie_id) VALUES (?, ?)", (text, k_id))

connection.commit()

# Kategorien aus DB laden
cursor.execute("SELECT k_id, name FROM kategorien")
kategorien_liste = cursor.fetchall()

# Menü-Schleife für Kategorie-Auswahl
while True:
    clear_screen()  # Bildschirm löschen vor Menü-Anzeige

    print("\nWähle eine Nachrichten Kategorie aus die dich Interessiert:")
    print("\n" + "-" * 70 + "\n")
    for k_id, kat_name in kategorien_liste:
        print(f"{k_id}: {kat_name}")
    print("\n" + "-" * 70 + "\n")

    print("\nDrücke 'n' wenn du Genug Nachrichten Gelesen hast und das Progamm beenden willst:")
    print()
    auswahl = input("Was Interessiert dich heute was du lesen Möchtest?: ").strip()
    print()

    if auswahl.lower() == 'n':
        print()
        print(f"Danke das du dir unsere Nachrichten Angeschaut hast {name}. Bis zum Nächsten Mal!")
        print()
        break

    if not auswahl.isdigit():
        print("Bitte gib eine gültige Zahl ein.")
        input("Drücke Enter, um es nochmal zu versuchen...")
        continue

    k_id_auswahl = int(auswahl)
    if k_id_auswahl not in [k[0] for k in kategorien_liste]:
        print("Diese Kategorie gibt es nicht. Versuch es nochmal.")
        input("Drücke Enter, um es nochmal zu versuchen...")
        continue

    # Nachrichten zu gewählter Kategorie abrufen
    cursor.execute("""
    SELECT n_id, nachricht FROM nachrichten WHERE kategorie_id = ?
    """, (k_id_auswahl,))

    nachrichten_auswahl = cursor.fetchall()

    clear_screen()  # Bildschirm löschen vor Anzeige der Nachrichten

    if not nachrichten_auswahl:
        print("Keine Nachrichten in dieser Kategorie.")
    else:
        kat_name = [k[1] for k in kategorien_liste if k[0] == k_id_auswahl][0]
        print(f"\nhier sind deine Neuesten Nachrichten in der Kategorie {kat_name}!\n")
        for n_id, text in nachrichten_auswahl:
            print(f"[{n_id}] {text}")
            print("-" * 40)

    input("\nDrücke Enter, um zurück zum Menü zu gelangen...")

connection.close()
