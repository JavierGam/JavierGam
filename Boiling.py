unit = input ("what unit are you using? ")
temp = int(input ("what temperature is the water? "))

if unit == 'f':
    if temp == 212:
        print("WATER IS BOILING!")
    else: 
        print("WATER IS NOT BOILING. MUST HIT 212F")
elif unit == 'c':
    if temp == 100:
        print("WATER IS NOT BOILING. MUST HIT 100C")
elif unit == 'k':
    if temp == 373:
        print("WATER IS BOILING!")
    else:
        print("WATER IS NOT BOILING. MUST HIT 373K")

#f - 212
#c - 100
#k -373
