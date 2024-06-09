import time
import random
from pynput.keyboard import Controller

# Function to generate a random 4-digit code
def generate_code():
    return str(random.randint(1000, 9999))

# Function to type the code with a delay between each digit
def type_code(code):
    keyboard = Controller()
    for char in code:
        print(f"Typing Digit")
        keyboard.type(char)
        time.sleep(1)  # Adding a 1-second delay between each character

# Main function
def main():
    print("Running Screentime Password...")

    # Wait for 5 seconds before generating and typing the code
    time.sleep(5)

    code = generate_code()  # Generate the random 4-digit code

    # Type the code for the first time
    print("Typing in Code 1/2")
    type_code(code)

    # Wait for another 5 seconds
    time.sleep(5)

    # Type the code for the second time
    print("Typing in Code 2/2")
    type_code(code)

    # Write the code to a text file
    with open("Screen Time Passcode.txt", "w") as file:
        file.write(code)

    print("Code has been saved to 'Screen Time Passcode.txt'.")

if __name__ == "__main__":
    main()
