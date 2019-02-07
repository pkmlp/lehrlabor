# -*- coding: utf-8 -*-

import numpy


def eingabePruefen(eingabe):
    ''' Prüfen, ob der Eingabe String genau drei Integer-Werte sind

    Arguments:
        string eingabe

    Returns:
        boolean -- True wenn die Eingabe korrekt ist
        list    -- Liste mit den drei Integer-Werten

    '''

    # Die Eingabe aufteilen in eine Liste mit den Eingaben
    dreiecksSeiten = eingabe.split()

    # Prüfen, ob genau drei Werte eingegeben wurden
    # wenn nicht, Status False und aufgesplitete Eingabe zurückgeben
    if len(dreiecksSeiten) != 3:
        return False, dreiecksSeiten

    # Versuchen die drei Werte in numerische Werte umzuwandeln
    # wenn nicht möglich, Status False und aufgesplitete Eingabe zurückgeben
    try:
        a = int(dreiecksSeiten[0])
        b = int(dreiecksSeiten[1])
        c = int(dreiecksSeiten[2])
    except:
        return False, dreiecksSeiten

    # Es wurden genau drei numerische Werte eingeben
    # Status True und eine Liste mit den drei umgewandelten
    # Eingabe-Werten zurückgeben
    return True, [a, b, c]


def gueltigesDreieck(a, b, c):
    ''' Prüfen, ob die drei Seiten ein Dreieck bilden können

    Arguments:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Returns:
        boolean -- True wenn die drei Seiten ein Dreieck bilden
                -- False wenn die Summe der zwei kürzeren Seiten
                   nicht grösser als die Länge der längste Seite ist

    '''

    gueltigesDreieck = False

    if (a >= b and a >= c):
        if (b + c > a):
            gueltigesDreieck = True
    elif (b >= c and b >= a):
        if (a + c > b):
            gueltigesDreieck = True
    else:
        if (a + b > c):
            gueltigesDreieck = True

    return gueltigesDreieck


def winkelBerechnen(a, b, c):
    ''' Winkel Berechnung mit Kosinussatz anhand der drei Seiten eines Dreieckes

    α = arccos( (b² + c² - a²) / 2bc )
    β = arccos( (a² + c² - b²) / 2ac )
    γ = arccos( (a² + b² - c²) / 2ab )

    Quelle: https://rechneronline.de/pi/dreieck.php

    Arguments:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Returns:
        float, float, float -- die Winkel α, β, γ

    '''

    # Arkuscosinus berechnen gem. obiger Formeln
    arccos_a = numpy.arccos((b*b + c*c - a*a) / (2*b*c))
    arccos_b = numpy.arccos((a*a + c*c - b*b) / (2*a*c))
    arccos_c = numpy.arccos((a*a + b*b - c*c) / (2*a*b))

    # Arkuscosinus ist in radiant (Bogenmass) und muss umgewandelt
    # werden in degree (Gradmass)
    winkel_a = numpy.rad2deg(arccos_a)
    winkel_b = numpy.rad2deg(arccos_b)
    winkel_c = numpy.rad2deg(arccos_c)

    return winkel_a, winkel_b, winkel_c


def dreieckSeiten(seite_a, seite_b, seite_c):
    ''' Definition des Dreieckes anhand der Seiten

    Arguments:
        a int -- Seite a
        b int -- Seite b
        c int -- Seite c

    Returns:
        str -- gleichseitig, gleichschenklig, ungleichseitig

    '''

    if (seite_a == seite_b and seite_a == seite_c):
        return "gleichseitig"
    elif(seite_a == seite_b or seite_a == seite_c or seite_b == seite_c):
        return "gleichschenklig"
    else:
        return "ungleichseitig"


def dreieckWinkel(gamma):
    ''' Definition des Dreieckes anhand des Winkels gamma

    Arguments:
        γ float -- Winkel γ

    Returns:
        str -- rechtwinklig, spitzwinklig, stumpfwinklig

    '''

    if (gamma > 90.0):
        return "stumpfwinklig"
    elif(gamma < 90.0):
        return "spitzwinklig"
    else:
        return "rechtwinklig"


if __name__ == "__main__":
    #
    # "Hauptprogramm"
    #
    print("                                                                   ")
    print("-------------------------------------------------------------------")
    print("Programm zur Bestimmung eines Dreiecks anhand der drei Seitenlängen")
    print("-------------------------------------------------------------------")
    print("                                                                   ")
    print("  Bitte drei ganzzahlige Werte (getrennt mit Leerschlag) eingeben  ")
    print("    Um das Programm zu beenden alle drei Seiten mit 0 eingeben     ")
    print("                                                                   ")
    print("-------------------------------------------------------------------")
    print("                                                                   ")

    while True:

        eingabe = input("Eingabe der drei Seitenlängen, "
                    "getrennt mit Leerschlag: ")
        print("")

        dreieckOK, dreiecksSeiten = eingabePruefen(eingabe)

        if dreieckOK:
            # Gültige Eingabe, die drei Seiten übernehmen
            a = dreiecksSeiten[0]
            b = dreiecksSeiten[1]
            c = dreiecksSeiten[2]

            # Prüfen, ob Programm abgebrochen werden soll
            if a == 0 and b == 0 and c == 0:
                print("")
                print("Programm beendet")
                print("")
                break

            # Prüfen, ob die drei Seiten ein Dreick sein können,
            # wenn Ja: Dreieck bestimmen und Resultat ausgeben
            # sonst: Fehlermeldung ausgeben
            if (gueltigesDreieck(a, b, c)):
                alpha, beta, gamma = winkelBerechnen(a, b, c)
                print("Gültiges Dreieck:")
                print("    Seiten a / b / c -->", a, "/", b, "/", c)
                print("    Winkel α / β / γ -->", round(alpha, 2), "/", round(beta, 2), "/", round(gamma, 2))
                print("    Typ --> ", dreieckWinkel(gamma), "-", dreieckSeiten(a, b, c))
            else:
                print("Ungültiges Dreieck")
                print("    Seiten a / b / c -->", a, "/", b, "/", c)
            print("-" * 55)
            print()

        else:
            print("ungültige Eingabe")
            print("    -->", eingabe)
            print("-" * 55)
            print()
