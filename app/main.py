from config import Config

def main():
    config = Config.from_file()
    print("Hello from main.py")
    print(f"Here is a config: ({config})")

if __name__ == '__main__':
    main()
