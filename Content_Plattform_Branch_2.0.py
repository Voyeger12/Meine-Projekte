import sys
import csv
import os
import textwrap
from colorama import Fore, Back, init
init(autoreset=True)

# Optional: Konsole aufräumen (funktioniert in Windows & Unix)
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# CSV-Datei einlesen
with open("data.csv", newline='', encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    data = list(reader)

header = data[0]
content = data[1]

# Begrüßung
print("\n" + "-" * 70 + "\n")
print(f"{Fore.RED}Willkommen zum IT News Netzwerk. Die Frischesten News nur für dich! ")
print("\n" + "-" * 70 + "\n")
print()

name = input("Bitte gib einen Nutzernamen ein: ").upper()
sys.stdout.write("\033[F")
sys.stdout.write("\033[K")
sys.stdout.flush()

def print_box(text, width=40):
    print(Fore.GREEN + Back.WHITE + "╔" + "═" * (width - 2) + "╗")
    print(Fore.GREEN + Back.WHITE + "║" + Fore.RED + f"{text:^{width - 3}}" + Fore.GREEN + "║")
    print(Fore.GREEN + Back.WHITE + "╚" + "═" * (width - 2) + "╝")

# Neue Funktion: News-Box
def print_news_card(titel, text, width=50):
    wrapped_text = textwrap.wrap(text, width - 4)
    print("╔" + "═" * (width - 2) + "╗")
    print(f"║ {titel.center(width - 5)} ║")
    print("╠" + "═" * (width - 2) + "╣")
    for zeile in wrapped_text:
        print(f"║ {zeile.ljust(width - 4)} ║")
    print("╚" + "═" * (width - 2) + "╝")

print_box(f"👋 Willkommen, {name}!")

# Altersabfrage mit Fehlerprüfung
while True:
    alter_eingabe = input("Wie alt bist du?: ")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.flush()

    try:
        alter = int(alter_eingabe)
        if 10 <= alter <= 100:
            break
        else:
            print("Bitte gib ein richtiges Alter ein.")
    except ValueError:
        print("⚠️ Ungültige Eingabe! Bitte gib dein Alter als Zahl ein.")

print("\n" + "-" * 40 + "\n")

if alter >= 18:
    print(f"✅ Du bist volljährig, {name}. Du bist {alter} Jahre alt. Viel Spaß mit unserem Content!\n")

    while True:
        clear_screen()  # Bildschirm aufräumen für bessere Übersicht

        # Menü anzeigen
        print("-" * 40)
        print(f"📺 Willkommen {name} bei IT News Media – deiner Content-Plattform!\n")
        print("Bitte suche dir jetzt deinen Content aus:\n")
        print("1️⃣  Gaming News 🎮")
        print("2️⃣  Technik News 🔧")
        print("3️⃣  KI News 🤖")
        print("-" * 40)

        auswahl = input("Wähle deinen Content mit der Ziffer 1, 2 oder 3: ").strip()

        if auswahl not in ["1", "2", "3"]:
            print("⚠️ Ungültige Auswahl. Bitte gib 1, 2 oder 3 ein.")
            input("Drücke Enter, um es nochmal zu versuchen ...")
            continue  # Zurück zur Menüanzeige

        # Gültige Auswahl
        index = int(auswahl) - 1
        news_typ = header[index]
        news_content = content[index]

        clear_screen()
        print("\n" + "-" * 40)
        print(f"Du hast {news_typ} gewählt!")
        print(f"Eine gute Auswahl, {name}! Hier sind die neuesten News:")
        print("-" * 40 + "\n")

        print_news_card(news_typ.upper(), news_content)

        print("\n" + "-" * 40)

        # Rückfrage: Zurück zum Menü?
        while True:
            weiter = input("🔁 Möchtest du zurück zum Menü? (j/n): ").strip().lower()
            if weiter == "j":
                break  # Menü erneut anzeigen
            elif weiter == "n":
                print("\n" + "-" * 40)
                print(f"\n👋 Danke fürs Reinschauen, {name}! Bis zum nächsten Mal!")
                print("\n" + "-" * 40)
                sys.exit()
            else:
                print("⚠️ Ungültige Eingabe. Bitte gib 'j' oder 'n' ein.")
else:
    print(f"⛔ Du bist nicht volljährig, {name}. Du bist {alter} Jahre alt. Content gesperrt.")
    sys.exit()
