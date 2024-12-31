import random

def generate_secret_code(name):
    # Generate a mock secret code based on the length of the name
    random.seed(len(name))  # Ensure consistency for each name
    return random.randint(1000000000, 9999999999)  # 10-digit secret code

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
        
        # Handle 'generate secret' command
        elif command.startswith('generate secret '):
            name = command[16:].strip()
            secret_code = generate_secret_code(name)
            print(f"Hello {name}! The secret code is {secret_code}.")
        
        # Handle invalid commands
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
