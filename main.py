from utils import check_password_strength, suggest_password

def main():
    password = input("Enter password: ")

    strength = check_password_strength(password)
    print(f"Strength: {strength}")

    if strength == "Weak":
        print("\nSuggestions:")
        for s in suggest_password(password):
            print("-", s)

if __name__ == "__main__":
    main()