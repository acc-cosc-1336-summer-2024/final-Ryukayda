def create_multiplication_table():
    # Create an empty list to hold the multiplication table
    table = []
    
    # Use nested looping to create the multiplication table
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    
    return table

def display_multiplication_table(table):
    # Loop through the list to display the table
    for row in table:
        print(' '.join(map(str, row)))

def main():
    while True:
        # Call the function to create the multiplication table
        multiplication_table = create_multiplication_table()
        
        # Call the function to display the multiplication table
        display_multiplication_table(multiplication_table)
        
        # Ask the user if they want to continue or quit
        choice = input("Do you want to generate another table? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
