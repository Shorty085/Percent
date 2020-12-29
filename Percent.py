#THIS APP GIVES YOU THE GIVEN PERCENT OF ANY NUMBER
#EXAMPLE 10% OF 100 IS 10

percent = int(input("Enter the desired percentage amount: "))

print("You have entered a percentage of {}%".format(percent))

amount = int(input("What is the amount you want to calculate {}% of: ".format(percent)))

calc1 = percent * amount
calc2 = calc1 / 100
print(calc2)
print("{}% of ${} is {}\n".format(percent,amount,calc2))

percentOf = print("WORK ON THIS ###################")