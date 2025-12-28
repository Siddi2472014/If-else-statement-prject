#Program to make a temperature reader to tell user what clothes to wear based on temperature input
temperature = float(input("Enter the temperature in Celcius: "))
if temperature < 0:
    print("It's freezing! Wear a heavy coat, gloves, and a hat.")
elif temperature <= 10:
    print("It's cold, stick to wearing a jacket and a scarf.")
elif temperature <= 20:
    print("It's mild, a light jacket or sweater is fine.")
elif temperature <= 30:
    print("It's quite hot outside, a t-shirt and short pants will do.")
else:
    print("It's very hot outside, wear very light clothing, or better just stay inside!")
