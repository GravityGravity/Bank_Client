from client import Client
import time
import shlex

client = None  # Client login will be stored within REPL file

# Login or Create Account (CREATE/GET)
# Print Clients accounts W/ Balances
# Withdrawal from specific account
# Depost from specific account


# Intro startup
print(r"""
****************************************
*                                      *
*        Bank App (ALPHA)              *
*                                      *
****************************************
""")
time.sleep(1)


while (True):
    try:
        user_input = input("% ")

        # Shlex Parses user input into {commands} {args...}
        if user_input:
            parsed_input = shlex.split(user_input)
            command = parsed_input[0]
            args = parsed_input[1:]

            match command.lower():
                case "exit":  # Close Application
                    break
                case _:
                    # Process the user input here
                    print(f"Entered: '{user_input}'")
    except Exception as e:
        print(f"An error occurred: {e}")


def login():
    return None
