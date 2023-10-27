# Reads input file and returns final_array with rod sizes and prices attached
def parse_input():

    # Instantiate final_array to store and return
    final_array = []

    # Reads text file input and stores in lines
    with open('input1.txt' , 'r' ) as file:
        lines = file.readlines()

    print(lines)
    
    # Loop through lines and assume every 2nd line is for number of pieces & price of each piece respecitvely
    for i in range(0 , len(lines) , 2):

        # Store number of rod pieces
        rods = int(lines[i])

        # Steps to clean up and convert rod price string
        # Removes left and right brackets
        rods_price_str = lines[i+1].strip()
        #Convert rod_prices in strinfs to array
        rods_price_str = rods_price_str[1:-1]

        # Instantiate rods_price array for storing prices of each rod
        rods_price=[]
        
        # Remove all commas from string to transfer numbers to rods_price array
        for x in rods_price_str.split(','):
            rods_price.append(int(x))
        
        # Store rod pieces and prices in data and append to final_array
        data = [rods , rods_price]
        final_array.append(data)

    # Return final_array with rod pieces and prices information
    return final_array



def rod_cutting(n , prices):

    # Instantiate optimal_price array used for Memoization
    # Store optimal rod_cutting for all rods of length i 
    # Aka store all C(i)
    optimal_price = []

    # Set all optimal prices equal to zero first , assuming that there is no negative value
    for i in range(n+1):
        optimal_price.append(0)
    
    # Loop n+1 cuts
    for i in range(0 , n+1):

        # Instantiate big_num used to store large negative number
        big_num = -99999

        #Run all 
        for j in range(1 , i+1):
            # Replace big_num value with max of either big_num or new max price
            big_num = max(prices[j-1] + optimal_price[i-j] , big_num)
            # Store new optimal_price value as current big_num value
            optimal_price[i] = big_num

    #print(optimal_price[n])
    return optimal_price[n]



# --- Main starts here ---
# Call parse_input() and store values in final_array
final_array = parse_input()

# Once you have the final array , you need to run rod_cutting_dp on each value and run it
for values in final_array:
    print("The max revenue is " , rod_cutting(values[0] , values[1]))
