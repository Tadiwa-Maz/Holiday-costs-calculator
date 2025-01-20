# This program calculates the total cost of travelliing to either Cape Tow, Durban or PE.

def hotel_cost(num_nights):
    price_per_night = 800
    
    return num_nights * price_per_night
    
    
def plane_cost(plane_cost): 
    if city_flight == "Cape town":
       return 2500
    elif city_flight == "Durban":
        return 3000
    elif city_flight == "Pretoria":
         return 1500
    else:
        return 0 

    
def car_rental(rental_days):
    daily_cost = 300
    
    return rental_days * daily_cost 


# Getiing the inputs from user.
city_flight = input(" Will you be visiting Cape Town, Durban or Pretoria?").title()
num_nights = int(input("How many nights will you be staying there?"))
rental_days = int(input("How many days will you be renting a car?"))

# Calculates the costs.
total_hotel_cost = hotel_cost(num_nights)
total_plane_cost = plane_cost(city_flight)
total_car_rental = car_rental(rental_days)

# Calculates the total holiday cost.
total_holiday_cost = total_hotel_cost + total_plane_cost + total_car_rental

print("\nHoliday Cost Breakdown:")
print(f"Plane cost to {city_flight}: R{total_plane_cost}")
print (f"Hotel cost will be: R{total_hotel_cost}")
print (f"Car renatl cost will be: R{total_car_rental}")

print(f"Therefore the total cost for the holiday will be : R{total_holiday_cost}")

