import random
bestand=open('eindopdracht.txt','w')

def raadselsdef():
    #https://groepsspellen.nl/raadsels/
    raadsel1='\n75% van een klas heeft de eerste vraag van een test goed beantwoord \n55% heeft de tweede vraag goed beantwoord \nen 20% heeft beide vragen fout beantwoord \nwelk percentage heeft beide antwoorden goed beantwoord?\n'
    raadsel2="\nFrank, Jasper en Peter hebben ruzie \nFrank zegt dat Jasper liegt \nJasper zegt dat Peter liegt\nPeter zegt dat Frank en Jasper liegen \nWie spreekt de waarheid?\n1:Frank\n2:Jasper\n3:Peter\n"
    raadsel3='\nEen slak zit in de put....20m diep.\nOverdag kruipt hij 5 meter omhoog.\ns Nachts zakt hij weer 4 meter.\nNa hoeveel dagen is hij boven?\n'
    #http://www.puzzlesite.nl/harder/index_nl.html#word_sums
    raadsel4='\nGegeven volgende reeks: 2 9 3 1 8 4 3 6 5 7 \nWat is het volgende getal in deze reeks?\n'
    raadsel5='\nBoer Axel heeft nieuwe koeien en kippen gekocht. \nSamen hebben de dieren 25 koppen en 72 poten. \nHoeveel kippen heeft boer Axel gekocht?\n'
    #http://www.puzzlesite.nl/math/boys_and_girls_nl.html
    raadsel6='\nRonald en Michelle hebben twee kinderen. \nDe kans dat het eerste kind een meisje is, is 50%. \nDe kans dat het tweede kind een meisje is, is ook 50%. \nRonald en Michelle vertellen je dat ze een dochter hebben.\nHoe groot de kans dat hun andere kind ook een meisje is? (in %, geen cijfers na de komma)\n'
    #http://www.puzzlesite.nl/logical/absurd_answers_nl.html
    raadsel7='\nHier staan drie antwoorden:\n1: Antwoord A\n2: Antwoord A of B\n3: Antwoord B of C\nEr is slechts één correct antwoord op deze vraag. \nWelk van de antwoorden is dat (1,2,3)?\n'
    #http://www.puzzlesite.nl/logical/the_round_table_nl.html
    raadsel8='\nGisteravond hebben Heleen en haar man hun buren (twee echtparen) uitgenodigd voor een diner bij hen thuis. \nDe zes personen zaten aan een ronde tafel. \nHeleen vertelt je het volgende:\n Victor zat links van de vrouw die links zat van de man die links zat van Anna.\n Esther zat links van de man die links zat van de vrouw die links zat van de man die links zat van de vrouw die links zat van mijn man.\n Jim zat links van de vrouw die links zat van Roger.\n Ik zat niet naast mijn man.\nWat is de naam van Heleens man?\n1: Victor 2: Jim 3: Roger\n'
    #http://www.puzzlesite.nl/logical/barbaras_boxes_nl.html
    raadsel9='\nBarbara heeft dozen in drie formaten: groot, standaard en klein. \nZe zet 11 grote dozen op tafel. \nSommige van deze dozen laat ze leeg, en in elk van de andere plaatst ze 8 standaarddozen. \nSommige van die standaarddozen laat ze leeg, en in elk van de andere plaatst ze 8 (lege) kleine dozen. \nVan alle dozen op tafel zijn er nu 102 leeg.\nHoeveel dozen heeft Barbara in totaal gebruikt?\n'
    #https://www.standaard.be/cnt/dmf20190827_04577182
    raadsel10='\nWelke is het enige getal waarvan de letters in opklimmende alfabetische volgorde staan?\n'
    global raadsels
    raadsels=(raadsel1,50,raadsel2,2,raadsel3,16,raadsel4,2,raadsel5,14,raadsel6,33,raadsel7,3,raadsel8,3,raadsel9,115,raadsel10,8)

def tekstbestand(ronde,aantal,correct,raadsels_resultaat,opgelost):
    bestand.write('ronde: '+str(ronde))
    bestand.write('\ndeze ronde bestond uit '+str(aantal)+' raadsels\n')
    bestand.write('daarvan heeft u er '+str(opgelost)+' opgelost\n')
    bestand.write('waarvan '+str(correct)+' goed opgelost\n')
    for k in range(0,opgelost):
        bestand.write('raadsel '+str(k+1)+': '+raadsels_resultaat[k]+'\n')
    bestand.write('u heeft dus '+str(round(correct/aantal*100))+'% behaald\n')

raadselsdef()
raadsels_resultaat={}
naam=input('wat is je naam?\n')
bestand.write('kandidaat: '+naam+"\n")
ronde=1
opnieuw=1
while opnieuw==1:
    aantal=11
    correct=0
    opgelost=0
    while aantal > 10:
        try:
            aantal=int(input('\nhoeveel raadsels wil je oplossen? \nmaximum:10 \nom te stoppen:0 \n'))
        except:
            print('verkeerde ingave')
        else:
            if aantal==0:
                opnieuw=0
    selectie=[]
    raadsel_sel=random.randint(0,9)
    for k in range(0,aantal):
        while raadsel_sel in selectie:
            raadsel_sel=random.randint(0,9)
        selectie.append(raadsel_sel)
    #print(selectie)
    stop=1
    for k in range(0,aantal):
        if stop ==1:
            raadsels_resultaat.update({k:0})
            raadsel_ok=0
            print('\nRaadsel ',k+1)
            while raadsel_ok==0:
                try:
                    raadsel_antw=int(input(raadsels[2*selectie[k]-2]))
                except:
                    print('dit is geen geldige input')
                else:
                    raadsel_ok=1
                    if raadsel_antw==raadsels[2*selectie[k]-1]:
                        raadsels_resultaat[k]="correct"
                        correct+=1
                        opgelost+=1
                        print('correct')
                    elif raadsel_antw==0:
                        raadsels_resultaat[k]="gestopt"
                        print('stop')
                        stop=0
                    else:
                        raadsels_resultaat[k]="niet correct"
                        print('niet correct')
                        opgelost+=1
    #print(raadsels_resultaat)
    if opnieuw != 0:
        tekstbestand(ronde,aantal,correct,raadsels_resultaat,opgelost)
        try:
            opnieuw=int(input('nog een keer? (ja=1)'))
        except:
            print('verkeerde input')
        ronde+=1

bestand.close()