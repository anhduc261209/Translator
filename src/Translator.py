from tkinter import *
from tkinter import messagebox
import textblob

root = Tk()
root.title("My Translator")
root.geometry("490x450")

inputfield = Text(root, width = 16, height = 10, font=("MV Boli", 16))
inputfield.grid(row = 0, column = 0)
outputfield = Text(root, width = 16, height = 10, font=("MV Boli", 16))
outputfield.grid(row = 0, column = 1)

button_frame = Frame(root)
button_frame.grid(row = 1, pady = 10)

def trans():
	try:
		outputfield.delete(1.0, END)
		words = textblob.TextBlob(inputfield.get(1.0, END))
		if clicked.get() == "English -> Tiếng Việt":
			words = words.translate(from_lang = "en", to = "vi")
		else:
			words = words.translate(from_lang = "vi", to = "en")
		outputfield.insert(1.0, words)
	except Exception as e:
		messagebox.showerror("Translator", f"ErRoR: {e}")

clicked = StringVar()
clicked.set("English -> Tiếng Việt")

menu = OptionMenu(button_frame, clicked, "English -> Tiếng Việt", "Tiếng Việt -> English")
menu.grid(row = 0, column = 0)

btn = Button(button_frame, font = ("MV boli", 10), text = "Translate!", command = trans)
btn.grid(row = 0, column = 1, padx = 10)

root.mainloop()