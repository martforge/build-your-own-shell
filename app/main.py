def main():
    while True:
        command = input("$ ")

        # Exit condition for 'exit 0'
        if command == 'exit 0':
            break
        
        # Handle 'type' command: Check if it's a known builtin
        if command.startswith('type '):
            cmd = command[5:].strip()
            if cmd in ['echo', 'exit', 'type']:
                print(f"{cmd} is a shell builtin")
            else:
                print(f"{cmd}: not found")
        
        # Handle 'echo' command
        elif command.startswith('echo '):
            print(command[5:])
        
        # Handle invalid commands
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
