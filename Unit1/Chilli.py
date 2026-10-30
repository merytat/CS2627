#read input
pepper1 = input("") # for CCC don't add prompt to your input
pepper2 = input("")
pepper3 = input("")

# efficient way
peppers = (pepper3 + pepper2 + pepper1).lower()
total = peppers.count("poblano")*1500 + peppers.count("mirasol")*6000

# not so efficient
poblano = 1500
mirasol = 6000
serrano = 15500
cayenne = 40000
thai = 75000
habanero = 125000
totalSpiciness = 0

if pepper1.lower() == "poblano":
    totalSpiciness += poblano
elif pepper1.lower() == "mirasol":
    totalSpiciness += mirasol
elif pepper1.lower() == "serrano":
    totalSpiciness += serrano
elif pepper1.lower() == "cayenne":
    totalSpiciness += cayenne
elif pepper1.lower() == "thai":
    totalSpiciness += thai
elif pepper1.lower() == "habanero":
    totalSpiciness += habanero

if pepper2.lower() == "poblano":
    totalSpiciness += poblano
elif pepper2.lower() == "mirasol":
    totalSpiciness += mirasol
elif pepper2.lower() == "serrano":
    totalSpiciness += serrano
elif pepper2.lower() == "cayenne":
    totalSpiciness += cayenne
elif pepper2.lower() == "thai":
    totalSpiciness += thai
elif pepper2.lower() == "habanero":
    totalSpiciness += habanero

if pepper3.lower() == "poblano":
    totalSpiciness += poblano
elif pepper3.lower() == "mirasol":
    totalSpiciness += mirasol
elif pepper3.lower() == "serrano":
    totalSpiciness += serrano
elif pepper3.lower() == "cayenne":
    totalSpiciness += cayenne
elif pepper3.lower() == "thai":
    totalSpiciness += thai
elif pepper3.lower() == "habanero":
    totalSpiciness += habanero




