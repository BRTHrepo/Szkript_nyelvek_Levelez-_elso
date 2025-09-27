def main():
    """Fő program, ami menüt biztosít a különböző programok futtatásához."""
    while True:
        print("\n=== Főmenü ===")
        print("1. p021.py - Szám vizsgálat, szöveges betűszámolás, véletlenszámok, ciklus példák")
        print("2. p022.py - Turtle grafikus négyzet rajzolás")
        print("0. Kilépés")
        
        valasztas = input("Kérem válasszon: ")
        
        if valasztas == "1":
            print("\nIndítás: p021.py")
            # Importáljuk és futtatjuk a p021.py főprogramját
            import p021
            p021.main()
        elif valasztas == "2":
            print("\nIndítás: p022.py")
            # Importáljuk és futtatjuk a p022.py főprogramját
            try:
                import p022
                p022.main()
            except Exception as e:
                print(f"Hiba történt a p022.py futtatásakor: {e}")
                print("A program továbbra is működik, de a turtle grafika elérhetetlen.")
        elif valasztas == "0":
            print("Viszlát!")
            break
        else:
            print("Érvényes választás adjon meg!")
        
        if valasztas != "0":
            try:
                input("\nNyomjon Entert a folytatáshoz...")
            except (KeyboardInterrupt, EOFError):
                print("\nAutomatikus folytatás (megszakítás vagy nem interaktív környezet).")

if __name__ == "__main__":
    main()
