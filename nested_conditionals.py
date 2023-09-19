bob_age = input("Enter Bob's age")
sarah_age = input("Enter Sarah's age")
mary_age = input("Enter Mary's age")
if bob_age > sarah_age:
    print('Bob is older than Sarah')
    if bob_age > mary_age:
        print("Bob is the Oldest")
elif bob_age == sarah_age:
    print('Bob and Sarah have the same age')
    if bob_age == mary_age:
        print("All the three are of same age")       
else:
    print('Bob is younger than Sarah')
    if bob_age < mary_age :
        print ("Bob is the youngest")
        if mary_age > sarah_age:
            print("Mary is the Oldest")
        else:
            print("Sarah is the Oldest")
        
