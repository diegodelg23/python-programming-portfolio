def readposint():
    while True:
        try:
            num = int(input("Please enter a positive integer: "))
            if num <= 0:
                print("Your number was not a valid entry")
            else:
                return (num)

        except Exception as e:
            print("Your number was not a valid entry")


readposint()