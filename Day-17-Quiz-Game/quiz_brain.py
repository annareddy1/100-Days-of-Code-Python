class QuizBrain:

    # Runs when we create the QuizBrain object
    def __init__(self, q_list):
        self.question_number = 0      # Keeps track of which question we are on
        self.score = 0                # Stores how many answers are correct
        self.question_list = q_list   # List containing all Question objects


    # Check if there are still questions left to ask
    def still_has_questions(self):
        return self.question_number < len(self.question_list)


    # Ask the next question to the user
    def next_question(self):

        # Get the current question from the list
        current_question = self.question_list[self.question_number]

        # Move to the next question number
        self.question_number += 1

        # Ask the user for an answer
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False): "
        )

        # Check if the user's answer is correct
        self.check_answer(user_answer, current_question.answer)


    # Compare the user's answer with the correct answer
    def check_answer(self, user_answer, correct_answer):

        # Convert both answers to lowercase to avoid case issues
        if user_answer.lower() == correct_answer.lower():

            # Increase score if correct
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong.")

        # Show correct answer
        print(f"The correct answer was: {correct_answer}.")

        # Show current score
        print(f"Your current score is: {self.score}/{self.question_number}")

        # Print empty line for spacing
        print("\n")