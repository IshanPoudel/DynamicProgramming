# Reads input file and returns final_array with rod sizes and prices attached
def parse_input():

    # Instantiate final_array to store and return
    final_array = []

    # Reads text file input and stores in lines
    with open('input2.txt' , 'r' ) as file:
        lines = file.readlines()
    
    # Loop through lines and skip over every 2
    for i in range(0 , len(lines) , 2):

        # Store width and height from first line of the wood board
        # Must use Map to convert to ints since lines[i] is returned as a list
        width, height = map(int, lines[i].strip().split())

        # Store the cut locations that can be used to cut the wood board
        board_cuts = lines[i+1].strip()
        
        # Store rod pieces and prices in data and append to final_array
        data = [width, height, board_cuts]
        final_array.append(data)

    # Return final_array with rod pieces and prices information
    return final_array



# --- Main starts here ---
# Call parse_input() function and store results in final_array
# final_array example will look like: [width, height, [[cut_x1, cut_y1], [cut_x2, cut_y2], ...]]
final_array = parse_input()
print(final_array)