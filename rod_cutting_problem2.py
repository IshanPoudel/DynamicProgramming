# Reads input file and returns final_array with width and height of wood board, along with board cuts you can do
def parse_input():

    # Instantiate final_array to store and return
    board_cuts = []
    final_array = []

    # Reads text file input and stores in lines
    with open('input2.txt' , 'r' ) as file:
        lines = file.readlines()
    
    # Loop through lines and skip over every 2
    for i in range(0 , len(lines) , 2):

        # Store width and height from first line of the wood board
        # Must use Map to convert to ints since lines[i] is returned as a list
        width, height = map(int, lines[i].strip().split())

        # Instantiate board_cuts to store cuts as int values
        board_cuts = []

        # Store the cut locations that can be used to cut the wood board
        # Strip off left and right brackets and split based on "],"
        board_cuts_str = lines[i+1].strip()[1:-1]
        board_cuts_str = board_cuts_str.split("],")

        # Splits x and y values and stores as ints
        # Covers 2 cases:
        #     Case 1: No trailing ] - This case happens if it is not the last cut in the string
        #     Case 2: Trailing ] - This case happens if it is the last cut in the string
        for cut in board_cuts_str:
            if "]" not in cut:
                board_cuts.append(list(map(int, cut[1:].split(","))))
            else:
                board_cuts.append(list(map(int, cut[1:-1].split(","))))
        
        # Store board width, height, and board cuts in data and append to final_array
        data = [width, height, board_cuts]
        final_array.append(data)

    # Return final_array with board width, height, and possible board cuts
    return final_array



# board_cutting() Function
# Inputs: Width of wood board, Height of wood board, X and Y values as list of board cuts
# Returns: Total min value of cuts cost, Optimal order cuts take place
def board_cutting(width, height, board_cuts):


    return 0, 0

# --- Main starts here ---
# Call parse_input() function and store results in final_array
# final_array example will look like: [width, height, [[cut_x1, cut_y1], [cut_x2, cut_y2], ...]]
final_array = parse_input()
print(final_array)

# Once you have the final array , you need to run rod_cutting_dp on each value and run it
for values in final_array:
    min_cost, board_cut_order = board_cutting(values[0], values[1], values[2])
    print("The minimum total cost is " + str(min_cost) + ". The optimal order of the cuts is " + str(board_cut_order) + ".")