# Placeholder text in the template that will be replaced with each name
PLACEHOLDER = "[name]"

# Read all invited names from file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read the template letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    # Generate a personalized letter for each name
    for name in names:
        stripped_name = name.strip()  # Remove newline characters from name

        # Replace placeholder with the actual name
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Create a new file for the personalized letter
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)  # Write updated letter to file