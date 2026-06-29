def check_weather(city, unit):  # Defines a function that accepts a city as a parameter
    if city=="":
        print("Please provide a city name.")  
        return  
    


    print("Checking weather for", city)  # Displays a message indicating which city's weather is being checked

    print("Temperature unit:", unit)  # Displays the temperature unit being used (Celsius or Fahrenheit)


     # print("Weather data will appear here.") # Indicates where weather information will eventually be displayed

    print("Connecting to weather service...") # Updated message from above


check_weather("Paris" , "Celsius")  # Calls the function and passes "Paris" as the city and "Celsius" as the temperature unit
