from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
import textblob
import googletrans

LANGUAGES = googletrans.LANGUAGES
NAMES = []
KEYS = []

for key in LANGUAGES:
	KEYS.append(key)
	NAMES.append(LANGUAGES[key])



root = Tk()
root.title("My Translator")
root.geometry("550x450")

text_frame = Frame(root)
text_frame.pack(pady = 20)

inputfield = ScrolledText(text_frame, width = 16, height = 10, font=("MV Boli", 16))
inputfield.grid(row = 0, column = 0)
inputfield.focus()
outputfield = ScrolledText(text_frame, width = 16, height = 10, font=("MV Boli", 16))
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



fr_lbl = Label(button_frame, font = ("MV boli", 10), text = "From:")
fr_lbl.grid(row = 0, column = 0)

menu1 = Combobox(button_frame, values = NAMES, width = 15)
menu1.grid(row = 0, column = 1)
menu1.current(21)

btn = Button(button_frame, font = ("MV boli", 10), text = "Translate!", command = trans, width = 10)
btn.grid(row = 0, column = 2)

fr_lbl = Label(button_frame, font = ("MV boli", 10), text = "To:")
fr_lbl.grid(row = 0, column = 3)

menu2 = Combobox(button_frame, values = NAMES, width = 15)
menu2.grid(row = 0, column = 4)
menu2.current(101)

root.mainloop()