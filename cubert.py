class cubert:
        
    def print_cube(self):
        print("{", end='')
        for i in range(6):
            print("{", end='')
            for j in range(9):
                print(self.cube[i*9+j], end = '')
            if i != 5:
                print("},")
            else:
                print("}}")
    
    def __perm_cycle(self,a,b,c,d):
        p_a=self.cube[a[0]*9+a[1]]
        p_b=self.cube[b[0]*9+b[1]]
        p_c=self.cube[c[0]*9+c[1]]
        p_d=self.cube[d[0]*9+d[1]]
        #copy to next location
        self.cube[a[0]*9+a[1]]=p_d
        self.cube[b[0]*9+b[1]]=p_a
        self.cube[c[0]*9+c[1]]=p_b
        self.cube[d[0]*9+d[1]]=p_c
    def w_move(self,direction):
        f=0 #face
        a=[4,3,2,1] #adjacents
        #direction=0 or 1 (Cw/ccw)
        if(direction==0):
            self.__perm_cycle((f,0),(f,2),(f,8),(f,6))
            self.__perm_cycle((f,1),(f,5),(f,7),(f,3))
            self.__perm_cycle((a[0],0),(a[1],0),(a[2],0),(a[3],0))
            self.__perm_cycle((a[0],1),(a[1],1),(a[2],1),(a[3],1))
            self.__perm_cycle((a[0],2),(a[1],2),(a[2],2),(a[3],2))
        if(direction==1):
            self.__perm_cycle((f,6),(f,8),(f,2),(f,0))
            self.__perm_cycle((f,3),(f,7),(f,5),(f,1))
            self.__perm_cycle((a[3],0),(a[2],0),(a[1],0),(a[0],0))
            self.__perm_cycle((a[3],1),(a[2],1),(a[1],1),(a[0],1))
            self.__perm_cycle((a[3],2),(a[2],2),(a[1],2),(a[0],2))

    def o_move(self,direction):
        f=1 #face
        a=[0,2,5,4] #adjacents
        #direction=0 or 1 (Cw/ccw)
        if(direction==0):
            self.__perm_cycle((f,0),(f,2),(f,8),(f,6))
            self.__perm_cycle((f,1),(f,5),(f,7),(f,3))
            self.__perm_cycle((a[0],0),(a[1],0),(a[2],0),(a[3],8))
            self.__perm_cycle((a[0],3),(a[1],3),(a[2],3),(a[3],5))
            self.__perm_cycle((a[0],6),(a[1],6),(a[2],6),(a[3],2))
        if(direction==1):
            self.__perm_cycle((f,6),(f,8),(f,2),(f,0))
            self.__perm_cycle((f,3),(f,7),(f,5),(f,1))
            self.__perm_cycle((a[3],8),(a[2],0),(a[1],0),(a[0],0))
            self.__perm_cycle((a[3],5),(a[2],3),(a[1],3),(a[0],3))
            self.__perm_cycle((a[3],2),(a[2],6),(a[1],6),(a[0],6))

    def g_move(self,direction):
        f=2 #face
        a=[0,3,5,1] #adjacents
        #direction=0 or 1 (Cw/ccw)
        if(direction==0):
            self.__perm_cycle((f,0),(f,2),(f,8),(f,6))
            self.__perm_cycle((f,1),(f,5),(f,7),(f,3))
            self.__perm_cycle((a[0],7),(a[1],0),(a[2],2),(a[3],8))
            self.__perm_cycle((a[0],8),(a[1],3),(a[2],1),(a[3],5))
            self.__perm_cycle((a[0],9),(a[1],6),(a[2],0),(a[3],2))
        if(direction==1):
            self.__perm_cycle((f,6),(f,8),(f,2),(f,0))
            self.__perm_cycle((f,3),(f,7),(f,5),(f,1))
            self.__perm_cycle((a[3],8),(a[2],2),(a[1],0),(a[0],7))
            self.__perm_cycle((a[3],5),(a[2],1),(a[1],3),(a[0],8))
            self.__perm_cycle((a[3],2),(a[2],0),(a[1],6),(a[0],9))


    def r_move(self,direction):
        f=3 #face
        a=[0, 4, 5, 2] #adjacents
        #direction=0 or 1 (Cw/ccw)
        if(direction==0):
            self.__perm_cycle((f,0),(f,2),(f,8),(f,6))
            self.__perm_cycle((f,1),(f,5),(f,7),(f,3))
            self.__perm_cycle((a[0],8),(a[1],0),(a[2],8),(a[3],8))
            self.__perm_cycle((a[0],5),(a[1],3),(a[2],5),(a[3],5))
            self.__perm_cycle((a[0],2),(a[1],6),(a[2],2),(a[3],2))
        elif(direction==1):
            self.__perm_cycle((f,0),(f,6),(f,8),(f,2))
            self.__perm_cycle((f,1),(f,3),(f,7),(f,5))
            self.__perm_cycle((a[3],8),(a[2],8),(a[1],0),(a[0],8))
            self.__perm_cycle((a[3],5),(a[2],5),(a[1],3),(a[0],5))
            self.__perm_cycle((a[3],2),(a[2],2),(a[1],6),(a[0],2))

    def b_move(self,direction):
        f=4 #face
        a=[0, 1, 5, 3] #adjacents
        #direction=0 or 1 (Cw/ccw)
        if(direction==0):
            self.__perm_cycle((f,0),(f,2),(f,8),(f,6))
            self.__perm_cycle((f,1),(f,5),(f,7),(f,3))
            self.__perm_cycle((a[0],0),(a[1],6),(a[2],8),(a[3],2))
            self.__perm_cycle((a[0],1),(a[1],3),(a[2],7),(a[3],5))
            self.__perm_cycle((a[0],2),(a[1],0),(a[2],6),(a[3],8))
        elif(direction==1):
            self.__perm_cycle((f,0),(f,6),(f,8),(f,2))
            self.__perm_cycle((f,1),(f,3),(f,7),(f,5))
            self.__perm_cycle((a[3],2),(a[2],8),(a[1],6),(a[0],0))
            self.__perm_cycle((a[3],5),(a[2],7),(a[1],3),(a[0],1))
            self.__perm_cycle((a[3],8),(a[2],6),(a[1],0),(a[0],2))

    def y_move(self,direction):
        f=5 #face
        a=[1, 2, 3, 4] #adjacents
        #direction=0 or 1 (Cw/ccw)
        if(direction==0):
            self.__perm_cycle((f,0),(f,2),(f,8),(f,6))
            self.__perm_cycle((f,1),(f,5),(f,7),(f,3))
            self.__perm_cycle((a[0],6),(a[1],6),(a[2],6),(a[3],6))
            self.__perm_cycle((a[0],7),(a[1],7),(a[2],7),(a[3],7))
            self.__perm_cycle((a[0],8),(a[1],8),(a[2],8),(a[3],8))
        elif(direction==1):
            self.__perm_cycle((f,0),(f,6),(f,8),(f,2))
            self.__perm_cycle((f,1),(f,3),(f,7),(f,5))
            self.__perm_cycle((a[3],6),(a[2],6),(a[1],6),(a[0],6))
            self.__perm_cycle((a[3],7),(a[2],7),(a[1],7),(a[0],7))
            self.__perm_cycle((a[3],8),(a[2],8),(a[1],8),(a[0],8))
            
    def run_moves(self,command):
        i = 0
        while i < len(command):
            current = command[i]
            if i+1 < len(command) and command[i+1] == "'":
                dir = 1
                i = i+2
                times=1
            elif i+1 < len(command) and command[i+1] == "2":
                dir=0
                i = i+2
                times=2
            else:
                dir = 0
                i = i+1
                times=1

            if current == 'w':
                move_idx = 0
            elif current == 'o':
                move_idx = 1
            elif current == 'g':
                move_idx = 2
            elif current == 'r':
                move_idx = 3
            elif current == 'b':
                move_idx = 4
            elif current == 'y':
                move_idx = 5
                
            for j in range(times):
                self.moves[move_idx](dir)
    
    def __init__(self,seed=""):
        self.cube=['w']*9+['o']*9+['g']*9+['r']*9+['b']*9+['y']*9
        self.moves=[self.w_move,self.o_move,self.g_move,self.r_move,self.b_move,self.y_move]
        
        self.run_moves(seed)
