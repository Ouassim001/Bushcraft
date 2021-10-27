# Opdracht 1
import time
input("wat is de dieselprijs per liter? ") 
print("je moet 21 keer tanken")
num1 = 21
num2 = 1.67
num = num1 * num2
print(num)
time.sleep(1)
print("je medehelden willen ook nog wat eten. jij betaalt voor ze")
numa = 8
numb = 5
numbroodjes = numa * numb
print (numbroodjes)
print(num + numbroodjes)
time.sleep(1)
print("je betaalt hetzelfde voor de terugreis en dat is")
time.sleep(1)
print(num + numbroodjes)
# Opdracht 2
print("je hebt wel wat eten nodig anders overleef je het niet")
input("hoe duur zijn de pemmican-repen per pak? ")
numreep = 0.58
numkeer = 6
numprijs = numreep * numkeer
print(numprijs)
time.sleep(1)
input("hoe duur zijn de vijgenplakken per stuk? ")
numvijg = 1.24
numk = 3
numprijs2 = numvijg * numk
print(numprijs2)
time.sleep(1)
input("hoe duur is de scheepsbiscuit? ")
numscheep = 2.67
numkeer = 2
numprijs3 = numscheep * numkeer
print(numprijs3)
time.sleep(1)
input("""je hebt ook wat survivalspullen nodig
bijvoorbeeld lucifers en dat soort dingen. hoeveel firesteels wil je en hoeveel kost een firesteel per stuk?""")
numfire = 3.26
numkeer1 = 2
numprijs4 = numfire * numkeer1
print(float(numprijs4))
input("hoe duur is een luciferdoosje? ")
numlucifer = 0.21
numkeer2 = 5
numprijs5 = numlucifer * numkeer2
print(numprijs5)
input("hoe duur is een originele vuursteen? ")
numsteen = 2.23
numkeer3 = 4
numprijs6 = numsteen * numkeer3
print(numprijs6)
input("hoeveel kost het als je 2 meter aan sisaltouw wilt hebben? ")
numtouw = 0.59
numkeer4 = 10
numprijs7 = numtouw * numkeer4
print(numprijs7)
print("het totale aan wat je kwijt bent aan benodigheden is")
time.sleep(1)
input(int(numprijs + numprijs2 + numprijs3 + numprijs4 + numprijs5 + numprijs6 + numprijs7))
# Opdracht 4
# dit is ook Opdracht 5, want ik heb opdracht 5 hierin geplakt
import time
def vraaggeld():
    print("""er moet natuurlijk ook betaald worden, daarom vraag ik je dit.
ben je bereid om een vijfde deel te betalen voor het bushcraften?\n""")
    ans = input("ja/nee\n")
    if ans == "ja":
        oke()
    else:
        gierig()

def oke():
    print("Dat is mooi om te horen.")
    time.sleep(1)
    print("Nu volgen er wat vragen voor de aanmeldingen.")
    

def gierig():
    print("Sorry ik heb niet iemand nodig die niet kan bijdragen aan deze avontuur.")
    time.sleep(1)
    print("Nu volgen er wat vragen voor de aanmelding als je niet wilt meebetalen dan kan je dit venster sluiten")
    time.sleep(5)

vraaggeld()
# Opdracht 3
print("""++++ Dit is de aanmelding voor de medehelden. ik zoek iemand die sterk is; ik heb ook een slimmerik nodig; wat ik ook nodig heb is iemand die handig is, en iemand die veel kan maken van wat de natuur hem geeft ++++""")
time.sleep(1)
geschikt = "je lijkt geschikt voor deze aanmelding, je zult zeker wat van mij horen"
ongeschikt = "sorry maar je bent niet het type dat ik zoek voor deze zware tocht"
eerstebeer = input("hoeveel kilo kan je bankdrukken?\n")
if eerstebeer == "100":
    print("isgood")
    tweedebeer = input("""kan je wasmachines optillen zonder iemands hulp
    a. heb ik een of meerdere keren gedaan
    b. heb ik nog nooit gedaan\n""")
    if tweedebeer == "a":
        print(geschikt)
        print("nu volgt de aanmelding voor de vos, als je je niet wilt aanmelden voor de vos dan kan je dit venster sluiten")
        time.sleep(2)
    else:
        print(ongeschikt)
        time.sleep(2)
    print("nu volgt de aanmelding voor de vos")
    time.sleep(2)
else:
    print(ongeschikt)
    time.sleep(2)
    print("nu volgt de aanmelding voor de vos")
    time.sleep(2)
eerstevos = input("hoe hoog is je iQ?\n")
if eerstevos == "130":
    print("oké ik heb nog een vraag voor je voor deze aanmelding")
elif eerstevos == "120":
    print("oké ik heb nog een vraag voor je voor deze aanmelding")
    tweedevos = input("kan je een ikea kast snel of traag in elkaar zetten?\n")
    if tweedevos == "snel":
        print(geschikt)
        print("nu volgt de aanmelding voor de bever, als je je niet wilt aanmelden voor de bever dan kan je dit venster sluiten")
        time.sleep(2)
    else:
        print(ongeschikt)
        time.sleep(2)
    print("nu volgt de aanmelding voor de bever")
    time.sleep(2)
else:
    print(ongeschikt)
    time.sleep(2)
    print("nu volgt de aanmelding voor de bever")
    time.sleep(2)
eerstebever = input("hoeveel meter breed was de grootste sloot waarover je bent gesprongen in cijfers?\n")
if eerstebever == "3":
    print("ik heb nog één vraag voor je")
    tweedebever = input("binnen hoeveel minuten in cijfers kan jij een vuurtje maken met een vuursteen en wat hooi")
    if tweedebever == "1":
        print(geschikt)
        print("nu volgt de aanmelding voor de uil, als je je niet wilt aanmelden voor de bever dan kan je dit venster sluiten")
        time.sleep(2)
    else:
        print(ongeschikt)
        time.sleep(2)
    print("nu volgt de aanmelding voor de uil")
    time.sleep(2)
else:
    print(ongeschikt)
    time.sleep(2)
    print("nu volgt de aanmelding voor de uil")
    time.sleep(2)
eersteuil = input("hoeveel eetbare paddestoelen kan je herkennen in het bos?\n")
if eersteuil == "10":
    print("ik heb nog één laatste vraag voor je")
    tweedeuil = input("hoeveel giftige kruiden kan je herkennen als je alleen in het bos bent")
    if tweedeuil == "20":
        print(geschikt)
        time.sleep(1)
        print("dat waren de aanmeldingen voor de medehelden.")
    else:
        print(ongeschikt)
else:
    print(ongeschikt)


