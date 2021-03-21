from collections import defaultdict
import random
import copy
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
import math


print(  "                        Vítám tě investore!")
print()
print("Tento program se pokusí vypočíst rizikovost tvého portfolia a vykreslit jeho časový vývoj.")
print()
print("Pro vytvoření portfolia, stačí postupně v tomto pořadí zadávat:")
print()
print("název firmy")
print("cena zakoupené akcie v dollarech")
print("množství zakoupených akcií")
print("odvětví dané firmy (např.: letectví, ropný průmysl, potravinářství)")
print("subjektivní RIZIKOVOST firmy") 
print()
print("Rizikovostí se rozumí, jak ty osobně vnímáš danou firmu na škále [1-10], kde 1 znamená VELMI BEZPEČNÁ a 10 VYSOCE RIZIKOVÁ firma")
print()
print("Nyní můžes začít s tvorbou vlastního portfolia. Zadávej prosím pro jednoduchost odpovědi a data ve tvarech, které jsou použity v otázkách.")


class Akcie:

    def __init__(self, nazev, cena, množství, odvětví, rizikovost):
        self.nazev=nazev
        self.cena=cena
        self.mnozstvi=množství
        self.odvetvi=odvětví
        self.rizikovost=rizikovost

    def __str__(self):
        return f"({self.nazev}, cena = {self.cena}, množství = {self.mnozstvi}, odvětví = {self.odvetvi}, rizikovost = {self.rizikovost})"

    def __repr__(self):
        return (self.nazev)

    def hodnota (self):
        return (self.cena*self.mnozstvi)

    

seznam_odvetvi=[]
seznam_akcii=[]
pocet_akcii=0

def zadani_firmy():

        global seznam_odvetvi,odpoved, pocet_akcii
        
        while True:
            
            try:
                 nazev=input("název firmy: ")
                 if ((nazev!="") and (nazev!=" ")): 
                     break
                 else:
                     print("Nesprávná hodnota, název by měl obsahovat alespoň 1 charakter (mezera se nepočítá).")

            except ValueError:
                     print("Nesprávná hodnota, název by měl obsahovat alespoň 1 charakter (mezera se nepočítá).")
    
        
        cena=0

        while True:
            
            try:
                 cena=float(input("cena akcie v dollarech: "))   #float je desetinné číslo
                 if (cena>=1 and cena<=5000): 
                     break
                 else:
                     print("Nesprávná hodnota, cena by měla být v intervalu reálných čísel (1,5000).")

            except ValueError:
                     print("Nesprávná hodnota, cena by měla být v intervalu reálných čísel (1,5000).")

        while True:
            
            try:
                 mnozstvi=float(input("množství akcií: "))
                 if (mnozstvi>0): 
                     break
                 else:
                     print("Nesprávná hodnota, množství by mělo být reálné číslo >0.")

            except ValueError:
                     print("Nesprávná hodnota, množství by mělo být reálné číslo >0.")
        
        if pocet_akcii==0:
            while True:
            
                try:
                 odvetvi=input("nové odvětví firmy: ")
                 if ((odvetvi!="") and (odvetvi!=" ")): 
                     break
                 else:
                     print("Nesprávná hodnota, odvětví by mělo obsahovat alespoň 1 charakter (mezera se nepočítá).")

                except ValueError:
                     print("Nesprávná hodnota, odvětví by mělo obsahovat alespoň 1 charakter (mezera se nepočítá).")
            
            seznam_odvetvi.append(odvetvi)
        else:
            
            print("Přejete si přidat nové odvětví?")
            odpoved=input("Ano/Ne: ")
            while not (odpoved=="Ano" or odpoved=="Ne"):
                print("Chybná odpověď, zadat jde jen: Ano/Ne.")
                print("Přejete si přidat nové odvětví?")
                odpoved=input("Ano/Ne: ")
            if odpoved=="Ano":
                while True:
            
                    try:
                     odvetvi=input("nové odvětví firmy: ")
                     if ((odvetvi!="") and (odvetvi!=" ")): 
                         break
                     else:
                         print("Nesprávná hodnota, odvětví by mělo obsahovat alespoň 1 charakter (mezera se nepočítá).")

                    except ValueError:
                         print("Nesprávná hodnota, odvětví by mělo obsahovat alespoň 1 charakter (mezera se nepočítá).")
                         
                while odvetvi in seznam_odvetvi:
                    print("Asi jsi se překlikl, zadej nové odvětví, toto již existuje. Zde je dosavadní seznam.")
                    print(seznam_odvetvi)
                    odvetvi=input("nové odvětví firmy: ")
                seznam_odvetvi.append(odvetvi)
        
            elif odpoved=="Ne":    
                    while True:
            
                        try:
                         odvetvi=input("odvětví firmy: ")
                         if ((odvetvi!="") and (odvetvi!=" ")): 
                             break
                         else:
                             print("Nesprávná hodnota, odvětví by mělo obsahovat alespoň 1 charakter (mezera se nepočítá).")

                        except ValueError:
                             print("Nesprávná hodnota, odvětví by mělo obsahovat alespoň 1 charakter (mezera se nepočítá).")
                             
                    while  not odvetvi in seznam_odvetvi:
                        print("Asi jsi se překlikl, toto odvětví jsi ještě nezadal, zkus to znovu. Zde je dosavadni seznam.")
                        print(seznam_odvetvi)
                        odvetvi=input("odvětví firmy: ")
                        
        while True:
            
            try:
                 rizikovost=int(input("rizikovost firmy [1-10]: "))
                 if (rizikovost>=1 and rizikovost<=10): 
                     break
                 else:
                     print("Nesprávná hodnota, rizikovost musí být celé číslo mezi [1,10].")

            except ValueError:
                     print("Nesprávná hodnota, rizikovost musí být celé číslo mezi [1,10].")
         


        nova_akcie=Akcie(nazev,cena,mnozstvi,odvetvi,rizikovost)
        return(nova_akcie)
    

        
print("Přejete si přidat novou akcii?")
odpoved_1=input("Ano/Ne: ")

while not (odpoved_1=="Ano" or odpoved_1=="Ne"):
                print("Chybná odpověď, zadat jde jen: Ano/Ne.")
                print("Přejete si přidat novou akcii?")
                odpoved_1=input("Ano/Ne: ") 
while odpoved_1=="Ne":
    print("Ale no tak, tvé portfolio je přece prázdné, zkus odpovědět ještě jednou.")
    print("Přejete si přidat novou akcii?")
    odpoved_1=input("Ano/Ne: ")
    while not (odpoved_1=="Ano" or odpoved_1=="Ne"):
                print("Chybná odpověď, zadat jde jen: Ano/Ne.")
                print("Přejete si přidat novou akcii?")
                odpoved_1=input("Ano/Ne: ")

while odpoved_1=="Ano":
    nova_akcie=zadani_firmy()

    print(nova_akcie)

    print("Jsou data akcie v pořádku a může se přidat do portfolia?")
    odpoved_2=input("Ano/Ne: ")
    while not (odpoved_2=="Ano" or odpoved_2=="Ne"):
                print("Chybná odpověď, zadat jde jen: Ano/Ne.")
                print("Jsou data akcie v pořádku a může se přidat do portfolia?")
                odpoved_2=input("Ano/Ne: ")
    if odpoved_2=="Ne":
        print("Opravdu chcete smazat tuto akcii?")
        odpoved_2=input("Ano/Ne: ")
        while not (odpoved_2=="Ano" or odpoved_2=="Ne"):
                print("Chybná odpověď, zadat jde jen: Ano/Ne.")
                print("Opravdu chcete smazat tuto akcii?")
                odpoved_2=input("Ano/Ne: ")
        if odpoved_2=="Ano":
            if (pocet_akcii>0):   
                if odpoved=="Ano":
                    seznam_odvetvi.pop()

        elif odpoved_2=="Ne":
            print("Akcie byla přidána do portfolia.")
            pocet_akcii+=1
            seznam_akcii.append(nova_akcie)

    elif odpoved_2=="Ano":
        pocet_akcii+=1
        seznam_akcii.append(nova_akcie)
        
    print("Přejete si pokračovat v přidávání akcií?")
    odpoved_1=input("Ano/Ne: ")
    while not (odpoved_1=="Ano" or odpoved_1=="Ne"):
                print("Chybná odpověď, zadat jde jen: Ano/Ne.")
                print("Přejete si pokračovat v přidávání akcií?")
                odpoved_1=input("Ano/Ne: ")

    while (odpoved_1=="Ne") and (pocet_akcii==0):
        print("Ale no tak, tvé portfolio je přece prázdné, zkus odpovědět ještě jednou.")
        print("Přejete si pokračovat v přidávání akcií?")
        odpoved_1=input("Ano/Ne: ")
        while not (odpoved_1=="Ano" or odpoved_1=="Ne"):
                print("Chybná odpověď, zadat jde jen: Ano/Ne.")
                print("Přejete si pokračovat v přidávání akcií?")
                odpoved_1=input("Ano/Ne: ")
        
        
print()
print("Nyní je portfolio kompletní, můžeme tedy provést simulaci akciového trhu.")
print()
print("Informace o vašem portfoliu:")
print()
print("počet akcií:", pocet_akcii)
print()
hodnota_portfolia=0
for i in seznam_akcii:
    print(i)
    print("hodnota: ",i.hodnota())
    hodnota_portfolia+=i.hodnota()
    hodnota_portfolia=round(hodnota_portfolia,2)
celkova_hodnota_portfolia=[]
celkova_hodnota_portfolia.append(hodnota_portfolia)


rozdeleni_odvetvi = defaultdict(list)     #zde se provede rozvrzeni portfolia podle odvetvi do seznamu
for i in seznam_akcii:
    rozdeleni_odvetvi[i.odvetvi].append(i)

rozvrzeni_odvetvi=[]
rozvrzeni_odvetvi=(list(rozdeleni_odvetvi.items()))
print()
print("Takto máte rozvrhnuté portfolio podle odvětví: ")
print()
print(rozvrzeni_odvetvi)
print()
print("Celková hodnota portfolia v dollarech: ", hodnota_portfolia)
print()

print("Na kolik časových jednotek má být provedena simulace? (rozumná hodnota pro časovou jednotku=týden by byla 1-100)")
print()
while True:
            
            try:
                 pocet_provedeni=int(input("počet čas. jednotek simulace (dnů/týdnů): "))
                 if (pocet_provedeni>=1 and pocet_provedeni<=1000): 
                     break
                 else:
                     print("Nesprávná hodnota, počet čas. jednotek musí být celé číslo mezi [1,1000].")

            except ValueError:
                     print("Nesprávná hodnota, počet čas. jednotek musí být celé číslo mezi [1,1000].")

#print(pocet_provedeni)

#print(pocet_akcii,seznam_akcii,seznam_odvetvi,rozvrzeni odvetvi)

hodnoty_akcii = defaultdict(list)     
for i in seznam_akcii:
    hodnoty_akcii[i].append(i.cena)

hodnoty_akcii_print=(list(hodnoty_akcii.items()))
#print(hodnoty_akcii_print)

def burzovni_obrat(akcie):

    zmena=random.randint(1,100)
    if zmena in range (1,62-akcie.rizikovost):
        znamenko="+"   #rust akcie
    else:
        znamenko="-"   #pokles akcie
    #print(znamenko)
    procento=[]
    procento=list(range(1,11))*(65+akcie.rizikovost-1)+list(range(11,21))*(54+akcie.rizikovost-1)+list(range(21,31))*(44+akcie.rizikovost-1)+list(range(31,41))*(35+akcie.rizikovost-1)+list(range(41,51))*(27+akcie.rizikovost-1)+list(range(51,61))*(20+akcie.rizikovost-1)+list(range(61,71))*(14+akcie.rizikovost-1)+list(range(71,81))*(9+akcie.rizikovost-1)+list(range(81,91))*(5+akcie.rizikovost-1)+list(range(91,101))*(1+akcie.rizikovost-1)
    #print(procento)   #upravil jsem pravděpodobnosti (místo: 10,9...,1+rizikovost, je to 55,45,36,28,21,15,10,6,3,1,+rizikovost - tedy každé další číslo je vždy o 1 větší...,NEBO OBRACENE)
    procento_1=random.choice(procento)
    #print(procento_1)
    
    if procento_1 in range(1,11):
        procento_final=random.randint(1,10)
    elif procento_1 in range(11,21):
        procento_final=random.randint(11,20)
    elif procento_1 in range(21,31):    
        procento_final=random.randint(21,30)
    elif procento_1 in range(31,41):    
        procento_final=random.randint(31,40)
    elif procento_1 in range(41,51):
        procento_final=random.randint(41,50)
    elif procento_1 in range(51,61):
        procento_final=random.randint(51,60)
    elif procento_1 in range(61,71):
        procento_final=random.randint(61,70)
    elif procento_1 in range(71,81):
        procento_final=random.randint(71,80)
    elif procento_1 in range(81,91):
        procento_final=random.randint(81,90)
    elif procento_1 in range(91,101):
        procento_final=random.randint(91,100)    

    #print(znamenko,procento_final)
        
    return (znamenko, procento_final)  
    



def zmena_hodnoty():

    global hodnoty_akcii,korelace_rozvrzeni
    
    for i in seznam_akcii:      #nova hodnota akcie
    
        (znamenko_final, procento_final_1)=burzovni_obrat(i)

        if procento_final_1>50:
            
            if not i.odvetvi in odvetvi_korel:
                
                    odvetvi_korel.append(i.odvetvi)  #ostatní akcie v tomto odvětví budou korelovat
                    if znamenko_final=="+":
                        korelace_odvetvi[i.odvetvi]=(i,procento_final_1)
                    elif znamenko_final=="-":
                        korelace_odvetvi[i.odvetvi]=(i,-1*procento_final_1)

            elif i.odvetvi in odvetvi_korel:    
                if procento_final_1>abs(korelace_odvetvi[i.odvetvi][1]):
                    if znamenko_final=="+":
                        korelace_odvetvi[i.odvetvi]=(i,procento_final_1)
                    elif znamenko_final=="-":
                        korelace_odvetvi[i.odvetvi]=(i,-1*procento_final_1)               

        if znamenko_final=="+":
            nova_hodnota=(hodnoty_akcii[i])   #kvuli vlastnostem dictionary
            #print(nova_hodnota)
            nova_hodnota_final=(float(nova_hodnota[-1]))*(1+procento_final_1/100)
        
        elif znamenko_final=="-":
            nova_hodnota=(hodnoty_akcii[i])
            #print(nova_hodnota)
            nova_hodnota_final=(float(nova_hodnota[-1]))*(1-procento_final_1/100)
        #print(nova_hodnota_final)
        nova_hodnota_final=round(nova_hodnota_final,2)    
        hodnoty_akcii[i].append(nova_hodnota_final)
    

def korelace():
    
    for i in odvetvi_korel:
        
        for j in rozdeleni_odvetvi[i]:
            
            if not j==korelace_odvetvi[i][0]:    #j=korelace_odvetvi[i][0]akcie s nejvetším/nejmenším nárůstem
                """narust_pomoc=(hodnoty_akcii[j][-1]/hodnoty_akcii[j][-2])
                if narust_pomoc>1:
                    narust=narust_pomoc-1
                else:
                    narust=-1*(1-narust_pomoc)    
                print(narust,narust_pomoc)"""                       #narust konkr. akcie
                
                narust_2=((abs(korelace_odvetvi[i][1]/100)-0.5+(j.rizikovost)/100+((10-korelace_odvetvi[i][0].rizikovost)/100)))/2
                         #!!!!vlastní rizikovost přidává a rizikovost referenční rostoucí/klesající akcie se odčítá
                if korelace_odvetvi[i][1]<0:
                    nova_hodnota_final=(float(hodnoty_akcii[j][-1]))*(1-narust_2)
                    nova_hodnota_final=round(nova_hodnota_final,2)
                    
                    hodnoty_akcii[j].append(nova_hodnota_final)
                elif korelace_odvetvi[i][1]>0:
                    nova_hodnota_final=(float(hodnoty_akcii[j][-1]))*(1+narust_2)
                    nova_hodnota_final=round(nova_hodnota_final,2)
                    
                    hodnoty_akcii[j].append(nova_hodnota_final)


def bankrot():

    for i in seznam_akcii:
        #print(hodnoty_akcii[i][-1], hodnoty_akcii[i][-2],hodnoty_akcii[i][-3])
        if (hodnoty_akcii[i][-1]<1) and (hodnoty_akcii[i][-2]<1) and (hodnoty_akcii[i][-3]<1) and (hodnoty_akcii[i][-1]!=0)  :   #pravidlo NASDAQ o delisting (měsíc hodnota pod 1 dollar)
            bankrot_firma=i
            bankrot_firma_riziko=i.rizikovost

            hodnoty_akcii[i].append(0) # cena 0 způsobí konec vývoje ceny (bankrot), akcie dále figuruje ve statistikách...
            for j in seznam_akcii:
                if not j==bankrot_firma:
                
                    nova_hodnota_final=((float(hodnoty_akcii[j][-1]))*(1-((j.rizikovost+(10-bankrot_firma_riziko))/100)))
                    nova_hodnota_final=round(nova_hodnota_final,2)
                                                                     
                    hodnoty_akcii[j].append(nova_hodnota_final)
                
for i in range(pocet_provedeni):

    odvetvi_korel=[]
    korelace_odvetvi={}
    zmena_hodnoty()
    #print(odvetvi_korel,korelace_odvetvi)
    korelace()
    if i>=2:
        bankrot()
    hodnota_portfolia=0
    for i in seznam_akcii:
        hodnota_portfolia+=hodnoty_akcii[i][-1]*i.mnozstvi
    hodnota_portfolia=round(hodnota_portfolia,2)
    celkova_hodnota_portfolia.append(hodnota_portfolia)
    
hodnoty_akcii_print=(list(hodnoty_akcii.items()))
print()
print("Dosavadni hodnoty ceny akcie v dollarech: ",hodnoty_akcii_print)
print()
    

print("Dosavadní celkové hodnoty portfolia v dollarech: ",celkova_hodnota_portfolia)
print()
#hodnoty_akcii_print=(list(hodnoty_akcii.items()))
#print(hodnoty_akcii_print[0][1])

def final_zuctovani():

    hodnota_portfolia=0
    for i in seznam_akcii:
        #print(i)
        kon_hodnota=hodnoty_akcii[i][-1]*i.mnozstvi
        kon_hodnota_zaokrouh=round(kon_hodnota,2)
        print()
        print()
        print("Konečná hodnota investice v dollarech u akcie",i.nazev,": ",kon_hodnota_zaokrouh)
        procentual_zmena=kon_hodnota/i.hodnota()
        procentual_zmena=round(procentual_zmena,2)
        #print(procentual_zmena)
        if procentual_zmena>1:
            procentual_zmena_final="+"+str(round((procentual_zmena-1)*100,2))
        else:
            procentual_zmena_final="-"+str(round((1-procentual_zmena)*100,2))
            
        print("Procentuální změna (zisk) investice u akcie",i.nazev,": ",procentual_zmena_final,"%")
    print()    
    print("Konečná hodnota portfolia v dollarech je: ",celkova_hodnota_portfolia[-1])

    procentual_zmena_port=celkova_hodnota_portfolia[-1]/celkova_hodnota_portfolia[0]
    procentual_zmena_port=round(procentual_zmena_port,2)
    if procentual_zmena_port>1:
        procentual_zmena_final_port_2="+"+str(round((procentual_zmena_port-1)*100,2))
    else:
        procentual_zmena_final_port_2="-"+str(round((1-procentual_zmena_port)*100,2))
    print()
    print("Procentuální změna (zisk) portfolia je: ", procentual_zmena_final_port_2,"%")

    if procentual_zmena_port>1:
        procentual_zmena_final_port=((procentual_zmena_port-1)*100)
    else:
        procentual_zmena_final_port=-1*((1-procentual_zmena_port)*100)
        
    procentual_zmena_final_port=abs(round(procentual_zmena_final_port))
    #print(procentual_zmena_final_port)
    
    print()
    if procentual_zmena_final_port in range(0,11):
        print("Celková rizikovost vašeho portfolia je 1, je tedy VELMI BEZPEČNÉ.") 
    elif procentual_zmena_final_port in range(11,21):
        print("Celková rizikovost vašeho portfolia je 2, je tedy VELICE BEZPEČNÉ.")
    elif procentual_zmena_final_port in range(21,31):    
        print("Celková rizikovost vašeho portfolia je 3, je tedy BEZPEČNÉ.")
    elif procentual_zmena_final_port in range(31,41):    
        print("Celková rizikovost vašeho portfolia je 4, je tedy SPÍŠE BEZPEČNÉ.")
    elif procentual_zmena_final_port in range(41,51):
        print("Celková rizikovost vašeho portfolia je 5, není tedy ani RIZIKOVÉ, ani BEZPEČNÉ. ")
    elif procentual_zmena_final_port in range(51,61):
        print("Celková rizikovost vašeho portfolia je 6, je tedy MÍRNĚ RIZIKOVÉ.")
    elif procentual_zmena_final_port in range(61,71):
        print("Celková rizikovost vašeho portfolia je 7, je tedy SPÍŠE RIZIKOVÉ.")
    elif procentual_zmena_final_port in range(71,81):
        print("Celková rizikovost vašeho portfolia je 8, je tedy RIZIKOVÉ.")
    elif procentual_zmena_final_port in range(81,91):
        print("Celková rizikovost vašeho portfolia je 9, je tedy VELICE RIZIKOVÉ.")
    elif procentual_zmena_final_port in range(91,1000000000000):
        print("Celková rizikovost vašeho portfolia je 10, je tedy VYSOCE RIZIKOVÉ.")


final_zuctovani()


def graf_hodnoty(hodnoty_akcii_print):
   
    """for i in hodnoty_akcii_print[0][1]:
        i=float(i)"""
    
    hodnoty_akcii_print_ceny=hodnoty_akcii_print[1]
    pocet_provedeni_cen=len(hodnoty_akcii_print_ceny)
    hodnoty_akcii_print_nazev=hodnoty_akcii_print[0].nazev
    titulek="Vývoj ceny akcie "+str(hodnoty_akcii_print_nazev)
    osa_x="Vývoj ceny "+str(hodnoty_akcii_print_nazev)+" během "+str(pocet_provedeni+1)+" dní" #pocet provedení nemusí sedět s počtem na ose x (korelace, atd. > během x dní se cena může změnit > x krát)
    #print(titulek,osa_x)
    hodnoty_akcii_print_ceny = np.array(hodnoty_akcii_print_ceny)
    #print(hodnoty_akcii_print_ceny,hodnoty_akcii_print_nazev)
    x = np.linspace(1,pocet_provedeni_cen,pocet_provedeni_cen)
    #print(x)
    
    plt.plot(x, hodnoty_akcii_print_ceny,'ro-', label=hodnoty_akcii_print_nazev,linewidth=4,markersize=10,)
    #plt.plot(x, svedsko_prvnich_14_dnu,'ko-', label="Švédsko",color='yellow',markersize=10, linewidth=4)
    plt.xlabel(osa_x, fontsize=12)
    plt.ylabel("Hodnota v dollarech",fontsize=12)
    plt.title(titulek,fontsize=18)
    #plt.fill_between(x,cesko_prvnich_14_dnu, svedsko_prvnich_14_dnu)
    plt.xticks(x)
    plt.legend()
    plt.show()   

def graf_portfolio(hodnoty_akcii_print):
   
    
    
    titulek="Celkový vývoj hodnoty portfolia"
    osa_x="Vývoj hodnoty portfolia během "+str(pocet_provedeni+1)+" dní"
    #print(titulek,osa_x)
    hodnoty_portfolia= np.array(hodnoty_akcii_print)
    #print(hodnoty_akcii_print_ceny,hodnoty_akcii_print_nazev)
    x = np.linspace(1,pocet_provedeni+1,pocet_provedeni+1)
    #print(x)
    
    plt.plot(x, hodnoty_portfolia, 'ko-',color='yellow', label="Vývoj hodnoty",linewidth=4,markersize=10,)
    plt.xlabel(osa_x, fontsize=12)
    plt.ylabel("Hodnota v dollarech",fontsize=12)
    plt.title(titulek,fontsize=18)
    #plt.fill_between(x,cesko_prvnich_14_dnu, svedsko_prvnich_14_dnu)
    plt.xticks(x)
    plt.legend()
    plt.show()   

def graf_odvetvi_konec():

    if celkova_hodnota_portfolia[-1]==0:
        print("Celková konečná hodnota vašeho portfolia je bohužel 0. Nelze tedy vytvořit konečný procentuální graf.")
    else:
        
        znacky=seznam_odvetvi
        velikosti_odvetvi=[]
        velikosti=[]
        for i in seznam_odvetvi:
            hodnota_odvetvi=0
        
            for j in rozdeleni_odvetvi[i]:
                hodnota=(hodnoty_akcii[j][-1]*j.mnozstvi)
                #print(hodnota)
                hodnota_odvetvi+=hodnota
            
            #print(hodnota_odvetvi)
        
            velikosti_odvetvi.append(hodnota_odvetvi)
    
        for i in velikosti_odvetvi:
            velikosti.append(round(((i/celkova_hodnota_portfolia[-1])*100),0))

        #print(znacky,velikosti)
        pocet_odvetvi=len(seznam_odvetvi)
        odsazeni=[]
        odsazeni.append(0.2)
        for i in range(pocet_odvetvi-1):
            odsazeni.append(0)

        odsazeni=tuple(odsazeni)
        #barvy=["#524947","#e70038","#03c502","#e8d20d"]
        fig,ax=plt.subplots()
        ax.pie(velikosti,explode=odsazeni,labels=znacky,shadow=True,startangle=330,autopct="%1.0f%%")
        ax.axis("equal")
        plt.title("Konečné procentuální rozložení portfolia podle hodnoty investic v jednotlivých odvětvích.",fontsize=18)
        plt.legend()
        plt.show()           

def graf_odvetvi_zacatek():

    #print(seznam_odvetvi)
    znacky=seznam_odvetvi
    velikosti_odvetvi=[]
    velikosti=[]
    for i in seznam_odvetvi:
        hodnota_odvetvi=0
        
        for j in rozdeleni_odvetvi[i]:
            hodnota=(hodnoty_akcii[j][0]*j.mnozstvi)
            #print(hodnota)
            hodnota_odvetvi+=hodnota
            
        #print(hodnota_odvetvi)
        
        velikosti_odvetvi.append(hodnota_odvetvi)
  
    for i in velikosti_odvetvi:
        velikosti.append(round(((i/celkova_hodnota_portfolia[0])*100),0))

    #print(znacky,velikosti)
    pocet_odvetvi=len(seznam_odvetvi)
    odsazeni=[]
    odsazeni.append(0.2)
    for i in range(pocet_odvetvi-1):
        odsazeni.append(0)

    odsazeni=tuple(odsazeni)
    #barvy=["#524947","#e70038","#03c502","#e8d20d"]
    fig,ax=plt.subplots()
    ax.pie(velikosti,explode=odsazeni,labels=znacky,shadow=True,startangle=330,autopct="%1.0f%%")
    ax.axis("equal")
    plt.title("Počáteční procentuální rozložení portfolia podle hodnoty investic v jednotlivých odvětvích.",fontsize=18)
    plt.legend()
    plt.show()   
    
    
for i in range(len(seznam_akcii)):

    hodnoty_akcii_print=(list(hodnoty_akcii.items()))
    hodnoty_akcii_print_fin=list(hodnoty_akcii_print[i])
    #print(hodnoty_akcii_print_fin,hodnoty_akcii_print_fin[1],hodnoty_akcii_print_fin[0])
    graf_hodnoty(hodnoty_akcii_print_fin)
    
print()
print("Počet dní nemusí sedět s hodnotou na ose x, jelikož kvůli korelaci a bankrotu se cena akcie může změnit vícekrát za den.")
print()
graf_portfolio(celkova_hodnota_portfolia)
graf_odvetvi_zacatek()
graf_odvetvi_konec()


    
