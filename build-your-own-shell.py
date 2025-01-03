import subprocess
import os
import shutil  # Import shutil module

def main():
    while True:
        command = input("$ ").strip()

        # Exit condition for 'exit 0'
        if command == 'exit 0':
            break
        
        # Handle 'type' command: Check if it's a known builtin or an external program
        if command.startswith('type '):
            cmd = command[5:].strip()
            if cmd in ['echo', 'exit', 'type']:
                print(f"{cmd} is a shell builtin")
            else:
                # Check if the command is in the system's PATH
                program_path = shutil.which(cmd)
                if program_path:
                    print(f"{cmd} is {program_path}")
                else:
                    print(f"{cmd}: not found")
        
        # Handle 'echo' command
        elif command.startswith('echo '):
            print(command[5:])
        
        # Handle external programs
        else:
            # Split the command into program and arguments
            parts = command.split()
            program = parts[0]
            arguments = parts[1:]

            try:
                # Run the external program with arguments
                result = subprocess.run([program] + arguments, capture_output=True, text=True)
                
                # Check if there is output and print it
                if result.stdout:
                    print(result.stdout.strip())
                
                # Check if there was an error and print it
                if result.stderr:
                    print(result.stderr.strip())
            
            except FileNotFoundError:
                print(f"{program}: command not found")
            except Exception as e:
                print(f"Error executing {program}: {e}")

if __name__ == "__main__":
    main()
