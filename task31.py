''' The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false '''


def generate_hashtag(s):
    new_lst = []

    if len(s) <= 1:
        return False

    lst = str(s).split()

    for i in lst:
        new_lst.append(i.capitalize())

    new_str = ''.join(new_lst)
    if new_str[0] != '#':
        final_str = '#' + new_str

    if len(final_str) > 140:
        return False

    return final_str


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    HELLO     World   "))
print(generate_hashtag(""))
print(generate_hashtag('c i n'))

