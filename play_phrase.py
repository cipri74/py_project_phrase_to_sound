"""
GUI to write a sentence and speech
"""

import pyttsx3
from tkinter import Tk, Text, Button, CENTER, Label, END

# Settings for speech
engine = pyttsx3.init()
# RATE
engine.setProperty('rate', 150)
# VOICE
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)

class MainWindow(object):
    def __init__(self, title="TextToSpeech", x = 520, y = 300):
        self.__init_main_window()

        self.label = Label(self.__root, text="Please write a sentence in English.")
        self.text_box = Text(self.__root, height=10, width=60, borderwidth=3)
        self.play_button = Button(self.__root, text="Play", justify=CENTER, command=self.get_input_from_text_box)
        self.title = title
        self.size_x = x
        self.size_y = y

        self.__design_main_window()
        self.__add_elements_to_window()
        self.__root.mainloop()

    def __init_main_window(self):
        self.__root = Tk()
        
    def __add_elements_to_window(self):
        self.__design_label()
        self.__design_text_box()
        self.__design_play_button()

    def __design_main_window(self):
        self.__root.resizable(False, False)
        self.__root.title(self.title)
        self.__root.geometry(f"{self.size_x}x{self.size_y}")
        
    def __design_text_box(self):
        self.text_box.grid(row=1, column=0, padx=16, pady=20)

    def __design_play_button(self):
        self.play_button.grid(row=2, column=0, ipadx=20, ipady=10)

    def __design_label(self):
        self.label.grid(row=0, column=0, pady=5)
        
    def get_input_from_text_box(self):
        engine.say(self.text_box.get("1.0", END))
        engine.runAndWait()

if __name__ == '__main__':
    gui = MainWindow()