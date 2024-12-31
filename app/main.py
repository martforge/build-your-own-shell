import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Ensure the prompt is displayed immediately

        command = input()

        # Debugging: Log the received command
        print(f"DEBUG: Received command: {command}")  # Debug log

        # Exit condition for 'exit 0'
        if command == 'exit 0':
            print("DEBUG: Exiting program.")  # Debug log
            break

        # Handle invalid commands
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()