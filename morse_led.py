import tkinter as tk
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
import time

master = tk.Tk()
master.title("Morse Code LED")
myFont = tk.font.Font(family = "Helvetica", size = 12, weight = "bold")
tk.Label(master, text = "Input text (maximum 12 characters)").grid(row = 0)

def led():
    morse = {"a":".-", "b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
             "k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
             "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
    _in = entry.get().lower()[:12]
    for x in _in:
        if x in morse:
            m = morse[x]
            for y in m:
                if y == ".":
                    GPIO.output(7,GPIO.HIGH)
                    time.sleep(0.25)
                elif y == "-":
                    GPIO.output(7,GPIO.HIGH)
                    time.sleep(0.75)
                GPIO.output(7,GPIO.LOW)
                time.sleep(0.25)
            GPIO.output(7,GPIO.LOW)
            time.sleep(0.75)
        elif x == " ":
            time.sleep(1.75)
            
entry = tk.Entry(master)
entry.grid(row = 0, column = 1)
button = tk.Button(master, text = "Blink in Morse Code", font = myFont, command = led,bg = 'yellow', height = 1, width = 24)
button.grid(row = 1, column = 1)