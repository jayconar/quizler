from tkinter import *
from brains import QuizBrain

BG = "#101D6B"


class Interface:
    def __init__(self, quiz: QuizBrain):
        self.screen = Tk()
        self.screen.title("Quizler")
        self.screen.config(bg=BG, pady=44, padx=44)
        self.quiz = quiz
        self.score_text = Label(text=f"Score: {quiz.score}", bg=BG, fg="white", font=("Franklin Gothic Demi", 12))
        self.score_text.grid(column=1, row=0)
        true_icon = PhotoImage(file="icons/true.png")
        false_icon = PhotoImage(file="icons/false.png")
        self.true = Button(image=true_icon, command=self.is_true, highlightthickness=0)
        self.false = Button(image=false_icon, command=self.is_false, highlightthickness=0)
        self.true.grid(column=0, row=2)
        self.false.grid(column=1, row=2)
        self.canvas = Canvas(width=360, height=280, highlightthickness=0)
        self.canvas.grid(column=0, row=1, padx=17, pady=17, columnspan=2)
        self.question = self.canvas.create_text(180, 140, width=340, font=("Franklin Gothic Book", 18, "italic"))
        self.show_question()
        self.screen.mainloop()

    def show_question(self):
        self.canvas.config(bg="white")
        if self.quiz.question_number < self.quiz.total_questions:
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=question)
        else:
            self.canvas.itemconfig(self.question, text=f"Your final score is {self.quiz.score}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def is_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, result):
        if result:
            self.canvas.config(bg="green")
            self.score_text.config(text=f"Score: {self.quiz.score}", bg=BG, fg="white",
                                   font=("Franklin Gothic Demi", 12))
        elif not result:
            self.canvas.config(bg="red")
        self.screen.after(1300, self.show_question)
