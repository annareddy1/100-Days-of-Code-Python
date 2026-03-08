# We are bringing in three things from other files
# Think of this like borrowing toys from other toy boxes

from question_model import Question     # A blueprint to make a question object
from data import question_data          # The list of quiz questions and answers
from quiz_brain import QuizBrain        # The brain that runs the quiz game


# We make an empty basket to store our questions
question_bank = []


# Go through each question inside the big question list
# Imagine opening each card from a stack of flashcards
for question in question_data:

    # Take the question text from the card
    question_text = question["question"]

    # Take the correct answer from the card
    question_answer = question["correct_answer"]

    # Make a new Question object using the text and answer
    # This is like creating a proper question card
    new_question = Question(question_text, question_answer)

    # Put that question card into our basket
    question_bank.append(new_question)


# Now we give all the question cards to the quiz brain
# The quiz brain will control asking questions
quiz = QuizBrain(question_bank)


# Keep asking questions while there are still questions left
# Like a teacher continuing the quiz until cards are finished
while quiz.still_has_questions():

    # Ask the next question
    quiz.next_question()


# When all questions are done, show a message
print("You've completed the quiz")

# Show the player's final score
# quiz.score = how many you got right
# quiz.question_number = how many questions were asked
print(f"Your final score was: {quiz.score}/{quiz.question_number}")