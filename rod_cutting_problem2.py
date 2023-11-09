# Reads input file and returns FinalArray with Width and Height of wood board, along with board cuts you can do
def parse_input():

    # Instantiate FinalArray to store and return
    BoardCuts = []
    FinalArray = []

    # Reads text file input and stores in lines
    with open('input2.txt' , 'r' ) as file:
        lines = file.readlines()
    
    # Loop through lines and skip over every 2
    for i in range(0 , len(lines) , 2):

        # Store Width and Height from first line of the wood board
        # Must use Map to convert to ints since lines[i] is returned as a list
        Width, Height = map(int, lines[i].strip().split())

        # Instantiate BoardCuts to store cuts as int values
        BoardCuts = []

        # Store the cut locations that can be used to cut the wood board
        # Strip off left and right brackets and split based on "],"
        BoardCutString = lines[i+1].strip()[1:-1]
        BoardCutString = BoardCutString.split("],")
        
        #The arrays in BoardCutString may have a leading space (depending on the input). Need to remove that
        BoardCutString = [s.lstrip() for s in BoardCutString]

        # Splits x and y values and stores as a paired list of ints
        # Covers 2 cases:
        #     Case 1: No trailing ] - This case happens if it is not the last cut in the string
        #     Case 2: Trailing ] - This case happens if it is the last cut in the string
        for cut in BoardCutString:
            if "]" not in cut:
                BoardCuts.append(list(map(int, cut[1:].split(","))))
            else:
                BoardCuts.append(list(map(int, cut[1:-1].split(","))))
        
        # Store board Width, Height, and board cuts in data and append to FinalArray
        data = [Width, Height, BoardCuts]
        FinalArray.append(data)

    # Return FinalArray with board Width, Height, and possible board cuts
    return FinalArray



# board_cutting() Function
# Inputs: Width and Height of wood board in Boards, X and Y values as list of board cuts
# Returns: Total min value of cuts cost, Optimal order cuts take place
def board_cutting(Boards, BoardCuts, MemoizedDictionary):

    key = (tuple(tuple(Board) for Board in Boards), tuple(tuple(Cut) for Cut in BoardCuts))

    # If key is already stored in Memoized Dict then return key or
    # If no board cuts return some hardcoded default values
    if key in MemoizedDictionary:
        return MemoizedDictionary[key]
    if not BoardCuts:
        return 0, []

    # Define MinCost as some high number and Instantiate OptimalOrder to store cut order
    MinCost = 99999
    OptimalOrder = []

    # Loop through all boards stored in the Boards parameter
    # Begining will be 1 and increase based on cuts: (n * 4 - 1) Boards
    for i, (XStart, YStart, Width, Height) in enumerate(Boards):

        # Loop through each cut and find the board associated with that cut if multiple boards exist
        for x, y in BoardCuts:

            # Check if x and y are within bounds of the current board being cut
            if XStart <= x < XStart + Width and YStart <= y < YStart + Height:

                # Cost of this specific board cut
                Cost = 2 * (Width * Height)

                # Remove the board that is being cut from the list
                # Add the four new boards that result from the cut
                # Example of the coordiantes of the board
                # Height___________________________
                # |                                |
                # |                                |
                # |                                |
                # |                                |
                # |                                |
                # |              _|_               |
                # |               |(X, Y)          |
                # |                                |
                # |                                |
                # |________________________________|Width
                # (XStart, YStart)
                NewBoards = Boards[:i] + Boards[i+1:]
                NewBoards.extend([[XStart, YStart, x, y],           # Top Left
                                  [x, YStart, Width - x, y],        # Top Right
                                  [XStart, y, x, Height - y],       # Bottom Left
                                  [x, y, Width - x, Height - y]])   # Bottom Right

                # Remove the cut that was just made
                NewBoardCuts = BoardCuts.copy()
                NewBoardCuts.remove([x, y])

                # Calculate next remaining cost and order by recursively calling board_cutting with new parameters
                RemainingCost, RemainingOrder = board_cutting(NewBoards, NewBoardCuts, MemoizedDictionary)

                # Store new total cost and compare to current minimum cost
                TotalCost = Cost + RemainingCost
                if TotalCost < MinCost:
                    
                    # Replace MinCost with TotalCost and append new cut to OptimalOrder
                    MinCost = TotalCost
                    OptimalOrder = [[x, y]] + RemainingOrder

    # Add new entry into Memoized Dictionary file and return the minimum cost and optimal order of cuts
    MemoizedDictionary[key] = (MinCost, OptimalOrder)
    return MinCost, OptimalOrder



# --- Main starts here ---
# Call parse_input() function and store results in FinalArray
# FinalArray example will look like: [Width, Height, [[cut_x1, cut_y1], [cut_x2, cut_y2], ...]]
FinalArray = parse_input()
print(FinalArray)

# Once you have the final array , you need to run board_cutting to find min cost and main order to cut the board
# Instantiate a memoized dictionary to hold all 
for Width, Height, CutPoints in FinalArray:
    MemoizedDictionary = {}
    MinimumCost, BoardCutOrder = board_cutting([[0, 0, Width, Height]], CutPoints, MemoizedDictionary)
    print("The minimum total cost is " + str(MinimumCost) + ". The optimal order of the cuts is " + str(BoardCutOrder) + ".")