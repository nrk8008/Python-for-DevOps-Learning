import sys

type = sys.argv[1]

if type == "t2.micro":
    print("This will charge $2 per Day")
    #print("Ok, we will create the instance for you")

elif type == "t2.medium" :
    print("This will charge $4 per Day")

else :
    print("Invalid Type")

