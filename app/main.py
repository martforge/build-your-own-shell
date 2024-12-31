import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Ensure the prompt is displayed immediately

        command = input()

        # Exit condition for 'exit 0'
        if command == 'exit 0':
            break

        # Handle invalid commands
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
