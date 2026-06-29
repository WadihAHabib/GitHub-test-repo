def check_weather(city):  # Defines a function that accepts a city as a parameter
    if city=="":
        print("Please provide a city name.")  
        return  
    


    print("Checking weather for", city)  # Displays a message indicating which city's weather is being checked


     # print("Weather data will appear here.") # Indicates where weather information will eventually be displayed

    print("Connecting to weather service...") # Updated message from above


check_weather("Paris")  # Calls the function and passes "Paris" as the city
