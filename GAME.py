import random 
naudas=20000

print("Sveiki, šeit ir kazino Sergei, vai vēlaties spēlēt?")
while naudas>0:
    
    pirm=random.choice(["Banans","ābols","apelsīns","arbūzs"])
    otr=random.choice(["Banans","ābols","apelsīns","arbūzs"])
    treš=random.choice(["Banans","ābols","apelsīns","arbūzs"])
    
    izvēle=input("Ja vēlaties spēlēt, nospiediet 1, ja nē, nospiediet 2. ")
    if izvēle=="1":
        
        if pirm==otr or pirm==treš or otr==treš:
            print( pirm,otr,treš,"jūs uzvarējāt!!!.")
            naudas = naudas * 2
            print(f"Jūsu nauda: {naudas} EUR")
        
        elif (otr==treš) and (pirm==otr):
             print( pirm,otr,treš,"DŽEKPOTS!!!!!!.")
             naudas=naudas*5
             print(f"Jūsu nauda: {naudas} EUR")
          
        else:
            print(pirm, otr, treš, "Jūs neko neuzvarējāt.")
            naudas = naudas/2
            print(f"Jūsu atlikušā nauda: {naudas} EUR")
            
    elif izvēle=="2":
        print("Uz redzēšanos.")
        break
    else :
        print("Lūdzu, ievadiet derīgu skaitli.")
        
    if naudas <= 1000:
        print("Jums vairs nav naudas lai spēlēt (1000). Spēle beigusies.")
