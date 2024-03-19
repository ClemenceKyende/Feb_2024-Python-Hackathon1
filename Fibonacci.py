# Function to generate Fibonacci sequence up to term n
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize with the first two terms
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fibonacci_sequence
    else:
        for i in range(2, n):
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)
        return fibonacci_sequence

# Main function
def main():
    # Task 1: Generate Fibonacci sequence
    try:
        n = int(input("Enter the number of terms for Fibonacci sequence: "))
        fibonacci_sequence = generate_fibonacci(n)
        print("Fibonacci sequence up to term {}:".format(n), fibonacci_sequence)
    except ValueError:
        print("Please enter a valid integer.")

    # Task 2: Check eligibility to vote
    try:
        age = int(input("\nEnter your age: "))
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Please enter a valid age.")

if __name__ == "__main__":
    main()
