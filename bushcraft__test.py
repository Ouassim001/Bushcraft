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


# hieronder vind je de originele opdracht 4 zonder functions
vraaggeld = input("""er moet natuurlijk ook betaald worden, daarom vraag ik je dit.
ben je bereid om een vijfde deel te betalen voor het bushcraften?\n""")
if vraaggeld == "ja":
    print("""dat is mooi om te horen.
    nu volgen er wat vragen voor de aanmeldingen.""")
else:
    print("""sorry ik heb niet iemand nodig die niet kan bijdragen aan deze avontuur.
    nu volgen er wat vragen voor de aanmelding als je niet wilt meebetalen dan kan je dit venster sluiten""")
    time.sleep(5)