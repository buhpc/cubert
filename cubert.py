color = {
"U": "white", "D": "yellow", "L": "orange", "R": "red", "F": "#00aa00", "B": "blue", "X": "darkgray",
"o": "#fdfdc6", "x": "blueviolet", "y": "magenta"
}

cube=['w']*9+['o']*9+['g']*9+['r']*9+['b']*9+['y']*9

def print_cube(cube):
    print("{", end='')
    for i in range(6):
        print("{", end='')
        for j in range(9):
            print(cube[i*9+j], end = '')
        if i != 5:
            print("},")
        else:
            print("}}")
    
    
print_cube(cube)

def perm_cycle(cube,a,b,c,d):
    p_a=cube[a[0]*9+a[1]]
    p_b=cube[b[0]*9+b[1]]
    p_c=cube[c[0]*9+c[1]]
    p_d=cube[d[0]*9+d[1]]
    #copy to next location
    cube[a[0]*9+a[1]]=p_d
    cube[b[0]*9+b[1]]=p_a
    cube[c[0]*9+c[1]]=p_b
    cube[d[0]*9+d[1]]=p_c


def w_move(cube,direction):
    f=0 #face
    a=[4,3,2,1] #adjacents
    #direction=0 or 1 (Cw/ccw)
    if(direction==0):
        perm_cycle(cube,(f,0),(f,2),(f,8),(f,6))
        perm_cycle(cube,(f,1),(f,5),(f,7),(f,3))
        perm_cycle(cube,(a[0],0),(a[1],0),(a[2],0),(a[3],0))
        perm_cycle(cube,(a[0],1),(a[1],1),(a[2],1),(a[3],1))
        perm_cycle(cube,(a[0],2),(a[1],2),(a[2],2),(a[3],2))
    if(direction==1):
        perm_cycle(cube,(f,6),(f,8),(f,2),(f,0))
        perm_cycle(cube,(f,3),(f,7),(f,5),(f,1))
        perm_cycle(cube,(a[3],0),(a[2],0),(a[1],0),(a[0],0))
        perm_cycle(cube,(a[3],1),(a[2],1),(a[1],1),(a[0],1))
        perm_cycle(cube,(a[3],2),(a[2],2),(a[1],2),(a[0],2))
        
def o_move(cube,direction):
    f=1 #face
    a=[0,2,5,4] #adjacents
    #direction=0 or 1 (Cw/ccw)
    if(direction==0):
        perm_cycle(cube,(f,0),(f,2),(f,8),(f,6))
        perm_cycle(cube,(f,1),(f,5),(f,7),(f,3))
        perm_cycle(cube,(a[0],0),(a[1],0),(a[2],0),(a[3],8))
        perm_cycle(cube,(a[0],3),(a[1],3),(a[2],3),(a[3],5))
        perm_cycle(cube,(a[0],6),(a[1],6),(a[2],6),(a[3],2))
    if(direction==1):
        perm_cycle(cube,(f,6),(f,8),(f,2),(f,0))
        perm_cycle(cube,(f,3),(f,7),(f,5),(f,1))
        perm_cycle(cube,(a[3],8),(a[2],0),(a[1],0),(a[0],0))
        perm_cycle(cube,(a[3],5),(a[2],3),(a[1],3),(a[0],3))
        perm_cycle(cube,(a[3],2),(a[2],6),(a[1],6),(a[0],6))

def g_move(cube,direction):
    f=2 #face
    a=[0,3,5,1] #adjacents
    #direction=0 or 1 (Cw/ccw)
    if(direction==0):
        perm_cycle(cube,(f,0),(f,2),(f,8),(f,6))
        perm_cycle(cube,(f,1),(f,5),(f,7),(f,3))
        perm_cycle(cube,(a[0],7),(a[1],0),(a[2],2),(a[3],8))
        perm_cycle(cube,(a[0],8),(a[1],3),(a[2],1),(a[3],5))
        perm_cycle(cube,(a[0],9),(a[1],6),(a[2],0),(a[3],2))
    if(direction==1):
        perm_cycle(cube,(f,6),(f,8),(f,2),(f,0))
        perm_cycle(cube,(f,3),(f,7),(f,5),(f,1))
        perm_cycle(cube,(a[3],8),(a[2],2),(a[1],0),(a[0],7))
        perm_cycle(cube,(a[3],5),(a[2],1),(a[1],3),(a[0],8))
        perm_cycle(cube,(a[3],2),(a[2],0),(a[1],6),(a[0],9))

w_move(cube,0)
print()
print_cube(cube)
w_move(cube,1)
print()
print_cube(cube)
