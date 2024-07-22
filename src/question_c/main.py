def main():
    # Initialize an empty list to store the numbers
    numbers = []
    
    # Prompt the user to enter 5 numbers
    for i in range(5):
        while True:
            try:
                num = float(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    # Calculate the required data
    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    # Display the results
    print(f"\nNumbers entered: {numbers}")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of numbers: {total}")
    print(f"Average of numbers: {average}")

if __name__ == "__main__":
    main()
