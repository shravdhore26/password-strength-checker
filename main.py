from utils import check_password_strength

def main():
    password = input("Enter password: ")
    strength = check_password_strength(password)
    print(f"Strength: {strength}")

if __name__ == "__main__":
    main()