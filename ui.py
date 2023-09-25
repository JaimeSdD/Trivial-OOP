from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 18, "italic")
TRUE_IMAGE_PATH = "images/true.png"
FALSE_IMAGE_PATH = "images/false.png"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.setup_window()
        self.create_widgets()
        self.get_next_question()
        self.window.mainloop()


    def setup_window(self):
        self.window.title("Trivial")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    def create_widgets(self):
        self.create_score_label()
        self.create_canvas()
        self.create_answer_buttons()

    def create_score_label(self):
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

    def create_canvas(self):
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, 
            text="Prueba", 
            fill=THEME_COLOR,
            font=FONT
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def create_answer_buttons(self):
        self.true_image = PhotoImage(file=TRUE_IMAGE_PATH)
        self.false_image = PhotoImage(file=FALSE_IMAGE_PATH)

        self.true_button = self.create_answer_button(self.true_image, self.true_pressed)
        self.false_button = self.create_answer_button(self.false_image, self.false_pressed)
    
    def create_answer_button(self, image, function):
        button = Button(image=image, highlightthickness=0, command=function)
        button.grid(row=2, column=0 if image == self.false_image else 1)
        return button
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.set_buttons_active()
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="This is the end of the Quiz")
            self.set_buttons_disabled()

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def set_buttons_active(self):
        self.true_button.config(state="active")    
        self.false_button.config(state="active")
    
    def set_buttons_disabled(self):
        self.true_button.config(state="disabled")    
        self.false_button.config(state="disabled") 

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.set_buttons_disabled()
        self.window.after(1000, self.get_next_question)