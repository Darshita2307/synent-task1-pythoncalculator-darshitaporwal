def get_operations():
    # Display menu and return the selected opertion symbol
    operations={
        '1':('Addition','+'),
        '2':('Subtraction','-'),
        '3':('Multiplication','*'),
        '4':('Division','/')
    }

    while True:
        for key,(name,symbol) in operations.items():
            print(f"{key}.{name} ({symbol})")
        choice = input("Choose between (1-4): ").strip()
        if choice in operations:
            return operations[choice][1]
        else:
            print("Invalid input. Try again!")    

def get_numbers():
    # Take two or more numbers from the user
    while True:

        num=input("Enter atleast two numbers with spaces between them: ").strip()
        parts=num.split()

        if len(parts)<2:
            print("Please enter atleast 2 numbers.")
            continue

        numbers=[]
        valid=True

        for p in parts:
            try:
                numbers.append(float(p))
            except ValueError:
                print(f" '{p}' is not a valid number.")
                valid=False
                break
        if valid:
            return numbers

def calculate(operations,numbers):
    # Perform the selected operation on the list of numbers
    result=numbers[0]

    for n in numbers[1:]:
        if operations=="+":
            result+=n
        elif operations=="-":
            result-=n
        elif operations=="*":
            result*=n
        elif operations=="/":
            if n==0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result/=n

    return result

def format_result(result):
    # Remove .0 from whole numbers
    if isinstance(result,float) and result.is_integer():
        return str(int(result))
    return str(result)

def main():
    # Main program loop
    print("Welcome to Command Line Integer Calculator ")
    while True:
  
        operations=get_operations()
        numbers=get_numbers()
        try:
            result=calculate(operations,numbers)
            expression =f" {operations} ".join(format_result(n) for n in numbers)
            print(f"\nResult: {expression} = {format_result(result)}")
        except ZeroDivisionError as e:
            print(f"\nError: {e}")

        again = input("\n Do you want another calculation? (y/n): ").strip().lower()

        if again!="y":
            print("\nThank You for using the Calculator!")
            break

if __name__=="__main__":
    main()