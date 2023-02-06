from cubert import cubert
import sys
def main():
    #user input
    if(len(sys.argv)>1):
        command=sys.argv[1]
    else:
        command=""
    print("seed: ",command)
    cube = cubert(command)
    cube.print_cube()
    
    while True:
        command = input("Enter your command(s): ")
        if command == "exit":
            exit()
        
        cube.run_moves(command)
        cube.print_cube()
            
if __name__ == "__main__":
    main()