code = 2345 #dit is de code die moet geraden worden (kan vervangen worden door een random getal)
getal = 1234
teller = 1
bestand=open('code.txt','w')
def aantal_juiste(lijst):
    juiste_plaats = 0
    lijst_code=[]
    for code_cijfer in str(code):
        code_cijfer=int(code_cijfer)
        lijst_code.append(code_cijfer)
    for k in range(0,3):
        if lijst[k]==lijst_code[k]:
            juiste_plaats += 1
    b=str(juiste_plaats)+" cijfers op de juiste plaats"
    print(b)
    bestand.write("\n"+b)
    
def getal_check(getal,teller): #cijfers: enkel 1 tem 7
    if len(str(getal)) == 4:
        lijst = []
        i=1
        check_1=0
        check_2=0
        for cijfer in str(getal):
            cijfer = int(cijfer)
            lijst.append(cijfer)
            if cijfer <1 or cijfer > 7: #elk cijfer van het getal moet tussen 1 en 7 liggen
                check_1 = 1
            for j in range(1,i): #nadien controle dat elke cijfer van het getal maar één keer voorkomt
                if cijfer == lijst[j-1]: 
                    check_2 = 1
            i+=1
        if check_1 == 1:
            b="elke cijfer moet tussen 1 en 7 liggen"
            print(b)
            bestand.write("\n"+b)
        if check_2 == 1:
            b="elk cijfer mag max 1 keer voorkomen"
            print(b)
            bestand.write("\n"+b)
        elif check_1==0 and check_2==0:
            if getal == code:
                b="correct geraden"
                print(b)
                bestand.write("\n"+b)
                teller =11
            else:
                aantal_juiste(lijst)
    else:
        b="het ingegeven getal moet bestaan uit exact 4 cijfers en niet beginnen met een '0'"
        print(b)
        bestand.write("\n"+b)

while teller <= 10 and getal != 9999:
    try:
        getal_1=input("geef een code getal, 4 cijfers, telkens tussen 1 en 7: ")
        getal=int(getal_1)
        b='geef een code getal, 4 cijfers, telkens tussen 1 en 7: '+str(getal)
        bestand.write(b)
    except(ValueError):
        bestand.write("geef een code getal, 4 cijfers, telkens tussen 1 en 7: "+str(getal_1))
        b='dit is geen geheel getal \ndit was poging '+str(teller)
        print(b)
        bestand.write("\n"+b+"\n")
        teller += 1
    else:
        if getal == code:
            b="correct geraden"
            print(b) 
            bestand.write("\n"+b)
            bestand.close()
            teller=11
        elif getal == 9999:
            b="gestopt door gebruiker"
            print(b)
            bestand.write("\n"+b)
            bestand.close()
        else:
            getal_check(getal,teller)
            b="dit was poging "+str(teller)
            print(b)
            bestand.write("\n"+b+"\n")
            teller +=1
else:
    if teller > 10 and getal != 9999 and getal != code:
        b="maximaal aantal pogingen bereikt\nhet gezochte getal was: "+str(code)
        print(b)
        bestand.write("\n"+b)
        bestand.close()