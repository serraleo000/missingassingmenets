#firstly defines the function checker which divides the interger by 2 and 3 and depending on if it can do one both or neither it returns that
def checker(number):
    if number % 2 == 0 and number % 3 == 0:
        return "divisible by both"
    elif number % 2 == 0:
        return "divisible by 2"
    elif number % 3 == 0:
        return "divisible by 3"
    else:
        return "not divisible by either"
#calls the earlier function and inputs every number and loops until it gets done and also spaces it out
def print_table(number):
    for i in range(1, number + 1):
        print(f"{i:<15}{checker(i):<35}")
number = int(input("enter a upper limit pls "))
#this is part i got help from the internet on, the ":<35" are the spacers.
print(f"{'number':<15}{'type':<35}")
print_table(number)
