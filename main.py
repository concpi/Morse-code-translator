morse_list = [" ", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
              "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
              ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
              ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..",
              "----.", "-----"]

alpha_list = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
              "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

string_list = []
translated_list = []
char_id = None

# Saving user input as Uppercase string
text = input("Text to translate: ").upper()

# Making a list of characters from inputted string
for letter in text:
    string_list.append(letter)

# Comparing every character from input to my list of known characters
for char in string_list:
    for x in range(len(alpha_list)):
        # If character exists in my list, save id of position in list.
        if char == alpha_list[x]:
            char_id = x
            # Using position id, append morse code character to a new list
            translated_list.append(morse_list[char_id])

# Create a new string from a list of translated morse code characters, split by " / "
translated = " / ".join(translated_list)
print(translated)
