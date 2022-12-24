code = "2345"
getal = "0000"
teller = 0
while getal not in code and teller < 10 and getal != "9999":
    test_input=0
    test_getal_lengte=0
    test_getal_zelfde=0
    while test_input != 2:
        zelfde=12
        #4 loops van cijfer_2, over de waarden van cijfer_1; over elke loop mag slechts 1x het cijfer_1 terug gevonden worden: dus 4x3
        getal=input('raad de code: ')
        teller += 1
        print('dit was poging:',teller)
        for cijfer_1 in getal:
            if cijfer_1 not in "1234567":
                #hier: opgevangen dat getal enkel uit cijfers 1 tem 7 mag bestaan, en enkel uit cijfers mag bestaan
                if getal !="9999":
                    getal="10000"
                    #hier: opgevangen dat een letter wordt ingegeven en vermijden dat int(getal) een fout zou geven
                    #we vervangen bv "12a3" door "10000" om in de loop te blijven (foutvermijding)
                    #maar als getal = 9999 moet deze behouden worden om uit programma te kunnen gaan
                break
            else:
                for cijfer_2 in getal:
                    if cijfer_2 != cijfer_1:
                        zelfde -= 1            
        if  getal == "9999":
            print('einde')
            break
        while (int(getal) < 1000 or int(getal)> 9999) and int(getal) != 9999 and teller <10:
            zelfde = 12
            print('getal moet bestaan uit exact 4 verschillende cijfers tussen 1 en 7')
            #kan ook via een len() # maar als len() gebruiken => ook 0123 opgevangen?
            #getal=(input('raad de code-0: '))
            getal=(input('raad de code: '))
            teller += 1
            print('dit was poging:',teller)
            if getal == "9999":
                print('einde')
                zelfde = 0 #om in dit geval de tweede while loop over te slaan
                test_getal_lengte = 1 #om ook uit de hoofdloop te gaan
                break
            for cijfer_1 in getal:
                if cijfer_1 not in "1234567":
                    if getal !="9999":
                        getal="10000"
                    break
                else:
                    for cijfer_2 in getal:
                        if cijfer_2 != cijfer_1:
                            zelfde -= 1
        else:
            test_getal_lengte = 1
        while zelfde != 0 and int(getal) != 9999 and teller < 10:
            print('getal moet bestaan uit exact 4 verschillende cijfers tussen 1 en 7')
            #getal=(input('raad de code-1: '))
            getal=(input('raad de code: '))
            if getal == "9999":
                print('einde')
                test_getal_zelfde = 1 #om uit de hoofdloop te gaan
                break
            teller +=1
            print('dit was poging:',teller)
            zelfde = 12
            for cijfer_1 in getal:
                if cijfer_1 not in "1234567":
                    if getal !="9999":
                        getal="10000"
                    break
                else:
                    for cijfer_2 in getal:
                        if cijfer_2 != cijfer_1:
                            zelfde -= 1            
        else:
            test_getal_zelfde = 1
        test_input = test_getal_lengte + test_getal_zelfde
    else:
        if teller <= 10 and getal != "9999":
            # op = 10: geen format check meer voor deze laatste
            # maar dit is toch de laatste, dus van geen belang meer
            # enkel nog nagaan of dit wel de gevraagde code is
            if getal == code:
                print('juist geraden')
                break
            elif teller == 10:
                print('verkeerd geraden, max aantal bereikt')
                break
            else:
                cijfer_code_correct=0
                cijfer_code_niet_correct=0
                cijfer_positie=0
                for cijfer in getal:
                    cijfer_positie += 1
                    if cijfer in code:
                        code_positie=0
                        for code_getal in code:
                            code_positie += 1
                            if cijfer == code_getal:
                                if cijfer_positie == code_positie:
                                    cijfer_code_correct += 1
                                    #print (cijfer,'komt voor op juiste plaats', 'teller=',cijfer_code_correct)
                                else:
                                    cijfer_code_niet_correct += 1
                                    #print(cijfer, 'komt voor op verkeerde plaats')
                    #else:
                        #print('cijfer ',cijfer,' komt niet voor in de code')
                if cijfer_code_correct != 0:
                    print('er komen',cijfer_code_correct,'cijfers voor op de juiste plaats')
                if cijfer_code_niet_correct != 0:
                    print('er komen',cijfer_code_niet_correct,'cijfers voor op de verkeerde plaats')
                if cijfer_code_correct == 0 and cijfer_code_niet_correct == 0 and getal != "9999":
                    print('geen enkel cijfer komt voor in de code')
        