#################### /ᐠ｡ꞈ｡ᐟ\ ######################
#Developed by: Tal Mendelson
#Purpose: Holds the solutions to Practice 3.
#Date:08/03/2025
#################### /ᐠ｡ꞈ｡ᐟ\ ######################

################################################################################################
# https://gitlab.com/vaiolabs-io/python-script/-/tree/master/01_scripting_intro?ref_type=heads#practice-3
## Task: 
# Practice - Page 42 (01_scripting_intro)
# Create python script file where you:
# create variable for wifi/eth/network that you are connected to, and put in it that name.
# create variable for your laptops hostname and save the name in it.
# concatenate the variable above with new variable named my_con .
# print() the variable
# add id (or any number) of your connection to my_con variable and re-print it.
################################################################################################

# Variable for wifi network name
network_name = "Hogwarts"

# Variable for Laptop name
laptop_name = "TALME-LAP"

# Both Variables together
my_con = (network_name + " - " + laptop_name)
print("Connection Info:", my_con)

# Add an ID to the connection info
connection_id = "001"
my_con = connection_id + " - " + my_con

# Re-print with the ID
print("Connection Info:", my_con)