import math 

def windchill(t : int , v : int) -> float:
    wind_chill = 35.74 + (0.6215 * t) + ((0.4275 * t) - 35.75) * pow(v , 0.16)
    return wind_chill

def main():
    try:
        t = float(input("Enter temperature (in Fahrenheit): "))
        v = float(input("Enter wind speed (in miles per hour): ")) 

        if t > 50 and 3 < v < 120:
            print("Give the proper values")

        else:
            wind_chill = windchill(t ,v)
            print(f"Wind Chill: {wind_chill:.2f}") 

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()