# symmetric chain

while True:
    my_string = input("Enter a string: ")
    if my_string == my_string[::-1]:
        print(f"'{my_string}' is symmetric")
    else:
        print(f"'{my_string}' is asymmetric")

    answer = input("Do you want to try again? (Y/N): ").upper().lstrip().rstrip()
    if answer != "Y" and answer != "YES":
        print("Bye! See you next time!!!")
        break
