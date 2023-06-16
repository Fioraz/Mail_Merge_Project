PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()


with open("./Input/Letters/starting_letter.txt") as letter:
    letter_format = letter.read()
    for name in names_list:
        stripped_name = name.strip("\n")
        new_letter = letter_format.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as updated_letter:
            updated_letter.write(new_letter)

