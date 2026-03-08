class Question:

    # This runs when we create a new Question object
    def __init__(self, q_text, q_answer):

        # Save the question text (the question we will ask)
        self.text = q_text

        # Save the correct answer to that question
        self.answer = q_answer