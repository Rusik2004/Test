def computepay(hours, rate):
    if hours > 40:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * rate
    return total_pay
try:
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly rate: "))

    if hours < 0 or rate < 0:
        print("Hours and rate must be non-negative.")
    else:
        pay = computepay(hours, rate)
        print(f"Salary: {pay:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for hours and rate.")
