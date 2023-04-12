def main():
    lime = input("Enter time:")
    x = convert(lime)
    if 7 == int(x):
        print("breakfast time")
    elif 12 == int(x):
        print("lunch time")
    elif int(x) == 18:
        print("dinner time")
    else:
        return 0
        
    
    
def convert(time):
    hours, minutes= time.split(":")
    z = float(hours) + float(minutes)/60
    return z






main()