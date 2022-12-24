class MyKlanten():
    def __init__(self):
        self.klantnaam=""
        self.klantvoornaam=""
        self.typeklant=""
        self.rekeningnummer=""
        self.saldo=""
    def nieuweklantgegevens(self,nieuw_klantnaam,nieuw_klantvoornaam,nieuw_typeklant,nieuw_rekeningnummer,nieuw_saldo):
        self.klantnaam=nieuw_klantnaam
        self.klantvoornaam=nieuw_klantvoornaam
        self.rekeningnummer=nieuw_rekeningnummer
        self.typeklant=nieuw_typeklant
        self.saldo=nieuw_saldo
        test=[self.klantnaam,self.klantvoornaam,self.typeklant,self.rekeningnummer,self.saldo]
        return test
    
class MyType(MyKlanten):
    def __init__(self,nieuwtype,saldo):
        super().__init__()
        self.nieuwtype=int(nieuwtype)
        self.saldo=int(saldo)
        if self.nieuwtype==3: #bronze
            self.minimumsaldo=0
            self.maxopvragenperkeer=max(0,self.saldo)
        if self.nieuwtype==2: #silver
            self.minimumsaldo=-2500
            self.maxopvragenperkeer=500
        elif self.nieuwtype==1: #golden
            self.minimumsaldo=-5000
            #self.maxopvragenperkeer: geen beperking (enkel het saldo, is andere check)

def typeklanten(nieuwtype,saldo):
    return MyType(nieuwtype,saldo)

klantnummer=0
mydict={}
def nieuweklant(klantnummer,test2):
    nieuw=""
    while nieuw not in ("ja","nee"):
        try:
            nieuw=input("klant ingeven? (ja/nee)")
        except:
            print('verkeerde input')
        else:
            if nieuw=="ja":
                klantnaam=input("nieuw_klantnaam: ")
                klantvoornaam=input("nieuw_klantvoornaam: ")
                typeklant=""
                while typeklant not in (1,2,3):
                    try:
                        typeklant=int(input("nieuw_typeklant? 1:golden 2:silver 3:bronze "))
                    except:
                        print('verkeerde input')
                        typeklant=""
                rekeningnummer=input("nieuw_rekeningnummer: ")
                saldo=""
                while saldo=="":
                    try:                
                        saldo=int(input("nieuw_saldo: "))
                        if saldo<0 and typeklant==3:
                            print('saldo moet >=0 zijn voor bronze klant')
                            saldo=""
                    except:
                        print('verkeerde input')
                        saldo=""
                p=MyKlanten()
                q=p.nieuweklantgegevens(klantnaam,klantvoornaam,typeklant,rekeningnummer,saldo)
                klantnummer+=1
                mydict.update({klantnummer:q})
                test2=mydict
                nieuweklant(klantnummer,test2)
                return test2
            elif nieuw=="nee":
                print('geen nieuwe klant ingegeven')
            
def klantentoevoegen():
    test2={}
    test3=nieuweklant(klantnummer,test2)
#    if test3 is None:
#        print('geen nieuwe toegevoegd')
#    else:
    if test3 is not None: #om op te vangen dat onmiddellijk gekozen wordt voor geen nieuwe klanten bij te voegen (maw, onmiddellijk 'nee' in het programma)
        bestand=open('klanten.txt','a') #klanten.txt doet dienst als extern bestand met klantengegevens
        num_lines = sum(1 for line in open('klanten.txt')) #hiermee tellen we het reeds aanwezige lijnen in de tekst file
        #num_lines = sum(1 for line in bestand) #hiermee tellen we het reeds aanwezige lijnen in de tekst file
        for k,v in test3.items():
            bestand.write(str(k+num_lines)+': '+str(v)+'\n') #hiermee voegen we de nieuwe klanten toe, en zorgen we ervoor dat de teller van nieuwe lijnen op juist getal begint: k+num_lines
        bestand.close()

class Myklanteninlezen():
    def __init__(self):
        #https://www.geeksforgeeks.org/python-string-split/
        #https://note.nkmk.me/en/python-split-rsplit-splitlines-re/
        f=open('klanten.txt')
        g=f.readlines()
        self.famname=[str(x.split('\', \'',1)[0]).split('[\'',2)[1] for x in g] #om 2e veld in klanten.txt te lezen
        self.vrname=[str(x.split('\', ',1)[1]).split('\'',2)[1] for x in g]
        self.typeklant=[x.split('\', ',3)[2][0] for x in g]
        self.reknr=[str(x.split(', \'',3)[2]).split('\'',2)[0] for x in g]
        self.saldo=[str(x.split('\', ',4)[3]).split(']',1)[0] for x in g]
        f.close()

def klanteninlezen():
    return Myklanteninlezen()

class Myklantenselectie():
    def __init__(self,sel):
        print('dit zijn de klanten die reeds aanwezig zijn:')
        self.sel=sel
        self.klanten=klanteninlezen()
        f=open('klanten.txt')
        self.num_lines = sum(1 for line in f)
        for i in range(0,self.num_lines):
            print(i+1,': fam naam:',self.klanten.famname[i],'voornaam:',self.klanten.vrname[i])
        self.klantsel=self.num_lines+2
        while not (1<=self.klantsel<self.num_lines+1):
            try:
                if self.sel==2:
                    self.klantsel=int(input('van welke klant wilt u het saldo opvragen? (cijfer)'))
                elif self.sel==3 or self.sel==4:
                    self.klantsel=int(input('van welke klant wilt u het saldo bijwerken? (cijfer)'))
            except:
                print('verkeerde selectie')
        f.close()

def klantenselectie(sel):
    return Myklantenselectie(sel)

class Mybijstorten():
    def __init__(self,sel):
        self.klanten=klanteninlezen()
        self.t=klantenselectie(sel)
        self.q=self.t.klanten        
        self.bedrag=""
        self.ingeven=-1
        while self.bedrag=="":
            try:
                while self.ingeven<0:
                    if sel==3:
                        message="welk bedrag wilt u bijstorten?: "
                        self.bedrag=int(input(message))
                        self.ingeven=self.bedrag
                    elif sel==4:
                        message="welk bedrag wilt u afhalen?: "                
                        self.bedrag=-int(input(message))
                        self.ingeven=-self.bedrag
            except:
                print('verkeerde input')
                self.bedrag=""
            else:
                nieuwtype=self.q.typeklant[self.t.klantsel-1]
                saldo=self.q.saldo[self.t.klantsel-1]
                self.u=typeklanten(nieuwtype,saldo)
                self.nieuwsaldo=int(saldo)+self.bedrag
                t=self.u
                if sel==4:
                    if (nieuwtype=="2" or nieuwtype=="3") and (-self.bedrag > self.u.maxopvragenperkeer): #geen check op maxopvragenperkeer voor type=1
                        print('opgevraagd bedrag is groter dan max toegelaten, bewerking geannuleerd')
                        print('opgevraagd:',abs(self.bedrag),'maximaal:',self.u.maxopvragenperkeer)
                        self.nieuwsaldo -= self.bedrag
                    elif (self.nieuwsaldo < self.u.minimumsaldo):
                        print('saldo is ontoereikend, bewerking geannuleerd')
                        print('opgevraagd:',abs(self.bedrag),'minimum saldo:',self.u.minimumsaldo)
                        self.nieuwsaldo -= self.bedrag
                    else:
                        self.q.saldo[self.t.klantsel-1]=self.nieuwsaldo
                elif sel==3:
                    self.q.saldo[self.t.klantsel-1]=self.nieuwsaldo
                
def bijstorten(sel):
    p=Mybijstorten(sel)
    return p
    
def klantennaarfile(num_lines,r):
    alle_klanten=[]
    teller=1
    bestand=open('klanten.txt','w')
    for j in range(0,num_lines):
        for i in range(0,2):
            alle_klanten=[r.q.famname[j],r.q.vrname[j],int(r.q.typeklant[j]),r.q.reknr[j],int(r.q.saldo[j])]
        bestand.write(str(teller)+': '+str(alle_klanten)+'\n')
        teller+=1      
    bestand.close()
    #opmerking: hier wordt de volledige file opnieuw gemaakt, dit moet beter kunnen via een update, maar niet gezien hoe dit precies te doen

def selectie():
    sel=""
    while sel not in (1,2,3,4):
        try:
            sel=int(input('wat wilt u doen?\n1:nieuwe klanten invoeren? \n2:saldo uitprinten? \n3:bedrag bijstorten? \n4:bedrag afhalen?\n'))
        except:
            print('verkeerde input')
        else:
            if sel==1:
                klantentoevoegen()
            elif sel in (2,3,4):
                try:
                    #https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
                    #https://linuxize.com/post/python-check-if-file-exists/
                    f=open("klanten.txt")
                except:
                    print('nog geen klanten ingevoerd, gelieve dit eerst te doen')
                else:
                    if sel==2:
                        t=klantenselectie(sel)
                        q=t.klanten
                        print('dit is het saldo voor deze klant:',q.saldo[t.klantsel-1])
                    elif sel==3 or sel==4:
                        r=bijstorten(sel)
                        print('saldo is:',r.nieuwsaldo)
                        numlines=r.t.num_lines
                        klantennaarfile(numlines,r)
                    f.close()

def hoofdprogramma():
    repeat=0
    selectie()
    while repeat==0:
        try:
            repeat=int(input('\nwil u het hoofdmenu opnieuw uitvoeren? (\'1\' is ja)'))
            if repeat != 1:
                repeat=2
        except:
            print('verkeerde input\n')
            repeat=0
        else:
            if repeat==1:
                hoofdprogramma()
            else:
                exit

hoofdprogramma()
