from genetika import *

naredbe=''
while True:
    naredba = input(">>")
    naredbe= naredbe + naredba + '\n'
    ugnijezdeno = 0
    for znak in naredba:
        if znak=='{':
            ugnijezdeno = ugnijezdeno + 1
        if ugnijezdeno > 0:
            komande = ''
            prekid = False
            while True:
                komanda = input("-")
                komande = komande + komanda + '\n'
                for zn in komande:
                    if zn=='{':
                        ugnijezdeno = ugnijezdeno + 1
                    if zn=='}':
                        ugnijezdeno = ugnijezdeno - 1
                    if ugnijezdeno <= 0:
                        naredbe = naredbe + komande
                        prekid = True
                        break
                if prekid == True:
                    break
    kod = P(naredbe)
    #prikaz(kod, 8)
    kod.izvrši()
    naredbe = naredbe.replace('output(', '---') 