from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
import textblob, googletrans, pyttsx3

try: 
	engine = pyttsx3.init()
except ImportError as e:
	messagebox.showerror("Error: The driver is not found")
except RuntimeError as e:
	messagebox.showerror("Error: The driver fails to initialize")

LANGUAGES = googletrans.LANGUAGES
NAMES = []
KEYS = []

for key in LANGUAGES:
	KEYS.append(key)
	NAMES.append(LANGUAGES[key])

root = Tk()
root.title("My Translator")
root.iconbitmap("icon.ico")

text_frame = Frame(root)
text_frame.pack(pady = 20)

inputfield = ScrolledText(text_frame, width = 16, height = 10, font=("Arial", 16))
inputfield.grid(row = 0, column = 0)
inputfield.focus()
outputfield = ScrolledText(text_frame, width = 16, height = 10, font=("Arial", 16))
outputfield.grid(row = 0, column = 1)
outputfield.configure(state = 'disabled')

button_frame = Frame(root)
button_frame.pack(pady = 20, padx = 0)

def trans():
	try:
		outputfield.configure(state = 'normal')
		outputfield.delete(1.0, END)
		words = textblob.TextBlob(inputfield.get(1.0, END))
		fr = menu1.current()
		fr = KEYS[fr]
		to = menu2.current()
		to = KEYS[to]
		words = words.translate(from_lang = fr, to = to)
		outputfield.insert(1.0, words)
		outputfield.configure(state = 'disabled')
	except Exception as e:
		messagebox.showerror("Translator", f"ErRoR: {e}")

def speak_input():
	engine.say(inputfield.get(1.0, END))
	engine.runAndWait()

def speak_output():
	engine.say(outputfield.get(1.0, END))
	engine.runAndWait()

speak_input_btn = Button(button_frame, font = ("MV boli", 10), text = "Speak", command=speak_input)
speak_input_btn.grid(row = 0, column = 0)

fr_lbl = Label(button_frame, font = ("MV boli", 10), text = "From:")
fr_lbl.grid(row = 0, column = 1)

menu1 = Combobox(button_frame, values = NAMES, width = 15)
menu1.grid(row = 0, column = 2)
menu1.current(21)

btn = Button(button_frame, font = ("MV boli", 10), text = "Translate!", command = trans, width = 10)
btn.grid(row = 0, column = 3)

to_lbl = Label(button_frame, font = ("MV boli", 10), text = "To:")
to_lbl.grid(row = 0, column = 4)

menu2 = Combobox(button_frame, values = NAMES, width = 15)
menu2.grid(row = 0, column = 5)
menu2.current(101)

speak_output_btn = Button(button_frame, font = ("MV boli", 10), text = "Speak", command = speak_output)
speak_output_btn.grid(row = 0, column = 6)

root.mainloop()