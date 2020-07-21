<<<<<<< HEAD
=======
#In this project we are trying to print each letter out of a word that a user inputs
>>>>>>> origin/master
def indexing(phrase):
    translation = ""
    alphabet = [":", "w", "v", "r", "2", "y", "u", "#", "9", "p", "{", "}", "a", "5", "z", "f", "g", "h", "7", "k", "+",
                ";", "q", "'", "d", "x", "j", "e", "b", "n", "m", "1", "!", "t", "@", "3", "i", "4", "$", "s", "%", "6",
<<<<<<< HEAD
                "^", "c", "&", "8", "*", "o", "(", "0", ")", ",", "<", ".", ">", "/", "?", "-", "_", "=", "l", "", ""]
=======
                "^", "c", "&", "8", "*", "o", "(", "0", ")", ",", "<", ".", ">", "/", "?", "-", "l", "=", "_", "", ""]
>>>>>>> origin/master
    for letter in phrase.lower():
        if letter in alphabet:
            pos = alphabet.index(letter)
            translation = translation + alphabet[pos - 2]
        else:
            translation = translation + letter
    return translation
<<<<<<< HEAD
print(indexing(input("Enter a phrase: ")))


=======
print(indexing(input("Enter a phrase: ")))
>>>>>>> origin/master
