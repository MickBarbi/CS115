#James Barbi
#I pledge my Honor that I have abided by the Stevens Honor System.


r = int(input("Enter red value (0-255): "))
g = int(input("Enter green value (0-255): "))
b = int(input("Enter blue value (0-255): "))

w = max(r/255, g/255, b/255)
cyan = str((w - (r / 255)) / w)
magenta = str((w - (g / 255)) / w)
yellow = str((w - (b / 255)) / w)
black = str(1 - w)

print("Given your RGB values, the respective CMYK value is (" + cyan + ", " + magenta + ", " + yellow + ", " + black)
input("Hit enter to end program")
