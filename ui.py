from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=300)
        self.question_text = self.canvas.create_text(150, 150, text="Hi", width=280, font=("Ariel", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        self.button1 = Button(command=self.check_answer_t)
        true_img1 = PhotoImage(file="images/true.png")
        self.button1.config(image=true_img1, highlightthickness=0)
        self.button1.grid(row=3, column=1)

        self.button2 = Button(command=self.check_answer_f)
        true_img2 = PhotoImage(file="images/false.png")
        self.button2.config(image=true_img2, highlightthickness=0)
        self.button2.grid(row=3, column=2)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=1, column=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")

    def check_answer_f(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def check_answer_t(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            bg_c = "green"
        else:
            bg_c = "red"
        self.canvas.configure(bg=bg_c)
        self.window.after(1000, self.get_next_question)



