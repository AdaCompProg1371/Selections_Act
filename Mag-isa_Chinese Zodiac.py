# Type year
year = int(input("Year:"))

# Reveal Chinese zodiac animal
if year % 12 == 0:
    sign = "monkey"
elif year % 12 == 1:
    sign = "rooster"
elif year % 12 == 2:
    sign = "dog"
elif year % 12 == 3:
    sign = "pig"
elif year % 12 == 4:
    sign = "rat"
elif year % 12 == 5:
    sign = "ox"
elif year % 12 == 6:
    sign = "tiger"
elif year % 12 == 7:
    sign = "rabbit"
elif year % 12 == 8:
    sign = "dragon"
elif year % 12 == 9:
    sign = "snake"
elif year % 12 == 10:
    sign = "horse"
else:
    sign = "goat"

# State result
print("Year", year, "is the year of the", sign)
