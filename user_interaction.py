#!/usr/bin/env python3

class User_Interaction:

    #user request choice
    def request_menu(self, choice=None):
        print(); print("-"*40); print()
        #model generates the code according to user description
        print("1.  Generate Raw Code")
        print(f"\tRequest model for code according to a description you provide.")
        #upload script instead of the model generating the code
        print("2.  Load Raw Code Script From File")
        print("3.  Add Argparse")
        print("4.  Exception Handling and Logging")
        print("5.  Add Unit Test Cases")
        print("6.  Run Unit Test Cases")
        print("7.  User Custom Request")
        print(f"\tYour custom request to the model. Requirement: code to be already loaded. A JSON file to request "
              f"the format of the response.")
        print("8.  Run Program With Enter Debug/Logs Loop")
        print(f"\tRun the program and upon errors send the log error captured for the model to amend the code "
              f"accordingly.")
        print("9.  Add Docstrings To Program Code.")
        print("10. Set Menu Sequence")
        print("11. Run All")
        print("12. Exit")

        while True:
            print()
            if choice is None:
                choice = input("Choose your request: ")
            else:
                print("Choose your request: ", choice)

            match choice:
                case _:
                    if choice.isdigit() and 1 <= int(choice) <= 12:
                        return choice
                    else:
                        print(); print(f"\033[41mInvalid Option\033[0m")

    def broken_json_user_action(self):
        while True:
            user_choice = input("The model's JSON response is broken, re-request? y/n: ")
            match user_choice.lower():
                case 'y':
                    return True
                case 'n':
                    return False
                case _:
                    print("Invalid selection.")
                    continue

    def request_input_from_user(self, mssg):
        return input(mssg)

    def user_choice_two_options(self, mssg, option1="y", option2="n", mssg_option1=None, mssg_option2=None, mssg_option3=None):
        while True:
            choice = input(mssg)
            match choice.lower():
                case option1 if 1 == 1:
                    if mssg_option1 is not None:
                        print(mssg_option1)
                        break
                case option2 if 1 == 1:
                    if mssg_option2 is not None:
                        print(mssg_option2)
                        break
                case _:
                    if mssg_option3 is not None:
                        print(mssg_option3)
                        continue
            return choice.lower()


def broken_json_user_action():
    return None