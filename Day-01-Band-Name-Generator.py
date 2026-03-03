# Print a welcome message to the user
print("Welcome to the Band Name Generator!")

# Ask the user which city they grew up in
# The \n ensures the cursor moves to the next line
city = input("Which city did you grow up in?\n")

# Ask the user for their pet's name
pet = input("What is the name of a pet?\n")

# Combine city and pet name with a space in between
band_name = city + " " + pet

# Display the final band name
print("Your band name could be " + band_name)