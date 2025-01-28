print(r"""
  ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-'

***************************
*   TAXI RECHNER          *
*   Fahrpreis berechnen!  *
***************************
""")

print("Willkommen in meinem Taxi Hier Wirst du deinen Preis sehen Können für die Fahrt")
print("")

grundgebühr = 5.70
Kilometerpauschale = 2.50


Kilometer = float(input("Bitte gebe hier deine Kilometer ein: "))
print("Dein Preis den du Zahlen musst Beträgt: ")
print(Kilometer * Kilometerpauschale + grundgebühr, "Euro")
print("")
print("Ich Hoffe sie hatten eine Gute Fahrt mit uns! ")
print("")
