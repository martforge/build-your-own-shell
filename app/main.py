import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Ensure the prompt is displayed immediately

        command = input()

        # Exit condition for 'exit 0'
        if command == 'exit 0':
            break
        
        # Handle 'echo' command: Print the rest of the command after 'echo'
        if command.startswith('echo '):
            # Print the part after 'echo '
            print(command[5:])


        # Handle invalid commands
        else: 
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
