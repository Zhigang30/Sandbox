MIN_PASSWORD_LENGTH = 8


def method_name():
    global get_password

    def get_password():
        while True:
            password = input("Enter your password: ")
            if len(password) >= MIN_PASSWORD_LENGTH:
                return password
            else:
                print("Password is too short. Minimum length is", MIN_PASSWORD_LENGTH)


method_name()

def print_stars(password):
    print("*" * len(password))

def main():
    password = get_password()
    print_stars(password)

if __name__ == "__main__":
    main()
