import string
#defines the function, function works by first setting two variables, a list and a placeholder var, if a letter is new it adds it to the lettercount if it is not it ADDS one to that letter and either eay adds it to letter count
def analyzetext(text):
    lettercount = {}
    totalletters = 0
    for char in text:
        if char.lower() in string.ascii_lowercase:
            charlower = char.lower()
            if charlower not in lettercount:
                lettercount[charlower] = 1
            else:
                lettercount[charlower] = lettercount[charlower] + 1
            totalletters = totalletters + 1

    #makes histogram by adding a * by freq or how many times its found in the lettercount list
    choice = input("choose display type: 'histogram' or 'percentages': ")
    if choice.lower() == 'histogram':
        for letter, freq in lettercount.items():
            print(f"{letter}: {'*' * freq}")
    elif choice.lower() == 'percentages':
        for letter, count in lettercount.items():
            freq = (count / totalletters) * 100
            print(letter + ": " + str(round(freq, 1)) + "%")
        #First command counts how many words using the .split which sees how many spaces and the other just counts how many characters

    wordcount = len(text.split())
    charcount = len(text)
    print(f"word count:{wordcount}")
    print(f"character count:{charcount}")
#prints using f format

text = input("enter text to analyze:")
analyzetext(text)
