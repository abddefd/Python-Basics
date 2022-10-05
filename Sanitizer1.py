
teststring1 = " - Hallo dies ist ein Test des Sanitizers() der <xml> und ggf auch 'sql SELECT FROM * WHERE X='Y' - erfasst werden!' "
teststring2 = ' <html> ist eine tolle Sprache</html> '
teststring3 = "Hacker schleusen auch gerne Code ein! test()"
teststring4 = " ebenso kommen gerne leerzeichen am Anfang von Eingaben vor!"
teststring5 = r"Oder am Ende von Eingaben "
teststring6 = r"""Hier folgt ein Codeabschnitt : \nif true:\n    print("wahr")\nelse:\n    print("falsch")\n"""
teststring7 = r"""Hier folgt ein Codeabschnitt : \nif true:\n    print('wahr')\nelse:\n    print('falsch')\n"""
teststring8 = r"<dieser String ist nun sanitized>"




notlikeChr =  [ "\\n", "<", ">", "(", ")", ";", "\"", "'", "-", "{", "}", "[", "]", " ", " ", r"*"]



teststrings = [teststring1, teststring2, teststring3, teststring4, teststring5, teststring6, teststring7, teststring8]




def sanitize(toScan):
    for x in notlikeChr:
        print ("enthält " + "\"" + x + "\"" + " : " + str(toScan.count(x))   )
        toScan = toScan.replace(x,'')
        Ausgabestring =  toScan   
    return (Ausgabestring)




#print (teststrings[1]) ; print("\n\r")



for teststring in teststrings:
    print("Eingangsstring\t" + "\"" + teststring + "\"");    #print("\n\r")
    print("Ausgabestring\t" + "\"" + sanitize (teststring)+ "\"");    print("\n\r")
