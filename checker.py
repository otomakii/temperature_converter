def temperature_checker(min_value):
    error = "Please enter a number that is more than {}".format(min_value)

    try:
        response = float(input("Choose a numer: "))

        if response < min_value:
            print(error)
        else:
            return response

    except ValueError:
        print(error)


while True:
    to_check = temperature_checker(-459)
    print("success")
