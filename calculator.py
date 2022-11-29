#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: Nov 29,2022
# This program asks the user for three parameters: a sign(operation)
# and two numbers as a float.It then calculates the results
# using a separate function.

# calculates the result of two numbers
def calculate(sign, number_1, number_2):

    if sign == "/":
        result = number_1 / number_2
    elif sign == "*":
        result = number_1 * number_2
    elif sign == "%":
        result = number_1 % number_2
    elif sign == "+":
        result = number_1 + number_2
    else:
        result = number_1 - number_2
    return result


# checks for invalid input and calls
# function to determine result of two numbers
def main():

    # displays opening message
    print("This program will perform calculations between two numbers!")
    print("")

    # gets operation from user
    sign_user = input("Enter the operation you want to perform " "(-, *, %, /, +): ")

    # checks if invalid operator is entered
    if (
        sign_user == "-"
        or sign_user == "%"
        or sign_user == "*"
        or sign_user == "/"
        or sign_user == "+"
    ):
        # gets first number from user
        first_num_string = input("Enter the first number: ")

        try:
            # converts input value to float
            first_num_float = float(first_num_string)

            # gets second number from user
            second_num_string = input("Enter the second number: ")

            try:
                # converts input values to float
                second_num_float = float(second_num_string)

                # assigns variable to function call that gives return value
                result_user = calculate(sign_user, first_num_float, second_num_float)

                # display results to user
                print(
                    "The result of {} {} {} is {}".format(
                        first_num_float, sign_user, second_num_float, result_user
                    )
                )

            # catches any entered strings
            except Exception:
                print("{} is not a valid number.".format(second_num_string))

        # catches any entered strings
        except Exception:
            print("{} is not a valid number.".format(first_num_string))

    else:
        print("Error. {} is not a recognized operation.".format(sign_user))


if __name__ == "__main__":
    main()
