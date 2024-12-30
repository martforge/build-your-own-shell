import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()  # Ensure the prompt is displayed immediately

        command = input()
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()