
try:
    exec(open("test.py").read())

except Exception as e:
    error_message = str(e)

    print("Error detected:")
    print(error_message)

    if "not defined" in error_message:
        print("\nExplanation:")
        print("You are using a variable before assigning a value.")

    elif "syntax" in error_message.lower():
        print("\nExplanation:")
        print("There is a syntax mistake. Check brackets or colons.")

    else:
        print("\nExplanation:")
        print("An error occurred. Please check your code.")

