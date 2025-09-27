import random

def szam_vizsgalat():
    bemenet = input("Kérem adjon meg egy számot: ")
    
    try:
        # Próbáljuk meg egész számként konvertálni
        szam = int(bemenet)
        print(f"A megadott szám ({szam}) egész szám, ", end="")
        
        # Ellenőrizzük, hogy pozitív vagy negatív
        if szam > 0:
            print("pozitív, ", end="")
        elif szam < 0:
            print("negatív, ", end="")
        else:
            print("nulla, ", end="")
        
        # Osztók keresése
        osztok = []
        for i in range(1, abs(szam) + 1):
            if szam % i == 0:
                osztok.append(i)
        
        print(f"osztói: {osztok}")
        
        # Prímszám ellenőrzés (csak pozitív számokra)
        if szam > 1 and len(osztok) == 2:
            print(f"A {szam} egy prímszám.")
        
    except ValueError:
        try:
            # Ha nem sikerült, próbáljuk meg lebegőpontos számként
            szam = float(bemenet)
            print(f"A megadott szám ({szam}) lebegőpontos szám, ", end="")
            if szam > 0:
                print("pozitív.")
            elif szam < 0:
                print("negatív.")
            else:
                print("nulla.")
        except ValueError:
            print("Hibás adatbevitel! Kérem számot adjon meg.")
            return

def szoveg_betuszamlalas():
    szoveg = input("Kérem adjon meg egy szöveget: ")
    betuk_szama = 0
    
    for betu in szoveg:
        if betu.isalpha():
            betuk_szama += 1
    
    print(f"A megadott szövegben {betuk_szama} betű található.")
    print(f"A szöveg hossza összesen: {len(szoveg)} karakter.")

def veletlenszamok_munkaja():
    try:
        darab = int(input("Hány véletlenszámot generáljon? "))
        if darab <= 0:
            print("A szám legyen pozitív!")
            return
            
        szamok = []
        for _ in range(darab):
            szamok.append(random.randint(1, 100))
        
        print(f"Generált számok: {szamok}")
        print(f"Minimum: {min(szamok)}")
        print(f"Maximum: {max(szamok)}")
        print(f"Átlag: {sum(szamok) / len(szamok):.2f}")
        
    except ValueError:
        print("Hibás adatbevitel! Kérem számot adjon meg.")

def ciklus_peldak():
    print("\nCiklusok bemutatása - break, continue és pass használatával")
    
    # Break bemutatása
    print("\n1. Break használata (ciklusból való kilépés):")
    for i in range(1, 11):
        if i == 5:
            print(f"Kilépés a ciklusból, mert elérkeztünk az 5-öshöz (i={i})")
            break
        print(f"Érték: {i}")
    
    # Continue bemutatása
    print("\n2. Continue használata (lépés kihagyása):")
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"{i} páros szám, kihagyjuk")
            continue
        print(f"{i} páratlan szám, feldolgozzuk")
    
    # Pass bemutatása
    print("\n3. Pass használata (üres művelet, helykitöltő):")
    print("Egy egyszerű példa, ahol a pass használható:")
    for i in range(3):
        if i == 1:
            print(f"{i} esetén: pass (nem csinálunk semmit)")
            pass  # Itt nem csinálunk semmit, csak folytatjuk
        else:
            print(f"{i} esetén: normális művelet")
    
    print("\nEgy másik példa a pass használatára:")
    def masodik_fuggveny():
        print("Ez egy üres függvény, a pass használatával")
        pass
    
    masodik_fuggveny()
    print("\nCiklusok befejeződtek!")

def main():
    while True:
        print("\nVálasszon a lehetőségek közül:")
        print("1. Szám vizsgálat")
        print("2. Szöveges betűszámolás")
        print("3. Véletlenszámokkal való munka")
        print("4. Ciklusok bemutatása (break/continue/pass)")
        print("0. Kilépés")
        
        valasztas = input("Kérem válasszon: ")
        
        if valasztas == "1":
            szam_vizsgalat()
        elif valasztas == "2":
            szoveg_betuszamlalas()
        elif valasztas == "3":
            veletlenszamok_munkaja()
        elif valasztas == "4":
            ciklus_peldak()
        elif valasztas == "0":
            print("Viszlát!")
            break
        else:
            print("Érvényes választás adjon meg!")
        
        input("\nNyomjon Entert a folytatáshoz...")

if __name__ == "__main__":
    main()
