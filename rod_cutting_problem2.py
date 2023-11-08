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
    # Boards = sorted(Boards, key=lambda x: x[0] * x[1], reverse=True)

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

    # print("Sorted Boards:", Boards)

    for i, (XStart, YStart, Width, Height) in enumerate(Boards):
        for x, y in BoardCuts:
            # XCut and YCut used for positional values for new board coordinates
            XCut = XStart + x
            YCut = YStart + y

            # if XStart <= XCut < XStart + Width and YStart <= YCut < YStart + Height:
            if XStart <= XCut < Width and YStart <= YCut < Height: # <---- Adding this gets 2 of them right

                # print("Before cut, Boards:", Boards)
                # print("Cutting at:", [x, y])

                # Cost of this specific board cut
                Cost = 2 * Width * Height # <----- Adding this gets 2 of them right
                # Cost = 2 * (Width - XStart) * (Height - YStart) # <----- Adding this gets 2 of them right

                print("Cost for this cut:", Cost)

                # Remove the board that is being cut from the list
                # Add the four new boards that result from the cut

                # 
                # Height___________________________
                # |                                |
                # |                                |
                # |                                |
                # |                                |
                # |                                |
                # |              _|_               |
                # |               |(XCut, YCut)    |
                # |                                |
                # |                                |
                # |________________________________|Width
                # (XStart, YStart)
                NewBoards = Boards[:i] + Boards[i+1:]
                NewBoards.extend([[XStart, YStart, x, y],               # Top Left
                                  [XCut, YStart, Width - x, y],         # Top Right
                                  [XStart, YCut, x, Height - y],        # Bottom Left
                                  [XCut, YCut, Width - x, Height - y]]) # Bottom Right

                # Remove the cut that was just made
                NewBoardCuts = BoardCuts.copy()
                NewBoardCuts.remove([x, y])

                # print("Calling recursively with Boards:", NewBoards)
                # print("And remaining cuts:", NewBoardCuts)

                RemainingCost, RemainingOrder = board_cutting(NewBoards, NewBoardCuts, MemoizedDictionary)

                # print("Returned cost and order:", RemainingCost, RemainingOrder)

                TotalCost = Cost + RemainingCost
                print("Total Cost: ", TotalCost)
                if TotalCost < MinCost:
                    # print("This cost was added: ", MinCost)
                    MinCost = TotalCost
                    OptimalOrder = [[x, y]] + RemainingOrder

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