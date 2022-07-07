import random

class InvalidInputError(Exception):
    def __str__(self):
        return "No one is joining for the party"
        
def choose_lucky(friends):
    option = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")
    if option.lower() == "yes":
        lucky = random.choice(friends)
        print(f"{lucky} is the lucky one!")
        return lucky
    print("No one is going to be lucky")
        
def bill_splitter(num):
    print("Enter the name of every friend (including you), each on a new line:\n")
    friends = [input() for _ in range(num)]
    total = int(input("Enter the total bill value:\n"))
    split_value = round(total / len(friends), 2)
    friends_dict = {}
    friends_dict = dict.fromkeys(friends, split_value)
    lucky = choose_lucky(friends)
    if lucky is not None:
        split_value = round(total / (len(friends) - 1), 2)
        friends_dict = dict.fromkeys(friends, split_value)
        friends_dict[f"{lucky}"] = 0
    return friends_dict
        
try:
    num = int(input("Enter the number of friends joining (including you):\n"))
    if num <= 0:
        raise InvalidInputError
    else:
        print(bill_splitter(num))
                
except (InvalidInputError, TypeError) as err:
    print(err)
