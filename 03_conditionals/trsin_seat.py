seta_type = input("Enter seat type (sleeper/AC/general/luxury): ").lower()

match seta_type:
    case "sleeper":
        print("Sleeper seat selected. Comfortable for long journeys.")
    case "ac":
        print("AC seat selected. Enjoy a cool ride.")
    case "general":
        print("General seat selected. Budget-friendly option.")
    case "luxury":
        print("Luxury seat selected. Experience premium comfort.")
    case _:
        print("Invalid seat type selected. Please choose a valid option.")