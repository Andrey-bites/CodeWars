""" Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior" """


def to_camel_case(text):
    for i in text:
        if i == '-':
            text = text.replace(i, ' ')
        else:
            if i == '_':
                text = text.replace(i, ' ')

    if text[0] == text[0].upper():
        text = text.title()
    else:
        if text[0] == text[0].lower():
            leter = text[0]
            text = text.title()
            text = text.replace(text[0], leter)

    text = text.replace(' ', '')

    return text


print(to_camel_case('the-stealth-warrior'))
