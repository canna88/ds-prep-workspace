alessio = [[0, 0, 0, 0], 
           [0, 0, 0, 0], 
           [0, 0, 1, 0],
           [0, 0, 1, 0]]



def check_if_mine(x,y,list):
    
    mine_count = int(0)
    
    for i in range(-1,2):
        for j in range(-1,2):
            
            if not (((x+i) == x) and ((y+j) == y)):
                if list[x+i][y+j] == 1:
                    mine_count += 1
                else:
                    None
    
    return mine_count
 


print(check_if_mine(2,1,alessio))