from client import Client


while(True):
    try:
        user_input = input("% ")
        match user_input.lower().strip():
            case "exit":
                break
            case _:
                # Process the user input here
                print(f"You entered: {user_input}")
    except Exception as e:
        print(f"An error occurred: {e}")