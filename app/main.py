import os

def main():
    while True:
        command = input("$ ")

        # Exit condition for 'exit 0'
        if command == 'exit 0':
            break
        
        # Handle 'type' command: Check if it's a known builtin
        if command.startswith('type '):
            cmd = command[5:].strip()
            
            # Check if it's a shell builtin
            if cmd in ['echo', 'exit', 'type']:
                print(f"{cmd} is a shell builtin")
            else:
                # Get PATH from environment variable
                path_dirs = os.environ.get('PATH', '').split(os.pathsep)  # Use the system-specific separator for PATH
                
                print(f"Debug: Searching in directories: {path_dirs}")  # Debugging line to check PATH

                found = False
                for directory in path_dirs:
                    command_path = os.path.join(directory, cmd)
                    print(f"Debug: Checking {command_path}")  # Debugging line to check the command path
                    
                    if os.path.isfile(command_path) and os.access(command_path, os.X_OK):
                        print(f"{cmd} is {command_path}")
                        found = True
                        break

                if not found:
                    print(f"{cmd}: not found")
        
        # Handle 'echo' command: Print the rest of the command after 'echo'
        elif command.startswith('echo '):
            print(command[5:])
        
        # Handle invalid commands
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
