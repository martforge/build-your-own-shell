import os
import subprocess

def main():
    while True:
        # Prompt for user input
        command = input("$ ")

        # Exit condition for 'exit 0'
        if command == 'exit 0':
            break

        # Handle 'type' command: Check if it's a known shell builtin or an external command
        if command.startswith('type '):
            cmd = command[5:].strip()

            # Check if it's a shell builtin
            if cmd in ['echo', 'exit', 'type']:
                print(f"{cmd} is a shell builtin")
            else:
                # Search for the command in directories listed in PATH
                path_dirs = os.environ.get('PATH', '').split(';')  # Use ';' for Windows, ':' for Unix-based systems
                found = False
                for directory in path_dirs:
                    command_path = os.path.join(directory, cmd)

                    if os.path.isfile(command_path) and os.access(command_path, os.X_OK):
                        print(f"{cmd} is {command_path}")
                        found = True
                        break

                if not found:
                    print(f"{cmd}: not found")

        # Handle 'echo' command: Print the rest of the command after 'echo'
        elif command.startswith('echo '):
            print(command[5:])

        # Handle running external commands with arguments
        else:
            # Split the command and its arguments
            parts = command.split()
            cmd = parts[0]
            args = parts[1:]

            # Search for the command in PATH
            path_dirs = os.environ.get('PATH', '').split(';')  # Use ';' for Windows, ':' for Unix-based systems
            found = False
            for directory in path_dirs:
                command_path = os.path.join(directory, cmd)

                if os.path.isfile(command_path) and os.access(command_path, os.X_OK):
                    try:
                        # Execute the command with arguments
                        result = subprocess.run([command_path] + args, capture_output=True, text=True)
                        print(result.stdout.strip())  # Print the output of the command
                        found = True
                        break
                    except Exception as e:
                        print(f"Error executing {cmd}: {e}")
                        found = True
                        break

            if not found:
                print(f"{cmd}: command not found")

if __name__ == "__main__":
    main()
