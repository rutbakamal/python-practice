#we use f-Strings to type out code where both text and numbers are required simultaneously. an example:

print(f"The temperature 75F in degrees Celsius is: {((75 - 32) * 5 / 9)} C")

#'f' denotes f-string or 'Formatted String' 
#'{}' curly braces are used to enclose the numeric calculations
#The f character tells Python that the subsequent string has data or computations within any pair of curly braces

#this works too: (from previous knowledge)
print("The temperature 75F in degrees Celsius is:", ((75 - 32) * 5 / 9), "C")

# → You can limit the answer to no characters after the decimal place by adding :.0f inside the curly braces of the f-string
print(f"Isabel's dog age is {28/7:.0f}")
#output: Isabel's dog age is 4 (instead of 4.0)

#To show a **fixed number of decimal places** in an f-string, use `:.nf` where `n` is the number of decimal places you want.
print(f"Isabel's dog age is {28/7:.1f}")
#Output: Isabel's dog age is 4.0

print(f"Isabel's dog age is {28/7:.2f}")
#Output: Isabel's dog age is 4.00

#Multi-line f-strings
print(f"""Most countries use the metric system for recipe measurement, but American bakers use a different system. For example, they use fluid ounces to measure liquids instead of milliliters (ml).
So you need to convert recipe units to your local measuring system!
For example, 8 fluid ounces of milk is {8 * 29.5735:.0f} ml.
And 100ml of water is {100 / 29.5735:.0f} fluid ounces.""")
