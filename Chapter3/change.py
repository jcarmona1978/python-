#change.py
#A program to calculate the values of some chane in dollars




def main ():
	print ("Change Counter")
	print ()
	print ("Please enter the count of each coin type.")

	quarters = eval (input("Quarters: "))
	dimes = eval(input("Dimes: "))
	nickles = eval (input("Nickles: "))
	pennies = eval(input("Pennies: "))
	total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
	print ()
	print ("the total value of your change is", total)

main()
