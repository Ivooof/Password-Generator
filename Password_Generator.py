import random
import time
import sys

characters = "abcdefghijklmnñopqrstuvwxyz"
numerical = "1234567890"
symbolic = "°!#$%&/()=?¡¨*[].,-;:_<>¨*"
alfa_numerical = characters+numerical
numerical_symbols = numerical+symbolic
characters_symbols = characters+symbolic
characters_symbols_numerical = characters+symbolic+numerical

while True:
    try:
        print("Welcome to the PASSWORD GENERATOR!.")
        print(""".-MENU-.
        1. Password of CHARACTERS. (Low level).
        2. Numerical password. (Low level).
        3. SYMBOLIC password. (Low level).
        4. Password ALPHA-NUMERIC. (Medium level).
        5. Numerical-SYMBOLS. (Medium level).
        6. CHARACTERS-SYMBOLS. (High level).
        7. CHARACTERS-SYMBOLS-NUMERICS. (High level).
        8. Exit the PROGRAM.""")
        option = int(input("Choose an option from the PREVIOUS MENU:"))
        if option == 1:
            print("You chose Option 1 (Password of CHARACTERS.)")
            length_1 = int(input("Enter the length of your password in CHARACTERS (MAX 27):"))
            print("Generating your PASSWORD...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")
            sample_1 = random.sample(characters, length_1)
            password_1 = "".join(sample_1)
            print(f"Your CHARACTER password is: {password_1}")
            break
        elif option == 2:
            print("You chose Option 2 (numericalL Password.)")
            length_2 = int(input("Enter the length of your NUMERIC password (MAX 10):"))
            print("Generating your PASSWORD...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")
            sample_2 = random.sample(numerical, length_2)
            password_2 = "".join(sample_2)
            print(f"Your NUMERIC password is: {password_2}")
            break
        elif option == 3:
            print("You chose Option 3 (SYMBOLIC Password.)")
            length_3 = int(input("Enter the length of your SYMBOLIC password (MAX 26):"))
            print("Generating your PASSWORD...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))  
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")  
            sample_3 = random.sample(symbolic, length_3)
            password_3 = "".join(sample_3)
            print(f"Your SYMBOLIC password is: {password_3}")
            break
        elif option == 4:
            print("You chose Option 4 (ALPHAnumericalL Password.)")
            length_4 = int(input("Enter the length of your ALPHANUMERIC password (MAX 37):"))
            print("Generating your PASSWORD...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))  
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")  
            sample_4 = random.sample(alfa_numerical, length_4)
            password_4 = "".join(sample_4)
            print(f"Your ALPHANUMERIC password is: {password_4}")
            break
        elif option == 5:
            print("You chose Option 5 (numericalL-SYMBOLS.)")
            length_5 = int(input("Enter the length of your password NUMERIC-SYMBOLS (MAX 36):"))
            print("Generating your PASSWORD...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))  
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")  
            sample_5 = random.sample(numerical_symbols, length_5)
            password_5: "".join(sample_5)
            print(f"SYour NUMBER-SYMBOLS password is: {password_5}")
            break
        elif option == 6:
            print("You chose Option 6 (CHARACTERS-SYMBOLS.)")
            length_6 = int(input("Enter the length of your password from CHARACTERS-SYMBOLS (MAX 53):"))
            print("Generating your PASSWORD...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))  
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")  
            sample_6 = random.sample(characters_symbols, length_6)
            password_6 = "".join(sample_6)
            print(f"Your CHARACTERS-SYMBOLS password is: {password_6}")
            break
        elif option == 7:
            print("You chose Option 7 (CHARACTERS-SYMBOLS-NUMERICS.)")
            length_7 = int(input("Enter the length of your password from CHARACTERS-SYMBOLS-NUMERICS (MAX 63):"))
            print("Generating your PASSWORD...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))  
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")  
            sample_7 = random.sample(characters_symbols_numerical, length_7)
            password_7 = "".join(sample_7)
            print(f"Your CHARACTERS-SYMBOLS-NUMERICS password is: {password_7}")
            break
        elif option == 8:
            print("You chose Option 8 (Exit the PROGRAM.) ")
            break
        else:
            print("Wrong Choice.")

    except:
        print("CHARACTER LENGTH/INVALID OPTION!.")
        break

    finally:
        print("")
        break

while True:
    try:
        option_1 = input("Would you like to generate a new password? (ENTER 'yes' or 'no'):")
        if option_1 == "Yes" or option_1 == "yEs" or option_1 == "YES" or option_1 == "yES" or option_1 == "yeS" or option_1 == "YEs":
            print(""".-MENU-.
        1. Password of CHARACTERS. (Low level).
        2. Numerical password. (Low level).
        3. SYMBOLIC password. (Low level).
        4. Password ALPHA-NUMERIC. (Medium level).
        5. Numerical-SYMBOLS. (Medium level).
        6. CHARACTERS-SYMBOLS. (High level).
        7. CHARACTERS-SYMBOLS-NUMERICS. (High level).
        8. Exit the PROGRAM.""")
            option = int(input("Choose an option from the PREVIOUS MENU:"))
            if option == 1:
                print("You chose Option 1 (Password of CHARACTERS.)")
                length_11 = int(input("Enter the length of your password in CHARACTERS (MAX 27):"))
                print("Generating your PASSWORD...")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1))  
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                sample_11 = random.sample(characters, length_11)
                password_11 = "".join(sample_11)
                print(f"Your CHARACTER password is: {password_1}")
            elif option == 2:
                print("You chose Option 2 (numericalL Password.)")
                length_22 = int(input("Enter the length of your NUMERIC password (MAX 10):"))
                print("Generating your PASSWORD...")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1))  
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                sample_22 = random.sample(numerical, length_22)
                password_22 = "".join(sample_22)
                print(f"Your NUMERIC password is: {password_22}")
            elif option == 3:
                print("You chose Option 3 (SYMBOLIC Password.)")
                length_33 = int(input("Enter the length of your SYMBOLIC password (MAX 26):"))
                print("Generating your PASSWORD...")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1))  
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                sample_33 = random.sample(symbolic, length_33)
                password_33 = "".join(sample_33)
                print(f"Your SYMBOLIC password is: {password_33}")
            elif option == 4:
                print("You chose Option 4 (ALPHA-Numerical Password.)")
                length_44 = int(input("Enter the length of your ALPHANUMERIC password (MAX 37):"))
                print("Generating your PASSWORD...")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1)) 
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                sample_44 = random.sample(alfa_numerical, length_44)
                password_44 = "".join(sample_44)
                print(f"Your ALPHA-NUMERIC password is: {password_44}")
            elif option == 5:
                print("You chose Option 5 (NUMERICAL-SYMBOLS.)")
                length_55 = int(input("Enter the length of your password NUMERIC-SYMBOLS (MAX 36):"))
                print("Generating your PASSWORD...")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1))  
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                sample_55 = random.sample(numerical_symbols, length_55)
                password_55: "".join(sample_55)
                print(f"Your NUMBER-SYMBOLS password is: {password_55}")
            elif option == 6:
                print("You chose Option 6 (CHARACTERS-SYMBOLS.)")
                length_66 = int(input("Enter the length of your password from CHARACTERS-SYMBOLS (MAX 53):"))
                print("Generating your PASSWORD...")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1))  
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                sample_66 = random.sample(characters_symbols, length_66)
                password_66 = "".join(sample_66)
                print(f"Your CHARACTERS-SYMBOLS password is: {password_66}")
            elif option == 7:
                print("You chose Option 7 (CHARACTERS-SYMBOLS-NUMERICS.)")
                length_77 = int(input("Enter the length of your password from CHARACTERS-SYMBOLS-NUMERICS (MAX 63):"))
                print("Generating your PASSWORD...")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1)) 
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                sample_77 = random.sample(characters_symbols_numerical, length_77)
                password_77 = "".join(sample_77)
                print(f"Your CHARACTERS-SYMBOLS-NUMERICS password is: {password_77}")
            elif option == 8:
                print("You chose Option 8 (Exit the PROGRAM.)")
                print("Wrong Choice.")
                toolbar_width = 40
                sys.stdout.write("[%s]" % (" " * toolbar_width))
                sys.stdout.flush()
                sys.stdout.write("\b" * (toolbar_width + 1))  
                for i in range(toolbar_width):
                    time.sleep(0.1)
                    sys.stdout.write("-")
                    sys.stdout.flush()
                sys.stdout.write("]\n")  
                break
            else:
                print("Wrong Choice.")
        elif option_1 == "No" or "no" or "nO" or "NO":
            print("Perfect!.")
            print("Leaving the PROGRAM...")
            toolbar_width = 40
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            sys.stdout.flush()
            sys.stdout.write("\b" * (toolbar_width + 1))
            for i in range(toolbar_width):
                time.sleep(0.1)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")
            break
        else:
            print("Wrong Choice.")
    except:
        print("CHARACTER LENGTH/INVALID OPTION!.")


print("Have a nice Day!.")