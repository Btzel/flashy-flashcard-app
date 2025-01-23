import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

class Interface:
    def __init__(self):

        self.data = pd.read_csv("./data/french_words.csv", sep=',')
        self.random_row = []
        self.is_active_timer = None
        self.score = 0

        # MAIN WINDOW
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

        #CANVAS
        self.canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
        self.card_image = PhotoImage(file="./images/card_front.png")
        self.canvas_image = self.canvas.create_image(400,263,image=self.card_image)
        self.language_text = self.canvas.create_text(400,150,text="",font=("Arial",20,"italic"))
        self.word_text = self.canvas.create_text(400,263,text="",font=("Arial",45,"bold"))
        self.score_text = self.canvas.create_text(60,40,text=f"Score: {self.score}",font=("Arial",15,"normal"))
        self.canvas.grid(column=0,row=0,columnspan=2)

        # BUTTONS
        self.wrong_image = PhotoImage(file="./images/wrong.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0,command=self.wrong_button_event)
        self.wrong_button.grid(column=0,row=1)
        self.right_image = PhotoImage(file="./images/right.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0,command=self.right_button_event)
        self.right_button.grid(column=1, row=1)

        self.right_english_word = ""
        self.english_word = ""

        self.random_data_row()
        self.window.mainloop()

    def canvas_modifier(self,image_name,language,word):
        self.card_image = PhotoImage(file=f"./images/{image_name}.png")
        self.canvas.itemconfig(self.canvas_image,image=self.card_image)
        self.canvas.itemconfig(self.language_text,text=language)
        self.canvas.itemconfig(self.word_text,text=word)
        if self.is_active_timer is not None:
            self.is_active_timer = None

    def flashy_cards(self):
        french_word = self.random_row[0][0]
        self.right_english_word = self.random_row[0][1]
        wrong_english_word = self.random_row[1][1]
        self.english_word = random.choice([self.right_english_word,wrong_english_word])
        self.canvas_modifier(image_name="card_front",language="French",word=french_word)
        self.is_active_timer = self.window.after(2000,self.canvas_modifier,"card_back","English",self.english_word)

    def random_data_row(self):
        if self.is_active_timer is None:
            self.random_row = self.data.sample(n=2).values.tolist()
            self.flashy_cards()

    def right_button_event(self):
        if self.right_english_word == self.english_word and self.is_active_timer is None:
            self.score += 1
            self.canvas.itemconfig(self.score_text,text=f"Score: {self.score}")

        self.random_data_row()

    def wrong_button_event(self):
        if self.right_english_word != self.english_word and self.is_active_timer is None:
            self.score += 1
            self.canvas.itemconfig(self.score_text,text=f"Score: {self.score}")

        self.random_data_row()

Interface()

