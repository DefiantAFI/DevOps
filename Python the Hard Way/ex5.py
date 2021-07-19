name = 'Zed A. Shaw'
age = 35  # not a lie
height = 72  # inches
heightcm = round(float(height) * 0.393701)  # centimeters
weight = 180  # lbs
weightkg = round(float(weight) * 0.45359237)  # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + heightcm + weightkg
print(f"If I add my age: {age}, my height in centimeters: {heightcm}, and my "
      f"weight in kilograms: {weightkg} I get {total}.")
