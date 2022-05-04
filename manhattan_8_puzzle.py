def format(matrix):
    for i in range(9):
        if i%3==0 and i>0:
            print("")
        print(str(matrix[i])+" ", end = "")

def convert(s):
    mat = []
    a = []
    b = []
    c = []
    for i in range(9):
        if i<3:
            a.append(s[i])
        if i>=3 and i<=5:
            b.append(s[i])
        if i>5:
            c.append(s[i])

    mat.append(a)
    mat.append(b)
    mat.append(c)
    return mat
    

def find_distance(value):
    x1 = 999
    y1 = 999
    goal = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 0]]
             
    for i in range(3):
        for j in range(3):
            if goal[i][j]==value:
                x1 = i
                y1 = j
                break

    return x1, y1


    
        
def count(start_state):
    inits = start_state.copy()
    inicon = convert(inits)
    x1 = y1 = x2 = y2 = 999
    total_h = 0;
    
    for i in range(3):
        for j in range(3):
            x1, y1 = find_distance(inicon[i][j])
            x2, y2 = i, j
            total_h += abs(x1-x2)+abs(y1-y2)
            
    return total_h


def move_place(ar, p, st):
    rh = 9999
    store_st = st.copy()
    
    for i in range(len(ar)):
        
        dupl_st = st.copy()
        
        tmp = dupl_st[p]
        dupl_st[p] = dupl_st[arr[i]]
        dupl_st[arr[i]] = tmp
        
        trh = count(dupl_st)
        
        if trh<rh:
            rh = trh
            store_st = dupl_st.copy()
    
    return store_st, rh
    
    
state = []
print("Enter your element: ")

for i in range(9):
    ele = int(input())
    state.append(ele) 
	
print("Start state: ", state)


h = count(state)
Level = 1


format(state)
print("\nManhattan Distance Heuristic Value : "+str(h))

print("")
print("->Solutions")


while h>0:
    position = int(state.index(0))
    
    Level += 1
    
    if position==0:
        arr = [1, 3]
        state, h = move_place(arr, position, state)
    elif position==1:
        arr = [0, 2, 4]
        state, h = move_place(arr, position, state)
    elif position==2:
        arr = [1, 5]
        state, h = move_place(arr, position, state)
    elif position==3:
        arr = [0, 4, 6]
        state, h = move_place(arr, position, state)
    elif position==4:
        arr = [1, 3, 5, 7]
        state, h = move_place(arr, position, state)
    elif position==5:
        arr = [2, 4, 8]
        state, h = move_place(arr, position, state)
    elif position==6:
        arr = [3, 7]
        state, h = move_place(arr, position, state)
    elif position==7:
        arr = [4, 6, 8]
        state, h = move_place(arr, position, state)
    elif position==8:
        arr = [5, 6]
        state, h = move_place(arr, position, state)
        
    format(state)
    print("\nManhattan Distance Heuristic Value : "+str(h))


"""1
2
3
5
6
0
4
7
8"""
