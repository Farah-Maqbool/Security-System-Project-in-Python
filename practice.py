# Question no 1
# crop monitoring system:
def monitor_crop(temperature, humidity, rainfall):
    if humidity < 40 and rainfall < 50:
        return "Watering needed"
    else:
        return "Optimal conditions"

# Sample usage
temperature = 25  # Example temperature in degrees Celsius
humidity = 30     # Example humidity percentage
rainfall = 40     # Example rainfall in millimeters

result = monitor_crop(temperature, humidity, rainfall)
print(result)
# Question no 2
# library book reservation system:
class LibraryBook:
    def __init__(self, title, available):
        self.title = title
        self.available = available

def reserve_book(book_title, student_status):
    """
    Reserves a book based on availability and student status.

    Parameters:
    - book_title (str): Title of the book to be reserved.
    - student_status (str): Student status ("regular" or "VIP").

    Returns:
    - str: Reservation status message.
    """
    # Sample list of library books (You may replace this with your own data structure or database)
    library_books = [
        LibraryBook("Introduction to Python", True),
        LibraryBook("Data Science Essentials", False),
        LibraryBook("Algorithm Design", True),
        # Add more books as needed
    ]

    # Check if the book is in the library
    book_found = False
    for book in library_books:
        if book.title == book_title:
            book_found = True
            if book.available:
                if student_status == "regular":
                    book.available = False
                    return f"Book '{book_title}' reserved successfully for regular student."
                elif student_status == "VIP":
                    return f"Instant reservation granted for VIP student for book '{book_title}'."
                else:
                    return "Invalid student status. Please provide 'regular' or 'VIP'."
            else:
                return f"Book '{book_title}' is currently not available."
    
    if not book_found:
        return f"Book '{book_title}' not found in the library."

# Example usage:
book_title = "Introduction to Python"
student_status_regular = "regular"
student_status_VIP = "VIP"

result_regular = reserve_book(book_title, student_status_regular)
result_VIP = reserve_book(book_title, student_status_VIP)

print(result_regular)
print(result_VIP)
# Question no 3
# ride sharing fare calculator
def calculate_fare(distance, time_of_day):
    """
    Calculates the fare for a ride based on distance and time of day.

    Parameters:
    - distance (float): Distance of the ride in kilometers.
    - time_of_day (int): Time of the ride in 24-hour format (0-23).

    Returns:
    - float: Calculated fare.
    """
    base_fare = 2.5  # Base fare for the ride
    rate_per_km = 1.5  # Fare rate per kilometer

    # Check for peak hours (8 am - 10 am and 5 pm - 7 pm)
    if (8 <= time_of_day <= 10) or (17 <= time_of_day <= 19):
        fare = (base_fare + rate_per_km * distance) * 1.2  # Apply 20% surcharge
    # Check for late-night rides (10 pm - 5 am)
    elif 22 <= time_of_day <= 5:
        fare = (base_fare + rate_per_km * distance) * 0.9  # Apply 10% discount
    else:
        fare = base_fare + rate_per_km * distance  # Regular fare

    return round(fare, 2)  # Round the fare to 2 decimal places

# Example usage:
distance_of_ride = 15.5  # in kilometers
time_of_ride = 18  # 6 pm in 24-hour format

fare = calculate_fare(distance_of_ride, time_of_ride)
print(f"The fare for the ride is ${fare}")
# Question no 4
# health tracker app:
def check_activity_goal(steps_taken, goal):
    """
    Checks if the user has achieved their daily step goal.

    Parameters:
    - steps_taken (int): Number of steps taken by the user.
    - goal (int): Daily step goal.

    Returns:
    - str: Message indicating goal achievement or the number of steps needed.
    """
    if steps_taken >= goal:
        return "Goal achieved"
    else:
        steps_needed = goal - steps_taken
        return f"You need {steps_needed} more steps to reach your goal."

# Example usage:
daily_goal = 10000
user_steps = 8500

result = check_activity_goal(user_steps, daily_goal)
print(result)
# Question no 5
# online shopping cart:
class Membership:
    REGULAR = 'Regular'
    PREMIUM = 'Premium'
    VIP = 'VIP'

def checkout(cart_total, membership_level):
    """
    Calculates the final cost after applying a discount based on the user's membership level.

    Parameters:
    - cart_total (float): Total cost of items in the shopping cart.
    - membership_level (str): User's membership level ('Regular', 'Premium', or 'VIP').

    Returns:
    - float: Final cost after applying the discount.
    """
    regular_discount_rate = 0.05
    premium_discount_rate = 0.10
    vip_discount_rate = 0.15

    if membership_level == Membership.REGULAR:
        discount_rate = regular_discount_rate
    elif membership_level == Membership.PREMIUM:
        discount_rate = premium_discount_rate
    elif membership_level == Membership.VIP:
        discount_rate = vip_discount_rate
    else:
        raise ValueError("Invalid membership level. Please provide 'Regular', 'Premium', or 'VIP'.")

    discounted_cost = cart_total * (1 - discount_rate)
    return round(discounted_cost, 2)  # Round the final cost to 2 decimal places

# Example usage:
total_cost = 150.0
user_membership_level = Membership.VIP

final_cost = checkout(total_cost, user_membership_level)
print(f"The final cost after applying the discount is ${final_cost}")
# Question no 6
# weather app:
def weather_advice(temperature, precipitation):
    """
    Provides weather advice based on temperature and precipitation.

    Parameters:
    - temperature (float): Current temperature in Celsius.
    - precipitation (str): Type of precipitation ('sunny', 'rainy', 'snowy', etc.).

    Returns:
    - str: Weather advice.
    """
    if temperature > 25 and precipitation == 'sunny':
        return "It's hot and sunny. Don't forget to wear sunscreen!"
    elif precipitation == 'rainy':
        return "It's raining. Remember to carry an umbrella."
    elif temperature < 10:
        return "It's cold. Dress warmly."
    else:
        return "Enjoy the weather!"

# Example usage:
current_temperature = 28.0  # in Celsius
current_precipitation = 'sunny'

advice = weather_advice(current_temperature, current_precipitation)
print(advice)