"""
GUI to write a sentence and play a speech
"""

from tkinter import Tk, Text, Button, CENTER, Label

# root = Tk()
# root.title("TextToSpeech")
# root.geometry("600x400")
# e = Entry(root, justify=CENTER)
# play_button = Button(root, text="Play sentence", justify=CENTER)
# e.grid(row=0, column=0)
# play_button.grid(row=1, column=0)

class MainWindow(object):
    def __init__(self, title="TextToSpeech", x = 520, y = 300):
        self.__init_main_window()

        self.label = Label(self.__root, text="Please write a sentence in English (MAX 250 characters): ")
        self.text_box = Text(self.__root, height=10, width=60, borderwidth=3) # TODO check width?
        self.play_button = Button(self.__root, text="Play", justify=CENTER)
        self.title = title
        self.size_x = x
        self.size_y = y

        self.__design_main_window()
        self.__add_elements()
        self.__root.mainloop()
    
    def __init_main_window(self):
        self.__root = Tk()
        
    def __add_elements(self):
        self.__design_label()
        self.__design_text_box()
        self.__design_play_button()

    def __design_main_window(self):
        self.__root.title(self.title)
        self.__root.geometry(f"{self.size_x}x{self.size_y}")
        
    def __design_text_box(self):
        self.text_box.grid(row=1, column=0, padx=16, pady=20)

    def __design_play_button(self):
        self.play_button.grid(row=2, column=0, ipadx=20, ipady=10)

    def __design_label(self):
        self.label.grid(row=0, column=0, pady=5)
        
if __name__ == '__main__':
    # root.mainloop()
    gui = MainWindow()