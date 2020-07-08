#In this project we are trying to print each letter out of a word that a user inputs
def indexing(phrase):
    translation = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for letter in phrase:
        if letter in alphabet:
            pos = alphabet.index(letter)
            if letter == "a" or "b" or "c":
                translation = translation + alphabet[pos + 2]
                print("plus 2 ")
            #if letter in alphabet == "z":
            #    translation = translation + alphabet[pos - 1]
            #else:
             #   translation = translation + alphabet[pos + 1]
            else:
                translation = translation + alphabet[pos + 1]
                print("else ")
        #else:
         #   translation = translation + alphabet
    return translation
print(indexing(input("Enter a phrase: ")))




