def calculate_sum(n):
    total =0
    for i in range(1, n+1):
        total += i
    return total

def main():
    try:
        num = int(input("Enter a number: "))
        if num < 1:
            print("Please enter the positive number")
        else:
            result = calculate_sum(num)
            print(f"The sum of values from 1 to {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter the valid number")

if __name__ == "__main__":
    main()




