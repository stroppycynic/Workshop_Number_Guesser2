print("""
Instructions: 
Imagine random number from 1 to 1000 and I will try to guess it in max. 10 tries. 
If I guess the number that is smaller than your number, write: "Too small".
If I guess the number that is bigger than your number, write: "Too big".
If I guess correctly, write: "You win" 
""")


def user_input():
    """Return proper value provided by user.

    :rtype: str
    :return: value provided by user from ["Too small", "Too big", "You win"]
    """
    possible_input = ["Too small", "Too big", "You win"]
    while True:
        user_answer = input()
        if user_answer in possible_input:
            break
        print("Answer is not in ['Too small', 'Too big', 'You win']")
    return user_answer


def computer_guess():
    """Main function for our program."""
    print("Imagine random number from 1 to 1000")
    print("Press 'Enter' below to continue")
    input()
    min_number = 1
    max_number = 1000
    user_answer = ""
    while user_answer != "You win":
        guess = int((max_number - min_number) // 2) + min_number
        print(f"I'm guessing your number is: {guess}")
        user_answer = user_input()
        if user_answer == "Too big":
            max_number = guess
            print("I did not guess your number")
        elif user_answer == "Too small":
            min_number = guess
            print("I did not guess your number")
    print("Hurray! I guessed your number!")


if __name__ == '__main__':
    computer_guess()
