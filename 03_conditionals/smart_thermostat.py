device_status = "active"
temprature = 38

if device_status == "active":
    if temprature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is within the safe range.")    
else:
    print("Device is offline. Please turn it on to proceed.")