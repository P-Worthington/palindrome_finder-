# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def palindromer(string):
    reverse = []
    string_2 = string.replace(" ", "")
    new_string = string.replace(" ", "")
    for item in new_string:
        reverse_item = new_string[-1:]
        new_string = new_string[:-1]
        reverse.append(reverse_item)
    rev_str = ''.join(str(x) for x in reverse)

    if string_2 == rev_str:
        print(f"'{string}' is a palindrome")
    else:
        print(f"'{string}' is not a palindrome")

def play_again():
    print("would you like to play again? y/n")
    again = input()
    if again == 'y':
        main()
    elif again == 'n':
        exit()
    else:
        print('Unknown input exiting program')
        exit()

def main():
    print('Welcome to palindromer. input a string below and the program will assess if it is a palindrome')
    string = input()
    palindromer(string)
    play_again()

main()