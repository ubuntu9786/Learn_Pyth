def translate(phrase):
    translation = ''
    for letter in phrase:
        if letter.lower in "AEIOU":
            if letter.isupper():
                translation = translation = "G"
            else:
                translation = translation + "g"
        elif letter in "ghtk":
            translation = translation + "7"
        else:
            translation = translation + letter
    return translation

print(translate(input('Enter something: ')))