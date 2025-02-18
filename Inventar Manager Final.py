import tkinter as tk
from tkinter import ttk, messagebox
import random
import pickle
import os
import customtkinter as ctk

# Modernes Design-System
DARK_THEME = {
    'bg': '#2E3440',
    'fg': '#D8DEE9',
    'accent': '#5E81AC',
    'secondary': '#3B4252',
    'success': '#A3BE8C',
    'warning': '#BF616A',
    'font': ('Segoe UI', 11)
}

RARITY_WEIGHTS = {
    "häufig": 1,
    "selten": 2,
    "sehr selten": 3
}

MODERN_ICONS = {
    'search': '🕵️',
    'add': '🆕',
    'delete': '❌',
    'save': '💾'
}

ITEMS = [
    {"name": "Konservendose", "type": "Essen", "rarity": "häufig", "description": "Eingemachtes Gemüse"},
    {"name": "Flasche Wasser", "type": "Trinken", "rarity": "häufig", "description": "0,5l Trinkwasser"},
    {"name": "Baseballschläger", "type": "Waffe", "rarity": "selten", "description": "Holzschläger mit Metallgriff"},
    {"name": "Taschenmesser", "type": "Waffe", "rarity": "sehr selten", "description": "Klappmesser mit 5 Klingen"},
    {"name": "Schrott", "type": "Schrott", "rarity": "häufig", "description": "Wertloser Metallabfall"},
    {"name": "Müsliriegel", "type": "Essen", "rarity": "häufig", "description": "Energieriegel mit Nüssen"},
    {"name": "Konservendose mit Reis", "type": "Essen", "rarity": "häufig", "description": "400g Basmatireis"},
    {"name": "Flasche grüner Tee", "type": "Trinken", "rarity": "häufig", "description": "500ml Bio-Tee"},
    {"name": "Katana", "type": "Waffe", "rarity": "selten", "description": "Japanisches Langschwert"},
    {"name": "Schwimmende Laterne", "type": "Deko", "rarity": "selten", "description": "Öllampe mit Schwimmfähigkeit"},
    {"name": "Faltbarer Regenschirm", "type": "Ausrüstung", "rarity": "häufig", "description": "Kompakter Regenschutz"},
    {"name": "Taschenlampe mit Handkurbel", "type": "Ausrüstung", "rarity": "häufig", "description": "Notstromversorgung"},
    {"name": "Instant Ramen", "type": "Essen", "rarity": "häufig", "description": "Schnellgericht mit Brühe"},
    {"name": "Schwämme aus Bambus", "type": "Haushalt", "rarity": "häufig", "description": "Natürliche Reinigungshilfen"},
    {"name": "Teebeutel aus grünem Tee", "type": "Trinken", "rarity": "häufig", "description": "Aromatischer Aufguss"},
    {"name": "Bastelschere", "type": "Werkzeug", "rarity": "häufig", "description": "Präzisionsschere"},
    {"name": "Taktischer Baseballschläger", "type": "Waffe", "rarity": "selten", "description": "Verstärkte Aluminiumversion"},
    {"name": "Bento-Box", "type": "Essen", "rarity": "häufig", "description": "Japanische Lunchbox"},
    {"name": "Yukata", "type": "Kleidung", "rarity": "selten", "description": "Leichter Baumwollkimono"},
    {"name": "Batteriebetriebener Ventilator", "type": "Ausrüstung", "rarity": "selten", "description": "Tragbare Kühlung"},
    {"name": "Tausend Kranich-Faltpapier", "type": "Deko", "rarity": "selten", "description": "Glücksbringer aus Papier"},
    {"name": "Echtes Miso", "type": "Essen", "rarity": "häufig", "description": "Fermentierte Sojapaste"},
    {"name": "Tanzender Daruma", "type": "Deko", "rarity": "häufig", "description": "Symbol für Durchhaltevermögen"},
    {"name": "Kaiten Sushi-Maschine", "type": "Maschine", "rarity": "sehr selten", "description": "Automatisierte Zubereitung"},
    {"name": "Seil aus Reisstroh", "type": "Werkzeug", "rarity": "selten", "description": "Reißfeste Naturfaser"},
    {"name": "Bambusfächer", "type": "Ausrüstung", "rarity": "häufig", "description": "Handgefertigter Luftsprudler"},
    {"name": "Kochmesser aus Kyoto", "type": "Werkzeug", "rarity": "sehr selten", "description": "Hochwertiger Schneidehelfer"},
    {"name": "Schwimmring in Form eines Karpfens", "type": "Ausrüstung", "rarity": "selten", "description": "Spielzeug für Erwachsene"},
    {"name": "Vorrat Reiswein", "type": "Trinken", "rarity": "selten", "description": "Süßer Alkohol aus Reis"},
    {"name": "Fischernetze", "type": "Ausrüstung", "rarity": "häufig", "description": "Robustes Fangwerkzeug"},
    {"name": "Schuluniform", "type": "Kleidung", "rarity": "häufig", "description": "Traditionelle Schülertracht"},
    {"name": "Lange Robe aus Kimono-Stoff", "type": "Kleidung", "rarity": "selten", "description": "Formelle Abendgarderobe"},
    {"name": "Tanzmaske aus Holz", "type": "Deko", "rarity": "selten", "description": "Traditionelles Theateraccessoire"},
    {"name": "Sake-Set", "type": "Trinken", "rarity": "selten", "description": "Keramikflasche mit Bechern"},
    {"name": "Kochbuch für traditionelle japanische Küche", "type": "Buch", "rarity": "selten", "description": "Über 100 Rezepte"},
    {"name": "Lange Bambusstangen", "type": "Werkzeug", "rarity": "häufig", "description": "Vielseitiges Baumaterial"},
    {"name": "Erdbebenradio", "type": "Ausrüstung", "rarity": "selten", "description": "Notfallkommunikation"},
    {"name": "Noh Maske", "type": "Deko", "rarity": "sehr selten", "description": "Antikes Theaterrequisit"},
    {"name": "Himawari Samen", "type": "Pflanze", "rarity": "häufig", "description": "Sonnenblumensamen"},
    {"name": "Bambus-Kochgeschirr", "type": "Haushalt", "rarity": "häufig", "description": "Feuerfeste Küchenutensilien"},
    {"name": "Yaki Imo", "type": "Essen", "rarity": "häufig", "description": "Gebackene Süßkartoffel"},
    {"name": "Schlüsselanhänger in Form eines Maneki-Neko", "type": "Deko", "rarity": "häufig", "description": "Glückskatze"},
    {"name": "Bento-Box mit Motiven aus Anime", "type": "Essen", "rarity": "selten", "description": "Künstlerisch gestaltet"},
    {"name": "Kräuterteeset mit Kamille", "type": "Trinken", "rarity": "häufig", "description": "Beruhigende Mischung"},
    {"name": "Tasche mit Kawaii-Stickerei", "type": "Kleidung", "rarity": "häufig", "description": "Niedliches Accessoire"},
    {"name": "Reisstrohmatte", "type": "Haushalt", "rarity": "häufig", "description": "Natürlicher Bodenbelag"},
    {"name": "Shōji-Schiebetür", "type": "Möbel", "rarity": "selten", "description": "Traditioneller Raumteiler"},
    {"name": "Sushimesser", "type": "Werkzeug", "rarity": "sehr selten", "description": "Präzisionsklinge für Fisch"},
    {"name": "Furoshiki-Tuch", "type": "Kleidung", "rarity": "häufig", "description": "Vielseitiges Verpackungstuch"},
    {"name": "Traditionelle Holz-Teekanne", "type": "Haushalt", "rarity": "selten", "description": "Handgeschnitztes Unikat"},
    {"name": "Japanischer Keramikbecher", "type": "Haushalt", "rarity": "häufig", "description": "Einfache Trinkschale"},
    {"name": "Koi-Karpfen Modell", "type": "Deko", "rarity": "selten", "description": "Symbol für Stärke und Glück"},
    {"name": "Dango-Spieße", "type": "Essen", "rarity": "häufig", "description": "Süße Reisknödel am Stiel"},
    {"name": "Yumi-Notbogen", "type": "Waffe", "rarity": "selten", "description": "Traditioneller Bambusbogen mit improvisierten Pfeilen"},
    {"name": "Kama-Sichel", "type": "Waffe", "rarity": "häufig", "description": "Landwirtschaftswerkzeug als Nahkampfwaffe"},
    {"name": "Concrete-Reinforcement-Stab", "type": "Waffe", "rarity": "häufig", "description": "Stahlstab aus Trümmern geschliffen"},
    {"name": "Feuerlöscher-Sprenggranate", "type": "Waffe", "rarity": "sehr selten", "description": "Modifizierter Löscher mit Nagelfüllung"},
    {"name": "Miso-Paste-Tuben", "type": "Essen", "rarity": "häufig", "description": "Haltbare Fermentierte Sojapaste"},
    {"name": "7-Eleven-Dorayaki", "type": "Essen", "rarity": "selten", "description": "Eingeschweißte Süßigkeiten mit langer Haltbarkeit"},
    {"name": "Sake-Miniflaschen", "type": "Trinken", "rarity": "selten", "description": "20ml Notrationen aus Automaten"},
    {"name": "Instanthochleistungs-Ramen", "type": "Essen", "rarity": "häufig", "description": "5000kcal Pro Portion"},
    {"name": "Kampfer-Öl-Fläschchen", "type": "Medizin", "rarity": "häufig", "description": "Traditionelles Desinfektionsmittel"},
    {"name": "Verbandsmaterial-Tatami", "type": "Medizin", "rarity": "selten", "description": "Reißfeste Reisstrohbinden"},
    {"name": "Fukushima-Jodtabletten", "type": "Medizin", "rarity": "sehr selten", "description": "Anti-Strahlungs-Prophylaxe"},
    {"name": "Onsen-Mineraliensalz", "type": "Medizin", "rarity": "häufig", "description": "Elektrolytersatz aus Thermalquellen"},
    {"name": "Shōji-Sperrholzplatten", "type": "Möbel", "rarity": "häufig", "description": "Wiederverwertete Raumteiler als Baumaterial"},
    {"name": "Vending-Machine-Tür", "type": "Deko", "rarity": "selten", "description": "Stahlschild aus Automatenresten"},
    {"name": "Tatami-Fluchtleiter", "type": "Möbel", "rarity": "selten", "description": "Reisstrohmatten zu Seilen verflochten"},
    {"name": "Karaoke-Mikrofon-Distresscaller", "type": "Ausrüstung", "rarity": "selten", "description": "Modifizierter Megaphon-Sender"},
    {"name": "Pachinko-Kugeln", "type": "Werkzeug", "rarity": "häufig", "description": "Metallkugeln für Schleudern/Tauschhandel"},
    {"name": "Koban-Handpresse", "type": "Werkzeug", "rarity": "sehr selten", "description": "Münzprägewerkzeug für Tauschsysteme"},
    {"name": "Kairo-Wärmepads", "type": "Ausrüstung", "rarity": "häufig", "description": "Einweg-Handwärmer aus Convenience Stores"},
    {"name": "Shinkansen-Federstahl", "type": "Material", "rarity": "sehr selten", "description": "Hochwertiger Stahl aus Zugwracks"},
    {"name": "Robot-Restaurant-Batterien", "type": "Material", "rarity": "selten", "description": "Leistungsstarke 12V-Akkus"},
    {"name": "Tsunami-Flutboje", "type": "Ausrüstung", "rarity": "sehr selten", "description": "Wasserdichter Notfallbehälter"},
    {"name": "Pocari-Sweat-Pulver", "type": "Trinken", "rarity": "selten", "description": "Elektrolytpulver in Alutütchen"},
    {"name": "Yakitori-Spießbündel", "type": "Essen", "rarity": "häufig", "description": "Rostfreie Metallspieße"},
    {"name": "Karaoke-Laserdiskus", "type": "Material", "rarity": "häufig", "description": "Spiegelnde Scheiben für Signalreflexion"},
    {"name": "Konservendose", "type": "Essen", "rarity": "häufig", "description": "Eingemachtes Gemüse"},
    {"name": "Flasche Wasser", "type": "Trinken", "rarity": "häufig", "description": "0,5l Trinkwasser"},
    {"name": "Baseballschläger", "type": "Waffe", "rarity": "selten", "description": "Holzschläger mit Metallgriff"},
    {"name": "Hammer", "type": "Werkzeug", "rarity": "häufig", "description": "Standard-Werkzeug mit Stahlkopf"},
    {"name": "Schraubendreher-Set", "type": "Werkzeug", "rarity": "häufig", "description": "Verschiedene Spitz- und Kreuzschliffen"},
    {"name": "Staubsauger", "type": "Haushalt", "rarity": "häufig", "description": "Elektrischer Reinigungsapparat"},
    {"name": "Bettlaken", "type": "Haushalt", "rarity": "häufig", "description": "Baumwollbettwäsche 140x200cm"},
    {"name": "Feuerzeug", "type": "Ausrüstung", "rarity": "häufig", "description": "Einweg-Feuerzeug mit Butangas"},
    {"name": "Taschenlampe", "type": "Ausrüstung", "rarity": "häufig", "description": "LED-Lampe mit Batterien"},
    {"name": "Erste-Hilfe-Kasten", "type": "Medizin", "rarity": "selten", "description": "Grundausstattung für Notfälle"},
    {"name": "Bügeleisen", "type": "Haushalt", "rarity": "häufig", "description": "Dampfbügeleisen mit Temperaturregler"},
    {"name": "Kabelrolle", "type": "Werkzeug", "rarity": "häufig", "description": "10m Verlängerungskabel mit Mehrfachstecker"},
    {"name": "Regenschirm", "type": "Ausrüstung", "rarity": "häufig", "description": "Klappbarer Wetterschutz"},
    {"name": "Küchenmesser", "type": "Werkzeug", "rarity": "häufig", "description": "20cm Kochklinge aus rostfreiem Stahl"},
    {"name": "Schraubzwinge", "type": "Werkzeug", "rarity": "selten", "description": "Holz- und Metallbearbeitungshilfe"},
    {"name": "Bohrmaschine", "type": "Werkzeug", "rarity": "selten", "description": "Akku-Bohrschrauber mit Bitsatz"},
    {"name": "Klebeband", "type": "Werkzeug", "rarity": "häufig", "description": "Universelle Klebelösung 50m"},
    {"name": "Schweizer Taschenmesser", "type": "Werkzeug", "rarity": "selten", "description": "Multifunktionswerkzeug mit 15 Klingen"},
    {"name": "Campingkocher", "type": "Ausrüstung", "rarity": "selten", "description": "Tragbares Gaskochersystem"},
    {"name": "Zelt", "type": "Ausrüstung", "rarity": "selten", "description": "3-Personen-Domzelt mit Heringen"},
    {"name": "Schlafsack", "type": "Ausrüstung", "rarity": "häufig", "description": "Komfortbereich -5°C bis +10°C"},
    {"name": "Wasserfilter", "type": "Ausrüstung", "rarity": "selten", "description": "Tragbare Entkeimungsanlage"},
    {"name": "Fahrradschlauch", "type": "Ausrüstung", "rarity": "häufig", "description": "28 Zoll Ersatzschlauch mit Flickset"},
    {"name": "Luftpumpe", "type": "Ausrüstung", "rarity": "häufig", "description": "Manuelle Doppelventil-Pumpe"},
    {"name": "Werkzeugkasten", "type": "Werkzeug", "rarity": "häufig", "description": "Grundausstattung mit 35 Teilen"},
    {"name": "Mehl", "type": "Essen", "rarity": "häufig", "description": "1kg Weizenmehl Type 405"},
    {"name": "Zucker", "type": "Essen", "rarity": "häufig", "description": "1kg Haushaltszucker"},
    {"name": "Salz", "type": "Essen", "rarity": "häufig", "description": "Jodiertes Speisesalz 500g"},
    {"name": "Nudeln", "type": "Essen", "rarity": "häufig", "description": "500g Spaghetti aus Hartweizen"},
    {"name": "Reis", "type": "Essen", "rarity": "häufig", "description": "1kg Langkornreis"},
    {"name": "Öl", "type": "Essen", "rarity": "häufig", "description": "1l Sonnenblumenöl"},
    {"name": "Konservenbüchse", "type": "Essen", "rarity": "häufig", "description": "400g Maiskolben in Lake"},
    {"name": "Dosenöffner", "type": "Werkzeug", "rarity": "häufig", "description": "Manuelles Öffnungsgerät"},
    {"name": "Plastikbox", "type": "Haushalt", "rarity": "häufig", "description": "20l Aufbewahrungsbehälter"},
    {"name": "Klebepistole", "type": "Werkzeug", "rarity": "selten", "description": "Elektrischer Heißkleberapparat"},
    {"name": "Stahldraht", "type": "Material", "rarity": "häufig", "description": "1mm starker Federstahl 10m"},
    {"name": "Schrauben", "type": "Material", "rarity": "häufig", "description": "Mischpackung 100 Stück 4-6mm"},
    {"name": "Holzbretter", "type": "Material", "rarity": "häufig", "description": "Kiefernholz 200x30x2cm"},
    {"name": "Metallrohre", "type": "Material", "rarity": "selten", "description": "Aluminiumrohre 1m Länge"},
    {"name": "Isolierband", "type": "Werkzeug", "rarity": "häufig", "description": "Elektrotechnisches Abschlussband"},
    {"name": "Feile", "type": "Werkzeug", "rarity": "häufig", "description": "Meißel Feinkorn 200mm"},
    {"name": "Schleifpapier", "type": "Werkzeug", "rarity": "häufig", "description": "Korn 80-240 Mischpackung"},
    {"name": "Schutzbrille", "type": "Ausrüstung", "rarity": "häufig", "description": "Transparente Arbeitsbrille"},
    {"name": "Gehörschutz", "type": "Ausrüstung", "rarity": "häufig", "description": "Kapselgehörschutz 27dB Dämpfung"},
    {"name": "Atemschutzmaske", "type": "Ausrüstung", "rarity": "häufig", "description": "FFP2 Partikelfilter"},
    {"name": "Arbeitshandschuhe", "type": "Ausrüstung", "rarity": "häufig", "description": "Lederhandschuhe Größe L"},
    {"name": "Stichsäge", "type": "Werkzeug", "rarity": "selten", "description": "Elektrische Kurzhub-Säge"},
    {"name": "Winkelschleifer", "type": "Werkzeug", "rarity": "selten", "description": "125mm Schleif- und Trennscheibe"},
    {"name": "Benzinkanister", "type": "Ausrüstung", "rarity": "selten", "description": "20l Kraftstoffbehälter"},
    {"name": "Stromgenerator", "type": "Ausrüstung", "rarity": "sehr selten", "description": "2kW Benzingenerator"},
    {"name": "Solarladegerät", "type": "Ausrüstung", "rarity": "selten", "description": "20W faltbares Solarpanel"},
    {"name": "Taschenwärmer", "type": "Ausrüstung", "rarity": "häufig", "description": "Einweg-Handwärmer 8h"},
    {"name": "Signalpistole", "type": "Waffe", "rarity": "sehr selten", "description": "Notfall-Leuchtmunition"},
    {"name": "Schutzweste", "type": "Ausrüstung", "rarity": "sehr selten", "description": "Stichfeste Schutzklasse IIIa"},
    {"name": "Nachtvisionsgerät", "type": "Ausrüstung", "rarity": "sehr selten", "description": "Digital Night Vision 4x"},
    {"name": "Wasserkanister", "type": "Ausrüstung", "rarity": "häufig", "description": "10l faltbarer Behälter"},
    {"name": "Gaskocher", "type": "Ausrüstung", "rarity": "selten", "description": "Tragbares Kochsystem"},
    {"name": "Kompass", "type": "Ausrüstung", "rarity": "häufig", "description": "Magnetischer Taschenkompass"},
    {"name": "Landkarte", "type": "Ausrüstung", "rarity": "häufig", "description": "Topographische Karte 1:50.000"},
    {"name": "Fernglas", "type": "Ausrüstung", "rarity": "selten", "description": "10x42 Vergütete Optik"},
    {"name": "Feuerlöscher", "type": "Ausrüstung", "rarity": "häufig", "description": "6kg ABC-Pulverlöscher"},
    {"name": "Notfallradio", "type": "Ausrüstung", "rarity": "selten", "description": "Kurbelbetriebenes UKW-Gerät"},
    {"name": "Alufolie", "type": "Haushalt", "rarity": "häufig", "description": "30cm breite Rolle"},
    {"name": "Frischhaltefolie", "type": "Haushalt", "rarity": "häufig", "description": "30m Lebensmittelverpackung"},
    {"name": "Müllbeutel", "type": "Haushalt", "rarity": "häufig", "description": "120l Reißfestigkeit"},
    {"name": "Wischmopp", "type": "Haushalt", "rarity": "häufig", "description": "Teleskopstiel mit Wechselkopf"},
    {"name": "Eimer", "type": "Haushalt", "rarity": "häufig", "description": "12l Kunststoffbehälter"},
    {"name": "Schrubber", "type": "Haushalt", "rarity": "häufig", "description": "Bodenreinigungsbürste"},
    {"name": "Scheuerpulver", "type": "Haushalt", "rarity": "häufig", "description": "500g Reinigungspulver"},
    {"name": "Spülmittel", "type": "Haushalt", "rarity": "häufig", "description": "750ml Konzentrat"},
    {"name": "Waschmittel", "type": "Haushalt", "rarity": "häufig", "description": "3kg Vollwaschmittel"},
    {"name": "Weichspüler", "type": "Haushalt", "rarity": "häufig", "description": "1,5l Flasche"},
    {"name": "Handdesinfektionsmittel", "type": "Medizin", "rarity": "häufig", "description": "70% Alkoholgel 500ml"},
    {"name": "Schmerztabletten", "type": "Medizin", "rarity": "häufig", "description": "Ibuprofen 400mg 20 Stück"},
    {"name": "Pflaster", "type": "Medizin", "rarity": "häufig", "description": "Wundauflagen in verschiedenen Größen"},
    {"name": "Verbandsmaterial", "type": "Medizin", "rarity": "häufig", "description": "Sterile Kompressen und Binden"},
    {"name": "Thermometer", "type": "Medizin", "rarity": "häufig", "description": "Digitales Fiebermessgerät"},
    {"name": "Pinzette", "type": "Medizin", "rarity": "häufig", "description": "Chirurgische Edelstahlpinzette"},
    {"name": "Schere", "type": "Medizin", "rarity": "häufig", "description": "Medizinische Stumpfschere"},
    {"name": "Decke", "type": "Haushalt", "rarity": "häufig", "description": "Wollmischgewebe 140x200cm"},
    {"name": "Kissen", "type": "Haushalt", "rarity": "häufig", "description": "40x80cm Federkernkissen"},
    {"name": "Handtücher", "type": "Haushalt", "rarity": "häufig", "description": "Baumwollhandtuch 50x100cm"},
    {"name": "Bademantel", "type": "Kleidung", "rarity": "häufig", "description": "Frotteestoff Größe L"},
    {"name": "Hausschuhe", "type": "Kleidung", "rarity": "häufig", "description": "Filzpuschen Größe 42"},
    {"name": "Regenjacke", "type": "Kleidung", "rarity": "häufig", "description": "Wasserdichte Outdoorjacke"},
    {"name": "Wanderstiefel", "type": "Kleidung", "rarity": "selten", "description": "Gore-Tex Membran Größe 44"},
    {"name": "Rucksack", "type": "Ausrüstung", "rarity": "häufig", "description": "30l Trekkingrucksack"},
    {"name": "Gürteltasche", "type": "Ausrüstung", "rarity": "häufig", "description": "Kleine Bauchtasche mit Reißverschluss"},
    {"name": "Geldbeutel", "type": "Ausrüstung", "rarity": "häufig", "description": "RFID-geschützte Kreditkartenhalter"},
    {"name": "Taschenmesser", "type": "Werkzeug", "rarity": "häufig", "description": "Klappmesser mit 3 Klingen"},
    {"name": "Multifunktionswerkzeug", "type": "Werkzeug", "rarity": "selten", "description": "14-in-1 Outdoor-Tool"},
    {"name": "Angelhaken", "type": "Werkzeug", "rarity": "häufig", "description": "Fischerbedarf Set mit 50 Haken"},
    {"name": "Fischköder", "type": "Werkzeug", "rarity": "häufig", "description": "Künstliche Würmer und Blinker"},
    {"name": "Zeltplane", "type": "Ausrüstung", "rarity": "selten", "description": "Wasserfeste Nylonplane 3x4m"},
    {"name": "Heringe", "type": "Ausrüstung", "rarity": "häufig", "description": "Zeltbefestigungs-Set aus Alu"},
    {"name": "Seil", "type": "Ausrüstung", "rarity": "häufig", "description": "Statisches Kletterseil 10m"},
    {"name": "Karabinerhaken", "type": "Ausrüstung", "rarity": "häufig", "description": "Alpinqualität 25kN Bruchlast"},
    {"name": "Trekkingstock", "type": "Ausrüstung", "rarity": "häufig", "description": "Teleskopierbarer Wanderstab"},
    {"name": "GPS-Gerät", "type": "Ausrüstung", "rarity": "sehr selten", "description": "Wander-GPS mit Topo-Karten"},
    {"name": "Powerbank", "type": "Ausrüstung", "rarity": "häufig", "description": "20000mAh USB-C Ladestation"},
    {"name": "Kabelbinder", "type": "Werkzeug", "rarity": "häufig", "description": "100 Stück 20cm Nylonbinder"},
    {"name": "Duct Tape", "type": "Werkzeug", "rarity": "häufig", "description": "Universalklebeband 50m"},
    {"name": "Schweißgerät", "type": "Werkzeug", "rarity": "sehr selten", "description": "MMA Schweißinverter 200A"},
    {"name": "Schweißmaske", "type": "Ausrüstung", "rarity": "selten", "description": "Automatische Verdunkelung"},
    {"name": "Schweißdraht", "type": "Material", "rarity": "häufig", "description": "1kg Elektroden 2,5mm"},
    {"name": "Gießkanne", "type": "Haushalt", "rarity": "häufig", "description": "5l Kunststoffkanne"},
    {"name": "Gartenschlauch", "type": "Haushalt", "rarity": "häufig", "description": "15m PVC-Schlauch mit Adapter"},
    {"name": "Rasensprenger", "type": "Haushalt", "rarity": "häufig", "description": "Oszillierender Gartenregner"},
    {"name": "Gartenschere", "type": "Werkzeug", "rarity": "häufig", "description": "Bypass-Schere für Äste"},
    {"name": "Spaten", "type": "Werkzeug", "rarity": "häufig", "description": "Grabewerkzeug mit Holzstiel"},
    {"name": "Schaufel", "type": "Werkzeug", "rarity": "häufig", "description": "Klappbare Expeditionsschaufel"},
    {"name": "Axt", "type": "Werkzeug", "rarity": "selten", "description": "Waldarbeiteraxt mit Faserstiel"},
    {"name": "Beil", "type": "Werkzeug", "rarity": "selten", "description": "Kompakte Camping-Handbeil"},
    {"name": "Motorsäge", "type": "Werkzeug", "rarity": "sehr selten", "description": "Benzinbetriebene Kettensäge"},
    {"name": "Rasentrimmer", "type": "Werkzeug", "rarity": "selten", "description": "Elektrischer Grasschneider"},
    {"name": "Heckenschere", "type": "Werkzeug", "rarity": "selten", "description": "Akku-Heckenschneider 45cm"},
    {"name": "Laubbläser", "type": "Werkzeug", "rarity": "selten", "description": "Elektro-Laubgebläse 300km/h"},
    {"name": "Schneeschieber", "type": "Werkzeug", "rarity": "häufig", "description": "Aluschaufel 60cm Breite"},
    {"name": "Eispickel", "type": "Werkzeug", "rarity": "selten", "description": "Alpin-Ausrüstung für Eis"},
    {"name": "Schneeketten", "type": "Ausrüstung", "rarity": "selten", "description": "Auto-Schneeketten Set"},
    {"name": "Warnweste", "type": "Ausrüstung", "rarity": "häufig", "description": "Neongelbe Sicherheitsweste"},
    {"name": "Warndreieck", "type": "Ausrüstung", "rarity": "häufig", "description": "Zusammenklappbares Verkehrszeichen"},
    {"name": "Verbandskasten", "type": "Medizin", "rarity": "häufig", "description": "DIN 13164 zertifiziert"},
    {"name": "Feuerlöschdecke", "type": "Ausrüstung", "rarity": "häufig", "description": "1,5x1,5m Flammschutzdecke"},
    {"name": "Rauchmelder", "type": "Ausrüstung", "rarity": "häufig", "description": "10-Jahres-Batteriebetrieb"},
    {"name": "Kohlenmonoxidmelder", "type": "Ausrüstung", "rarity": "häufig", "description": "Digitale CO-Warnung"},
    {"name": "Gassensor", "type": "Ausrüstung", "rarity": "selten", "description": "Explosionsgas-Warngerät"},
    {"name": "Atemschutzfilter", "type": "Ausrüstung", "rarity": "selten", "description": "ABEK1 P3 Kombinationsfilter"},
    {"name": "Straßenkarte", "type": "Ausrüstung", "rarity": "häufig", "description": "Aktuelle Autoatlas-Version"},
    {"name": "Werkstatthandbuch", "type": "Buch", "rarity": "häufig", "description": "Reparaturanleitung für Fahrzeuge"},
    {"name": "Brecheisen", "type": "Werkzeug", "rarity": "selten", "description": "1m Stahlhebel mit Spitze"},
    {"name": "Bolzenschneider", "type": "Werkzeug", "rarity": "selten", "description": "42cm Schneidkopfdurchmesser"},
    {"name": "Rohrzange", "type": "Werkzeug", "rarity": "häufig", "description": "Verstellbare Wasserpumpenzange"},
    {"name": "Schlüsselsatz", "type": "Werkzeug", "rarity": "häufig", "description": "32-teiliger Bitsatz"},
    {"name": "Steckschlüssel", "type": "Werkzeug", "rarity": "häufig", "description": "1/2 Zoll Antrieb mit Nüssen"},
    {"name": "Drehmomentschlüssel", "type": "Werkzeug", "rarity": "selten", "description": "40-200Nm Einstellbereich"},
    {"name": "Fettpresse", "type": "Werkzeug", "rarity": "häufig", "description": "Handbetriebene Schmierfettpumpe"},
    {"name": "Ölkanne", "type": "Werkzeug", "rarity": "häufig", "description": "1l Metallkanne mit Auslauf"},
    {"name": "Bremsenreiniger", "type": "Material", "rarity": "häufig", "description": "500ml Sprühdose"},
    {"name": "WD-40", "type": "Material", "rarity": "häufig", "description": "400ml Rostlöser und Schmiermittel"},
    {"name": "Kriechöl", "type": "Material", "rarity": "häufig", "description": "Penetrierendes Öl 250ml"},
    {"name": "Schweißschutzcreme", "type": "Material", "rarity": "häufig", "description": "Hautschutz für Metallarbeiten"},
    {"name": "Arbeitslampe", "type": "Werkzeug", "rarity": "häufig", "description": "LED-Baustellenleuchte 50W"},
    {"name": "Strommessgerät", "type": "Werkzeug", "rarity": "selten", "description": "Digitales Multimeter"},
    {"name": "Kabeltrommel", "type": "Werkzeug", "rarity": "häufig", "description": "25m Verlängerungskabel"},
    {"name": "Stromadapter", "type": "Werkzeug", "rarity": "häufig", "description": "Internationale Steckdosenadapter"},
    {"name": "USB-Hub", "type": "Werkzeug", "rarity": "häufig", "description": "4-fach USB 3.0 Verlängerung"},
    {"name": "Externes Laufwerk", "type": "Werkzeug", "rarity": "selten", "description": "1TB SSD Festplatte"},
    {"name": "Datenkabel", "type": "Werkzeug", "rarity": "häufig", "description": "USB-C auf Lightning 2m"},
    {"name": "Netzteil", "type": "Werkzeug", "rarity": "häufig", "description": "Universalladegerät 65W"},
    {"name": "Lötkolben", "type": "Werkzeug", "rarity": "selten", "description": "60W Elektroniklötstation"},
    {"name": "Lötzinn", "type": "Material", "rarity": "häufig", "description": "Zinn-Blei-Legierung 0,8mm"},
    {"name": "Entlötpumpe", "type": "Werkzeug", "rarity": "häufig", "description": "Manuelle Saugpumpe für Lötzinn"},
    {"name": "Heißluftpistole", "type": "Werkzeug", "rarity": "selten", "description": "500°C Luftstrom für Schrumpfschläuche"},
    {"name": "Kabelmesser", "type": "Werkzeug", "rarity": "häufig", "description": "Isoliertes Abisolierwerkzeug"},
    {"name": "Kabelbinderpistole", "type": "Werkzeug", "rarity": "selten", "description": "Elektrische Kabelbindermontage"},
    {"name": "Klemmleiste", "type": "Werkzeug", "rarity": "häufig", "description": "12-polige Verteilerdose"},
    {"name": "Isolierband", "type": "Werkzeug", "rarity": "häufig", "description": "Vinyl-Elektroband schwarz"},
    {"name": "Kabelkanal", "type": "Werkzeug", "rarity": "häufig", "description": "PVC-Kabelkanal 40x40mm"},
    {"name": "Schrumpfschlauch", "type": "Werkzeug", "rarity": "häufig", "description": "3:1 Schrumpfverhältnis 10m"},
    {"name": "Steckverbinder", "type": "Werkzeug", "rarity": "häufig", "description": "Crimp-Stecker für Kabelenden"},
    {"name": "Netzwerkkabel", "type": "Werkzeug", "rarity": "häufig", "description": "Cat7 Ethernetkabel 10m"},
    {"name": "Switch", "type": "Werkzeug", "rarity": "selten", "description": "8-Port Gigabit Ethernet Switch"},
    {"name": "WLAN-Router", "type": "Werkzeug", "rarity": "selten", "description": "Dual-Band 1200Mbit/s"},
    {"name": "NAS-System", "type": "Werkzeug", "rarity": "sehr selten", "description": "4-Bay Netzwerkspeicher"},
    {"name": "Drucker", "type": "Werkzeug", "rarity": "selten", "description": "Multifunktions-Laserdrucker"},
    {"name": "Scanner", "type": "Werkzeug", "rarity": "selten", "description": "Dokumentscanner A4 Format"},
    {"name": "Batterieladegerät", "type": "Werkzeug", "rarity": "häufig", "description": "AA/AAA Akkuladegerät"},
    {"name": "Batterien", "type": "Werkzeug", "rarity": "häufig", "description": "AA Alkaline 12er Pack"},
    {"name": "Powerstation", "type": "Werkzeug", "rarity": "sehr selten", "description": "2000Wh Lithium-Speicher"},
    {"name": "Solarmodul", "type": "Werkzeug", "rarity": "sehr selten", "description": "300W faltbares Solarpanel"},
    {"name": "Wechselrichter", "type": "Werkzeug", "rarity": "selten", "description": "12V DC zu 230V AC 1000W"},
    {"name": "Tragbarer Kühlschrank", "type": "Werkzeug", "rarity": "sehr selten", "description": "12V/220V Kompressorkühler"},
    {"name": "Campingdusche", "type": "Ausrüstung", "rarity": "selten", "description": "Solarbetriebene Warmwasserdusche"},
    {"name": "Faltbare Badewanne", "type": "Ausrüstung", "rarity": "selten", "description": "Kompakte Campingwanne"},
    {"name": "Chemietoilette", "type": "Ausrüstung", "rarity": "selten", "description": "Tragbares Sanitärsystem"},
    {"name": "Desinfektionstabletten", "type": "Medizin", "rarity": "häufig", "description": "Wasseraufbereitungstabletten"},
    {"name": "Wasseraufbereiter", "type": "Ausrüstung", "rarity": "selten", "description": "Tragbarer UV-Filter"},
    {"name": "Kanister", "type": "Ausrüstung", "rarity": "häufig", "description": "20l Lebensmittelkanister"},
    {"name": "Wassersack", "type": "Ausrüstung", "rarity": "häufig", "description": "10l faltbarer Wasserbehälter"},
    {"name": "Wasserpumpe", "type": "Ausrüstung", "rarity": "selten", "description": "Handbetriebene Membranpumpe"},
    {"name": "Feldflasche", "type": "Ausrüstung", "rarity": "häufig", "description": "1l Aluminiumtrinkflasche"},
    {"name": "Isolierflasche", "type": "Ausrüstung", "rarity": "häufig", "description": "Thermosflasche 750ml"},
    {"name": "Campinggeschirr", "type": "Ausrüstung", "rarity": "häufig", "description": "Besteck und Teller-Set"},
    {"name": "Outdoor-Topfset", "type": "Ausrüstung", "rarity": "selten", "description": "3-teiliges Aluminium-Kochset"},
    {"name": "Grillrost", "type": "Ausrüstung", "rarity": "häufig", "description": "Eisenrost 40x30cm"},
    {"name": "Feuerstahl", "type": "Ausrüstung", "rarity": "häufig", "description": "Feuerstein mit Magnesiumstab"},
    {"name": "Zunder", "type": "Ausrüstung", "rarity": "häufig", "description": "Feueranzünder aus Baumwolle"},
    {"name": "Holzkohle", "type": "Ausrüstung", "rarity": "häufig", "description": "3kg Grillkohle Briketts"},
    {"name": "Feuerholz", "type": "Ausrüstung", "rarity": "häufig", "description": "Buchenholz 25cm Länge"},
    {"name": "Grillzange", "type": "Ausrüstung", "rarity": "häufig", "description": "30cm Edelstahlzange"},
    {"name": "Grillhandschuhe", "type": "Ausrüstung", "rarity": "häufig", "description": "Hitzebeständig bis 500°C"},
    {"name": "Grillbesteck", "type": "Ausrüstung", "rarity": "häufig", "description": "Edelstahl-Spaten und Gabel"},
    {"name": "Grillreiniger", "type": "Ausrüstung", "rarity": "häufig", "description": "Rostentferner Spray"},
    {"name": "Fleischthermometer", "type": "Ausrüstung", "rarity": "häufig", "description": "Digitales Einstichthermometer"},
    {"name": "Kühlakkus", "type": "Ausrüstung", "rarity": "häufig", "description": "4x 20x10cm Kühlelemente"},
    {"name": "Kühlbox", "type": "Ausrüstung", "rarity": "häufig", "description": "30l Kompressor-Kühlbox"},
    {"name": "Zeltreparaturset", "type": "Ausrüstung", "rarity": "häufig", "description": "Nadelset mit Nylonfaden"},
    {"name": "Schuhcreme", "type": "Haushalt", "rarity": "häufig", "description": "Schwarzes Schuhpflegemittel"},
    {"name": "Schuhspanner", "type": "Haushalt", "rarity": "häufig", "description": "Holzspanner Größe 42-46"},
    {"name": "Schuhputzzeug", "type": "Haushalt", "rarity": "häufig", "description": "Bürstenset mit Politur"},
    {"name": "Wachstuch", "type": "Haushalt", "rarity": "häufig", "description": "Tischdecke 150x250cm"},
    {"name": "Tischdecke", "type": "Haushalt", "rarity": "häufig", "description": "Bügelfreie Polyesterdecke"},
    {"name": "Servietten", "type": "Haushalt", "rarity": "häufig", "description": "Papierservietten 100 Stück"},
    {"name": "Besteckset", "type": "Haushalt", "rarity": "häufig", "description": "12-teiliges Edelstahlbesteck"},
    {"name": "Geschirrset", "type": "Haushalt", "rarity": "häufig", "description": "Porzellangeschirr für 6 Personen"},
    {"name": "Weingläser", "type": "Haushalt", "rarity": "häufig", "description": "6 Kristallgläser 400ml"},
    {"name": "Biergläser", "type": "Haushalt", "rarity": "häufig", "description": "6 Maßkrüge 500ml"},
    {"name": "Kaffeetassen", "type": "Haushalt", "rarity": "häufig", "description": "Keramiktassen 300ml"},
    {"name": "Kochlöffel", "type": "Haushalt", "rarity": "häufig", "description": "Holzlöffel-Set 3 Größen"},
    {"name": "Schneebesen", "type": "Haushalt", "rarity": "häufig", "description": "Edelstahlbesen 25cm"},
    {"name": "Pfannenwender", "type": "Haushalt", "rarity": "häufig", "description": "Silicone Pfannenheber"},
    {"name": "Dosenhalter", "type": "Haushalt", "rarity": "häufig", "description": "Universal-Dosenhalter für Öffner"},
    {"name": "Flaschenöffner", "type": "Haushalt", "rarity": "häufig", "description": "Magnetischer Kronkorkenöffner"},
    {"name": "Korkenzieher", "type": "Haushalt", "rarity": "häufig", "description": "Wellenkorkenzieher mit Messer"},
    {"name": "Küchenwaage", "type": "Haushalt", "rarity": "häufig", "description": "Digitale Waage 5kg"},
    {"name": "Messbecher", "type": "Haushalt", "rarity": "häufig", "description": "Plastikbecher mit Skala"},
    {"name": "Backform", "type": "Haushalt", "rarity": "häufig", "description": "Springform 26cm Durchmesser"},
    {"name": "Auflaufform", "type": "Haushalt", "rarity": "häufig", "description": "Keramikform 30x20cm"},
    {"name": "Backpapier", "type": "Haushalt", "rarity": "häufig", "description": "Antihaft-Backfolie 10m"},
    {"name": "Gewürzregal", "type": "Haushalt", "rarity": "häufig", "description": "Wandregal mit 12 Gläsern"},
    {"name": "Brotkasten", "type": "Haushalt", "rarity": "häufig", "description": "Holzkasten mit Belüftung"},
    {"name": "Obstschale", "type": "Haushalt", "rarity": "häufig", "description": "Glasobstschale 30cm Durchmesser"},
    {"name": "Salatschüssel", "type": "Haushalt", "rarity": "häufig", "description": "Keramikschüssel 25cm"},
    {"name": "Topflappen", "type": "Haushalt", "rarity": "häufig", "description": "Hitzebeständige Baumwolllappen"},
    {"name": "Backhandschuhe", "type": "Haushalt", "rarity": "häufig", "description": "Silicone Backhandschuhe"},
    {"name": "Schneidebrett", "type": "Haushalt", "rarity": "häufig", "description": "Bambusbrett 40x30cm"},
    {"name": "Gemüseschäler", "type": "Haushalt", "rarity": "häufig", "description": "Edelstahlschäler Y-förmig"},
    {"name": "Küchenuhr", "type": "Haushalt", "rarity": "häufig", "description": "Digitale Eieruhr mit Magnet"},
    {"name": "Mülleimer", "type": "Haushalt", "rarity": "häufig", "description": "30l Pedal-Eimer mit Deckel"},
    {"name": "Mülltrennung", "type": "Haushalt", "rarity": "häufig", "description": "4-fach Trennsystem"},
    {"name": "Kompostbehälter", "type": "Haushalt", "rarity": "häufig", "description": "Bokashi-Eimer 15l"},
    {"name": "Wasserkocher", "type": "Haushalt", "rarity": "häufig", "description": "1,7l Edelstahlkocher"},
    {"name": "Toaster", "type": "Haushalt", "rarity": "häufig", "description": "2-Schlitz-Toaster mit Auftaufunktion"},
    {"name": "Sandwichmaker", "type": "Haushalt", "rarity": "häufig", "description": "Panini-Grill mit Platten"},
    {"name": "Eierkocher", "type": "Haushalt", "rarity": "häufig", "description": "Digitaler Eierkocher für 7 Eier"},
    {"name": "Reiskocher", "type": "Haushalt", "rarity": "häufig", "description": "1,8l Mengenkocher mit Dampfkorb"},
    {"name": "Mixer", "type": "Haushalt", "rarity": "häufig", "description": "Standmixer 1000W"},
    {"name": "Entsafter", "type": "Haushalt", "rarity": "häufig", "description": "Zentrifugenentsafter 500W"},
    {"name": "Schneidemaschine", "type": "Haushalt", "rarity": "häufig", "description": "Elektrische Gemüseschneider"},
    {"name": "Fleischwolf", "type": "Haushalt", "rarity": "häufig", "description": "Manueller Fleischwolf"},
    {"name": "Waffeleisen", "type": "Haushalt", "rarity": "häufig", "description": "Herzförmige Waffelbackform"},
    {"name": "Fondue-Set", "type": "Haushalt", "rarity": "häufig", "description": "Keramik-Käsefondue mit Rechaud"},
    {"name": "Raclette-Grill", "type": "Haushalt", "rarity": "häufig", "description": "12 Pfännchen Elektrogrill"},
    {"name": "Crêpe-Maker", "type": "Haushalt", "rarity": "häufig", "description": "30cm gusseiserne Crêpeplatte"},
    {"name": "Pizzastein", "type": "Haushalt", "rarity": "häufig", "description": "38cm Durchmesser Backstein"},
    
]

SAVE_FILE = "survival_save.pkl"

class ModernInventory(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Survival RPG - Modern Edition")
        self.geometry("1400x800")
        self.configure(fg_color=DARK_THEME['bg'])
        
        self.inventory = []
        self.items_db = ITEMS.copy()
        self.load_game()
        
        self.setup_ui()
        self.bind_events()
        self.update_inventory_display()

    def setup_ui(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Action Panel
        action_frame = ctk.CTkFrame(main_frame)
        action_frame.pack(fill=tk.X, pady=10)
        
        self.create_action_button(action_frame, "Ort durchsuchen", MODERN_ICONS['search'], self.search)
        self.create_action_button(action_frame, "Item erstellen", MODERN_ICONS['add'], self.show_custom_item_dialog)
        self.create_action_button(action_frame, "Items löschen", MODERN_ICONS['delete'], self.delete_items)
        
        # Sortierleiste
        sort_frame = ctk.CTkFrame(main_frame)
        sort_frame.pack(fill=tk.X, pady=10)
        
        sort_options = [
            "Name (Aufsteigend)",
            "Name (Absteigend)",
            "Seltenheit (Aufsteigend)",
            "Seltenheit (Absteigend)"
        ]
        self.sort_combo = ctk.CTkComboBox(
            sort_frame,
            values=sort_options,
            command=lambda _: self.update_inventory_display()
        )
        self.sort_combo.set("Name (Aufsteigend)")
        self.sort_combo.pack(side=tk.RIGHT, padx=10)
        ctk.CTkLabel(sort_frame, text="Sortierung:").pack(side=tk.RIGHT, padx=5)
        
        # Inventory Display
        self.tree = ttk.Treeview(main_frame, columns=('Typ', 'Seltenheit', 'Beschreibung'), show='tree', height=25)
        self.tree.heading('#0', text='Name')
        self.tree.heading('Typ', text='Typ')
        self.tree.heading('Seltenheit', text='Seltenheit')
        self.tree.heading('Beschreibung', text='Beschreibung')
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', 
                      background=DARK_THEME['secondary'],
                      fieldbackground=DARK_THEME['secondary'],
                      foreground=DARK_THEME['fg'],
                      rowheight=35,
                      font=('Segoe UI', 11))
        
        style.configure('Treeview.Heading', 
                      background=DARK_THEME['accent'],
                      foreground=DARK_THEME['fg'],
                      font=('Segoe UI', 11, 'bold'))
        
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Status Bar
        self.status_bar = ctk.CTkLabel(main_frame, text="Bereit", anchor='w')
        self.status_bar.pack(fill=tk.X)

    def create_action_button(self, parent, text, icon, command):
        btn = ctk.CTkButton(parent,
                          text=f"  {icon}  {text}  ",
                          command=command,
                          fg_color=DARK_THEME['accent'],
                          hover_color=DARK_THEME['secondary'])
        btn.pack(side=tk.LEFT, padx=5)

    def bind_events(self):
        self.tree.bind('<Double-1>', self.edit_item_description)
        self.tree.bind('<Button-3>', self.edit_item_description)
        self.tree.bind('<Delete>', lambda e: self.delete_items())
        self.protocol("WM_DELETE_WINDOW", self.save_and_exit)

    def edit_item_description(self, event):
        item_id = self.tree.focus()
        if not item_id:
            return

        item_data = self.tree.item(item_id)
        name = item_data['text'].split(' (Menge: ')[0]
        details = (name,) + tuple(item_data['values'])

        matches = [i for i, item in enumerate(self.inventory)
                 if (item['name'] == name and
                     item['type'] == details[1] and
                     item['rarity'] == details[2])]

        dialog = ctk.CTkToplevel(self)
        dialog.title("Beschreibung bearbeiten")
        dialog.geometry("600x400")

        ctk.CTkLabel(dialog, text=f"Bearbeite: {name}").pack(pady=10)
        
        textbox = ctk.CTkTextbox(dialog, wrap=tk.WORD)
        textbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        textbox.insert("1.0", self.inventory[matches[0]].get('description', ''))

        def save_changes():
            new_description = textbox.get("1.0", tk.END).strip()
            
            for index in matches:
                self.inventory[index]['description'] = new_description
            
            self.update_inventory_display()
            self.save_game()
            dialog.destroy()
            self.show_status(f"Beschreibung für {name} aktualisiert!", DARK_THEME['success'])

        ctk.CTkButton(dialog, text="Speichern", command=save_changes).pack(pady=10)

    def search(self):
        try:
            weights = [RARITY_WEIGHTS[item['rarity']] for item in self.items_db]
            found_items = random.choices(
                self.items_db,
                weights=weights,
                k=random.randint(1, 3)
            )
            
            self.inventory.extend(found_items)
            self.update_inventory_display()
            self.show_status(f"{len(found_items)} neue Items gefunden!", DARK_THEME['success'])
            self.save_game()
        except Exception as e:
            messagebox.showerror("Fehler", str(e))

    def aggregate_items(self):
        aggregated = {}
        for item in self.inventory:
            key = (item['name'], item['type'], item['rarity'], item.get('description', ''))
            if key in aggregated:
                aggregated[key]['quantity'] += 1
            else:
                aggregated[key] = item.copy()
                aggregated[key]['quantity'] = 1
        return list(aggregated.values())

    def update_inventory_display(self):
        aggregated = self.aggregate_items()
        
        sort_key = self.sort_combo.get()
        if "Name" in sort_key:
            aggregated = sorted(aggregated, 
                              key=lambda x: x['name'].lower(),
                              reverse="Absteigend" in sort_key)
        else:
            aggregated = sorted(aggregated,
                              key=lambda x: RARITY_WEIGHTS[x['rarity']],
                              reverse="Absteigend" in sort_key)
        
        self.tree.delete(*self.tree.get_children())
        for item in aggregated:
            display_name = f"{item['name']} (Menge: {item['quantity']})"
            self.tree.insert('', 'end', 
                            text=display_name,
                            values=(item['type'], 
                                   item['rarity'], 
                                   item.get('description', '')))

    def delete_items(self):
        selected = self.tree.selection()
        if not selected:
            return

        to_delete = []
        for item_id in selected:
            item_data = self.tree.item(item_id)
            name = item_data['text'].split(' (Menge: ')[0]
            details = (name,) + tuple(item_data['values'])
            
            matches = [i for i, item in enumerate(self.inventory)
                      if (item['name'] == name and
                          item['type'] == details[1] and
                          item['rarity'] == details[2] and
                          item.get('description', '') == details[3])]
            to_delete.extend(matches)

        if messagebox.askyesno("Bestätigen", 
                             f"{len(to_delete)} Items wirklich löschen?", 
                             icon='warning'):
            for index in sorted(set(to_delete), reverse=True):
                del self.inventory[index]
            
            self.update_inventory_display()
            self.save_game()
            self.show_status(f"{len(to_delete)} Items gelöscht", DARK_THEME['warning'])

    def show_custom_item_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Neues Item")
        dialog.geometry("400x300")
        
        fields = [
            ('Name', 'text', ''),
            ('Typ', 'combo', ['Essen', 'Trinken', 'Waffe', 'Deko', 'Ausrüstung', 'Werkzeug', 'Kleidung', 'Buch', 'Maschine', 'Haushalt', 'Möbel', 'Pflanze', 'Schrott']),
            ('Seltenheit', 'combo', list(RARITY_WEIGHTS.keys())),
            ('Beschreibung', 'text', '')
        ]
        
        entries = {}
        for idx, (label, field_type, *rest) in enumerate(fields):
            ctk.CTkLabel(dialog, text=f"{label}:").grid(row=idx, column=0, padx=10, pady=5, sticky='e')
            
            if field_type == 'combo':
                entry = ctk.CTkComboBox(dialog, values=rest[0])
                entry.set(rest[1] if len(rest) > 1 else '')
            else:
                entry = ctk.CTkEntry(dialog)
                if len(rest) > 0:
                    entry.insert(0, rest[0])
            
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky='ew')
            entries[label] = entry
        
        def add_item():
            try:
                new_item = {
                    'name': entries['Name'].get(),
                    'type': entries['Typ'].get(),
                    'rarity': entries['Seltenheit'].get(),
                    'description': entries['Beschreibung'].get()
                }
                
                if not all([new_item['name'], new_item['type'], new_item['rarity']]):
                    raise ValueError("Alle Pflichtfelder müssen ausgefüllt sein!")
                
                self.items_db.append(new_item)
                self.inventory.append(new_item)
                self.update_inventory_display()
                self.save_game()
                dialog.destroy()
                self.show_status(f"Item '{new_item['name']}' hinzugefügt!", DARK_THEME['success'])
            except Exception as e:
                messagebox.showerror("Fehler", str(e))
        
        ctk.CTkButton(dialog, text="Hinzufügen", command=add_item).grid(row=4, columnspan=2, pady=10)

    def show_status(self, message, color):
        self.status_bar.configure(text=message, text_color=color)
        self.after(3000, lambda: self.status_bar.configure(text="Bereit", text_color=DARK_THEME['fg']))

    def save_game(self):
        with open(SAVE_FILE, 'wb') as f:
            pickle.dump({
                'inventory': self.inventory,
                'items_db': self.items_db
            }, f)

    def load_game(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, 'rb') as f:
                    data = pickle.load(f)
                    self.inventory = data['inventory']
                    self.items_db = data['items_db']
            except Exception as e:
                messagebox.showerror("Fehler", f"Save-File Fehler: {str(e)}")
        else:
            self.items_db = ITEMS.copy()

    def save_and_exit(self):
        self.save_game()
        self.destroy()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = ModernInventory()
    app.mainloop()
