print("Main Menu")
a = "1"
print("1. Book Ride")
b = "2"
print("2. Exit")

val = input("Enter your choice: ")



if val == "1":
    print("1. Auto")
    print("2.Sedan")
    print("3. SUV")

    if val == "1":
        vehicle = input("Enter your vehicle choice: ")
        if vehicle == "1":
            print("You have selected Auto")
            print("Choose your Pickup Location:")
            print("1.Pune Station")
            print("2. Swargate")
            print("3. Hinjawadi")
            source = input("Enter your pickup location : ")
            if source == "1":
                print("You have selected Pune Station")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            elif source == "2":
                print("You have selected Swargate")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
        
            elif source == "3":
                print("You have selected Hinjawadi")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            else:
                print("Invalid Pickup Location Choice")

            destination = input("Enter your drop location : ")
            if destination == "1":
                    print("You have selected Shivaji Nagar")  
                    distance = 5
                    rate = 12

            elif destination == "2":
                    print("You have selected Kothrud")
                    distance = 8
                    rate = 12
            elif destination == "3":
                    print("You have selected Wakad")
                    distance = 10
                    rate = 12
            else:
                    print("Invalid Drop Location Choice")

            fare = distance * rate
            print("Your fare is: ", fare)


        elif vehicle == "2":
            print("You have selected Sedan")
            print("Choose your Pickup Location:")
            print("1.Pune Station")
            print("2. Swargate")
            print("3. Hinjawadi")
            source = input("Enter your pickup location : ")
            if source == "1":
                print("You have selected Pune Station")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            elif source == "2":
                print("You have selected Swargate")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            elif source == "3":
                print("You have selected Hinjawadi")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            destination = input("Enter your drop location : ")
            if destination == "1":
                    print("You have selected Shivaji Nagar")
                    distance = 5
                    rate = 18
            elif destination == "2":
                    print("You have selected Kothrud")
                    distance = 8
                    rate = 18
            elif destination == "3":
                    print("You have selected Wakad")
                    distance = 10
                    rate = 18
        
            else:
                    print("Invalid Drop Location Choice")
                
            fare = distance * rate
            print("Your fare is: ", fare)
        
        elif vehicle == "3":
            print("You have selected SUV")
            print("Choose your Pickup Location:")
            print("1.Pune Station")
            print("2. Swargate")
            print("3. Hinjawadi")
            source = input("Enter your pickup location : ")
            if source == "1":
                print("You have selected Pune Station")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            elif source == "2":
                print("You have selected Swargate")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            elif source == "3":
                print("You have selected Hinjawadi")
                print("Choose your Drop Location:")
                print("1. Shivaji Nagar")
                print("2. Kothrud")
                print("3. Wakad")
            destination = input("Enter your drop location : ")
            if destination == "1":
                print("You have selected Shivaji Nagar")
                distance = 5   
                rate = 25         
            elif destination == "2":
                print("You have selected Kothrud")
                distance = 8    
                rate = 25
            elif destination == "3":
                print("You have selected Wakad")
                distance = 10   
                rate = 25
            else:
                print("Invalid Drop Location Choice")

            fare = distance * rate
            print("Your fare is: ", fare)
        
        else:
            print("Invalid Vehicle Choice")


    else:
        print("Invalid Choice")


else:
    print("Exiting the program")
