#How to build a basic translator in a python so we can take in a phrase or a word and be able to translate it into a different language
#In our first translation, we will convert each vowel in a word to g
def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": #this can efficiently be typed if letter.lower() in "aeiou"
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))



