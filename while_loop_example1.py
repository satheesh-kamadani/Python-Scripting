def calculate_sum():
    total = 0

    while True:
        try:
            num = int(input("Enter a number (-1 to stop): "))
            if num == -1:
                break
            total += num
        except ValueError:
            print("Invalid input. Please eneter the valid number")

    print(f"sum of the entered numbers is: {total}")

calculate_sum()


