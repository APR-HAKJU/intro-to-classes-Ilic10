# TODO: 
# Aufgabe 1:
"""Erstelle eine Klasse Buch mit folgenden Attributen:

- titel
- autor
- seiten
- gelesen (Boolean )

Erstelle zwei Bücher: Eines, das du gelesen hast (setze gelesen=True), 
und eines, das du noch nicht gelesen hast.
"""

class Buch: 
    def __init__(self):
        self.titel = titel 
        self.autor = autor 
        self.seiten  = seiten
        self.gelesen = gelesen
        print("Neues Buch wurde erstellt!")

buch_1= Buch( titel="Harry Potter", autor="JK Rowlig", seiten=300 ,gelesen=True )
buch_2= Buch (titel ="Nibelungenlied", autor="Horst Unteregger", seiten=150, gelesen= False )

print(buch_1.titel)

buch_3= Buch("Die drei Fragezeichen", "Horst Unteregger", 100 , True)


# TODO: Aufgabe 2:
# Gib für jedes Buch eine Nachricht aus, die angibt, ob du das Buch gelesen hast oder nicht.


print(f"{buch_1.titel}wurde gelesen: {buch_1.gelesen}")
print(f"{buch_2.titel}wurde gelesen: {buch_2.gelesen}")
print(f"{buch_3.titel}wurde gelesen: {buch_3.gelesen}")

