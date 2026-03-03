# TODO-1:
# Bring the logo from art.py so we can show it
import art

# Show the logo when the program starts
print(art.logo)

# This is our alphabet list (like ABC letters in order)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# This function moves letters left or right
def caesar(original_text, shift_amount, encode_or_decode):
    # This will store the new secret message
    output_text = ""

    # If we are decoding, move letters backwards
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Look at each letter one by one
    for letter in original_text:

        # TODO-2:
        # If it's NOT a letter (like 3, !, space),
        # just keep it the same
        if letter not in alphabet:
            output_text += letter
        else:
            # Find where the letter is
            shifted_position = alphabet.index(letter) + shift_amount

            # Wrap around if we go past z
            shifted_position %= len(alphabet)

            # Add new shifted letter
            output_text += alphabet[shifted_position]

    # Show the final message
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3:
# This helps us run the program again and again
should_continue = True

while should_continue:

    # Ask if we want to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Ask for the message
    text = input("Type your message:\n").lower()

    # Ask how many steps to move
    shift = int(input("Type the shift number:\n"))

    # Call the function to do the work
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if we want to restart
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    # If user says no, stop the loop
    if restart == "no":
        should_continue = False
        print("Goodbye")