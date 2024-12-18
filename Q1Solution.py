def calculate_rental_cost(start_time, end_time):
    if start_time < 0 or end_time < 0 or start_time >= 24 or end_time >= 24:
        return "Invalid input: Time must be in the range 0-24."
    if start_time >= end_time:
        return "Invalid input: Starting time must be less than ending time."
    
    total_cost = 0
    current_time = start_time

    while current_time < end_time:
        if (0 <= current_time < 7) or (21 <= current_time < 24):
            total_cost += 500  # RWF 500 per hour
        elif (7 <= current_time < 10) or (19 <= current_time < 21):
            total_cost += 1000  # RWF 1000 per hour
        elif (10 <= current_time < 19):
            total_cost += 1500  # RWF 1500 per hour

        current_time += 1  # Move to the next hour

    return total_cost

# Input from the user
try:
    start_time = float(input("Enter the starting time (0-24): "))
    end_time = float(input("Enter the ending time (0-24): "))

    cost = calculate_rental_cost(start_time, end_time)
    if isinstance(cost, str):  # If the return is a string, it's an error message
        print(cost)
    else:
        print(f"Total amount to be paid: RWF {cost}")

except ValueError:
    print("Invalid input: Please enter numeric values for time.")


