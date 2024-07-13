first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
name_length = len (first_name) + len(last_name)

print ("*"*10)
if name_length == 12:
    print(f"{first_name} {last_name} is exactly the average length of American names")

    #print("EXACTLY AVERAGE!")

elif name_length < 12:
    print(f"{first_name} {last_name} is shorter than the average American names")
    #print("SHORTER THAN AVERAGE")

else:
    print(f"{first_name} {last_name} is lonnger than the average American names")
    
    #print("LONGER THAN AVERAGE")
    print ("*"*10)
