import turtle

class SquareDrawer:
    """Ez az osztály felelős a turtle grafikai négyzet rajzolásáért."""
    
    def __init__(self):
        """Inicializálja a turtle objektumot."""
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()
        
    def setup(self):
        """Beállítja a turtle alapvető tulajdonságait."""
        self.turtle.speed(1)  # Lassú sebesség a jobb láthatóságért
        self.turtle.color("blue")  # Kék szín
        self.turtle.pensize(3)  # Vastagabb toll
        self.screen.title("Négyzet rajzolás Turtle segítségével")
        self.screen.bgcolor("white")
        
    def draw_square(self):
        """Rajzol egy négyzetet a turtle segítségével."""
        for _ in range(4):
            self.turtle.forward(100)  # 100 pixel előre
            self.turtle.right(90)    # 90 fok fordulás jobbra
            
    def finish(self):
        """Befejezi a rajzot és várja a bezárást."""
        print("A négyzet elkészült! Kattintson az ablak bezárásához.")
        self.screen.mainloop()

def main():
    """Fő program, ami létrehozza és használja a SquareDrawer osztályt."""
    try:
        # Példányosítjuk a SquareDrawer osztályt
        drawer = SquareDrawer()
        
        # Beállítjuk a tulajdonságokat
        drawer.setup()
        
        # Rajzoljuk a négyzetet
        drawer.draw_square()
        
        # Befejezzük a rajzot
        drawer.finish()
    except Exception as e:
        print(f"Hiba történt a turtle grafika indításakor: {e}")
        print("Lehetséges okok: Tkinter/Tcl nincs telepítve vagy hibásan konfigurálva.")
        print("Kérjük, telepítse a Tkinter-t: pip install tk")

if __name__ == "__main__":
    main()
