"""
GUI to write a sentence and play a speech
"""

from tkinter import Tk, Entry, Button

root = Tk()
root.title("TextToSpeech")
e = Entry(root)
play_button = Button(root, text="Play sentence")
e.grid(row=0, column=0)
play_button.grid(row=1, column=0)

if __name__ == '__main__':
    root.mainloop()