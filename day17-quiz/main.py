from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create a list of question objects
question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'],question['answer']))
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You've completed the quiz. \n Your final score was:{quiz.score/quiz.question_number}")