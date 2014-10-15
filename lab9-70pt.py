############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "What is the temperature in Celcius?"
userinput = int(raw_input())
farenheit = userinput * 9 / 5 + 32
print "Farenheit:" + str(farenheit)