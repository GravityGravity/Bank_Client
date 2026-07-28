from client import Client
# Main list of clients is automatically read in during program initlization
from client_list import Main_list
import time
import shlex

client: Client = None  # Client login will be stored within REPL file

# Login or Create Account (CREATE/GET)
# Print Clients accounts W/ Balances
# Withdrawal from specific account
# Depost from specific account


# Command List:
# ----INITIAL STARTUP-----
# CREATE {ACCOUNT NUMBER INT} - create a new client
# LOGIN {CLIENT ID OR F_NAME L_NAME} - login as an existing client

# ----ONCE LOGGED IN-----
# ACCOUNTS / LIST / LS / BALANCES- print list of accounts with balances
# CREATE ACCOUNT {ACCOUNT NUMBER}
# WITHDRAWAL {ACCOUNT NUMBER} {AMOUNT}
# DEPOSIT {ACCOUNT NUMBER} {AMOUNT}
# INFO - prints clients information F_name, L_name, client_ID

# Intro startup
print(r"""
****************************************
*                                      *
*        Bank App (ALPHA)              *
*                                      *
****************************************
""")
time.sleep(1)


def REPL():

    while (True):
        try:
            if client == None:
                client_initiation()

            user_input = input(f"{client.f_name}-{client.user_id}% ")

            # Shlex Parses user input into {commands} {args...}
            if user_input:
                parsed_input = shlex.split(user_input)
                command = parsed_input[0]
                args = parsed_input[1:]

                match command.lower():
                    case "exit":  # Close Application
                        break
                    case "help":
                        show_help()
                    case _:
                        # Process the user input here
                        print(f"Entered: '{user_input}'")

        except Exception as e:
            print(f"An error occurred: {e}")


def client_initiation():  # Initial login that requests client to login or create an account

    while (True):
        try:
            user_input = input(
                "LOGIN OR CREATE AN ACCOUNT (Commands list type 'Help')% ")

            # Shlex Parses user input into {commands} {args...}
            if user_input:
                parsed_input = shlex.split(user_input)
                command = parsed_input[0]
                args = parsed_input[1:]

                match command.lower():
                    case "exit":  # Close Application
                        break
                    case "help":
                        show_help()
                    case "create":
                        REPL_create(args)
                        break
                    case "login":
                        REPL_login(args)
                        break
                    case _:
                        # Process the user input here
                        print(f"Entered: '{user_input}'")

        except Exception as e:
            print(f"~! An error occurred: {e}")

    return None

# Functions implement REPL command functionality


def REPL_login(args):  # REPL command LOGIN to login in as an existing client
    if len(args) == 1:
        Main_list.get_client_by_id(int(args[1]))
    else:
        print(
            r"~! LOGIN, Too many arguments.  Type 'Help' for command structure~")
        return None


def REPL_create(args) -> int:  # REPL command CREATE to create a new client account
    #! Most likely will need to add more error checks

    print(*args)

    if len(args) != 3:
        print(
            r"~! CREATE commands arguments error.  Type 'Help' for command structure~")
        return 0

    # Creates new client object
    try:
        args[2] = int(args[2])
        global client
        client = Client(*args)
        return 1
    except Exception as e:
        print(f"~! An error occurred: {e}")
        return 0


def show_help():
    print("""
    Commands
    --------

    ----Startup:----
    CREATE <First Name> <Last Name> <Client ID>
    LOGIN <client_id | first_name last_name>

    ----Logged In:----
    ACCOUNTS | LIST | LS | BALANCES
    CREATE ACCOUNT <account_number>
    WITHDRAWAL <account_number> <amount>
    DEPOSIT <account_number> <amount>
    INFO

    ----Other:-----
    HELP
    EXIT
    """)


REPL()  # Program Initlization

print("""
========================
 Thank you for using
      Team 2s App
      Goodbye!
========================
""")
