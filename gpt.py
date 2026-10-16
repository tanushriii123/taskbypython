
import random

# Predefined cab rates
cab_rates = {
    "1": 12,  # Auto
    "2": 18,  # Sedan
    "3": 25   # SUV
}

# Predefined route distances (in km)
route_distances = {
    "1": 5,   # Shivaji Nagar
    "2": 8,   # Kothrud
    "3": 10   # Wakad
}

pickup_locations = {
    "1": "Pune Station",
    "2": "Swargate",
    "3": "Hinjawadi"
}

drop_locations = {
    "1": "Shivaji Nagar",
    "2": "Kothrud",
    "3": "Wakad"
}

cab_names = {
    "1": "Auto",
    "2": "Sedan",
    "3": "SUV"
}

# Infinite loop
while True:

    print("\n===== MAIN MENU =====")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    # Exit condition
    if choice == "2":
        print("Thank you for using our cab service!")
        break

    elif choice == "1":

        # Cab selection
        print("\nChoose your cab:")
        print("1. Auto")
        print("2. Sedan")
        print("3. SUV")

        vehicle = input("Enter your cab choice: ")

        if vehicle not in cab_rates:
            print("Invalid cab choice. Please try again.")
            continue

        print("You selected:", cab_names[vehicle])

        # Pickup location
        print("\nChoose your pickup location:")

        for key, value in pickup_locations.items():
            print(key + ".", value)

        source = input("Enter your pickup choice: ")

        if source not in pickup_locations:
            print("Invalid pickup location.")
            continue

        print("Pickup:", pickup_locations[source])

        # Drop location
        print("\nChoose your drop location:")

        for key, value in drop_locations.items():
            print(key + ".", value)

        destination = input("Enter your drop choice: ")

        if destination not in drop_locations:
            print("Invalid drop location.")
            continue

        print("Drop:", drop_locations[destination])

        # Calculate fare
        distance = route_distances[destination]
        rate = cab_rates[vehicle]
        fare = distance * rate

        print("\n===== RIDE DETAILS =====")
        print("Cab:", cab_names[vehicle])
        print("Pickup:", pickup_locations[source])
        print("Drop:", drop_locations[destination])
        print("Distance:", distance, "km")
        print("Rate per km: Rs.", rate)
        print("Total fare: Rs.", fare)

        # Cancellation is allowed BEFORE OTP sharing
        cancel = input(
            "\nDo you want to cancel the ride before OTP sharing? (yes/no): "
        ).lower()

        if cancel == "yes":
            print("Ride cancelled successfully.")
            continue

        elif cancel != "no":
            print("Invalid choice. Ride booking cancelled.")
            continue

        # OTP is shared only after cancellation decision
        otp = random.randint(1000, 9999)

        print("\nYour OTP is:", otp)
        print("OTP shared successfully.")
        print("Cancellation is not allowed after OTP sharing.")

        # OTP verification
        entered_otp = input("Enter OTP to confirm your ride: ")

        if entered_otp == str(otp):
            print("OTP verified successfully!")
            print("Your ride is confirmed.")
            print("Have a safe journey!")
        else:
            print("Incorrect OTP.")
            print("Ride confirmation failed.")

    else:
        print("Invalid menu choice. Please select 1 or 2.")
