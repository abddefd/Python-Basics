# Funktionen: funktionsname()
# Methoden: objekt.methode()

inhalt= "Python rocks \n\r\n"
ausgabe=inhalt.rstrip('\n\r')
print("ausgabe")


inhalt="321  Python 3 rocks"
ausgabe=inhalt.lstrip('123456789')
print(ausgabe)

inhalt=" - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
ausgabe=inhalt.rstrip('\n\r')
print("ausgabe")

