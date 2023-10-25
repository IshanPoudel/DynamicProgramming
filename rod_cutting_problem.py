#Read file



def parse_input():

    final_array = []

    with open('input1.txt' , 'r' ) as file:
        lines = file.readlines()
            #Assume that each 2 lines are for number of pieces and price of each piece respecitvely. 

    print(lines)

    for i in range(0 , len(lines) , 2):
        rods = int(lines[i])
        rods_price_str = lines[i+1].strip()

        #Remove left [  and right ]


        #Convert rod_prices in strinfs to array

        rods_price_str = rods_price_str[1:-1]


        #Array for storing rod_prices
        rods_price=[]
        

        for x in rods_price_str.split(','):
            rods_price.append(int(x))
        
        data = [rods , rods_price]
        final_array.append(data)

    return final_array



def rod_cutting(n , prices):

    #Memoization array
    #Store optimal rod_cutting for all rods of length i 
    #Aka store all C(i)

    optimal_price = []

    #Set all optimal price equal to zero first , assuming that there is no negative value
    for i in range(n+1):
        optimal_price.append(0)
    




    for i in range(0 , n+1):

        #Set a large negative num
        big_num = -99999

        #Run all 
        for j in range(1 , i+1):


            big_num = max(prices[j-1] + optimal_price[i-j] , big_num)
            optimal_price[i]=big_num

    print(optimal_price[n])
    return optimal_price[n]



final_array = parse_input()



  
#Once you have the final array , you need to run rod_cutting_dp on each value and run it



for values in final_array:
    print("The max revenue is " , rod_cutting(values[0] , values[1]))

