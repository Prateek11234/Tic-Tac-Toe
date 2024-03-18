board = ["   " for i in range(9)]

def boardchoice():  #this is a void function in which we donot pass anyhting as function parameters and the print is used for the answer instead of return statement
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
    

def playermove(icon):

    if icon == " X ":
        num = 1
    elif icon == " O ":
        num = 2

    print("your turn player{}".format(num))
    
    choice = int(input("tell me the number ?: ").strip())
    if board[choice-1] == "   ":
        board[choice-1] = icon
    else:
        print()
        print("The space is taken")

    

def isvictory(icon):
        
    if(board[0] == icon and board[1] == icon and board[2] == icon):   #instead of elif we can use or\ and write the all statements in one if code
        return True
    
    elif(board[3] == icon and board[4] == icon and board[5] == icon):
        return True
       
    elif(board[6] == icon and board[7] == icon and board[8] == icon):
        return True
        
    elif(board[0] == icon and board[4] == icon and board[8] == icon):
        return True
        
    elif(board[2] == icon and board[4] == icon and board[6] == icon):
        return True
        
    elif(board[0] == icon and board[3] == icon and board[6] == icon):
        return True
        
    elif(board[1] == icon and board[4] == icon and board[7] == icon):
        return True
        
    elif(board[2] == icon and board[5] == icon and board[8] == icon):
        return True
        
    else :
        return False

def isdraw():
    if "   " not in board:
        return True
    else:
        return False

while True:
    boardchoice()
    playermove(" X ")
    boardchoice()
    if isvictory(" X "):
        print("X Wins !! congo!!")
        break
    elif isdraw():
        print("it's a draw!!")
        break
    playermove(" O ")
    boardchoice()
    if isvictory(" O "):
        print("O Wins !! congo!!")
        break
    elif isdraw():
        print("it's a draw!!")
        break
    
