#In this project we are trying to print each letter out of a word that a user inputs
def indexing(phrase):
    translation = ""
    alphabet = [":", "w", "v", "r", "2", "y", "u", "#", "9", "p", "{", "}", "a", "5", "z", "f", "g", "h", "7", "k", "+",
                ";", "q", "'", "d", "x", "j", "e", "b", "n", "m", "1", "!", "t", "@", "3", "i", "4", "$", "s", "%", "6",
                "^", "c", "&", "8", "*", "o", "(", "0", ")", ",", "<", ".", ">", "/", "?", "-", "l", "=", "_", "", ""]
    for letter in phrase.lower():
        if letter in alphabet:
            pos = alphabet.index(letter)
            translation = translation + alphabet[pos - 2]
        else:
            translation = translation + letter
    return translation
print(indexing(input("Enter a phrase: ")))