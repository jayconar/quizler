import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.total_questions = len(self.question_list)
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        question = html.unescape(f"Q.{self.question_number}. {self.current_question.text} (True/False): ")
        return question

    def check_answer(self, choice):
        correct_answer = self.current_question.answer
        if choice == correct_answer:
            self.score += 1
            return True
        else:
            return False
