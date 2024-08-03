from tkinter import  *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizzinterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.s = 0
        self.score = Label(self.window,text=f"Score : {self.quiz.score}",fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(self.window,bg="white",width=300,height=250)
        self.question = self.canvas.create_text(
            150,125,
            width=200,
            text="some random question ",
            fill=THEME_COLOR,
            font=("Ariel",20,"italic")

        )
        self.canvas.grid(row=1,column=0,columnspan = 2,pady=50)

        correct = PhotoImage(file = "images/true.png")
        self.crct_ans = Button(image=correct,highlightthickness=0,command=self.tick)
        self.crct_ans.grid(row=2,column = 0)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_ans = Button(image=wrong, highlightthickness=0,command=self.cross)
        self.wrong_ans.grid(row=2, column=1)
        self.get_nxt_question()

        self.window.mainloop()
    def get_nxt_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="End of question")
            self.crct_ans.config(state="disabled")
            self.wrong_ans.config(state="disabled")






    def tick(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def cross(self):
        self.give_feedback(self.quiz.check_answer("False"))
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"Score : {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_nxt_question)

