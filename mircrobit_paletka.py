from microbit import *

y = 0
x = 1
kierunek_y = 1
kierunek_x = 1
jasnosc = 1

paletka = 3

game_over = False

def zmien_wsp(wartosc, kierunek):
    return wartosc + (1 * kierunek)

def zmien_kierunek(wartosc, kierunek, czy_y=False):
    if (czy_y and wartosc == 3) or (not czy_y and wartosc == 4) or wartosc == 0:
        kierunek = kierunek * -1
    return kierunek
     
while not game_over:
    display.clear()
    jasnosc = y * -1 + 9
    
    y = zmien_wsp(y, kierunek_y)
    x = zmien_wsp(x, kierunek_x)
    
    kierunek_x = zmien_kierunek(x, kierunek_x)
    kierunek_y = zmien_kierunek(y, kierunek_y, True)
    
    if y == 3 and not (x == paletka or x == paletka + 1):
        game_over = True
        
    display.set_pixel(x, y, jasnosc)
    display.set_pixel(paletka, 4, 9)
    display.set_pixel(paletka + 1, 4, 9)
   
    if button_a.was_pressed() and paletka > 0:
        paletka -= 1
    if button_b.was_pressed() and paletka < 3:
        paletka += 1
        
    sleep(200)
    
display.scroll(str(round(running_time() / 1000)))