#include "Cubert.hpp"
#include <iostream>
#include <string>
//Ignore this, its not important
int main(){
    Cubert cube;
    cube.run_moves("w2g2");
    Cubert cube_copy(cube);
    cube.print_cube();
    cube_copy.print_cube();
    cube.run_moves("g2w2");
    cube.print_cube();
    cube_copy.print_cube();

    for (char i: cube.get_cube())
        std::cout << i;
    std::cout<<std::endl;
    //testing get_cube() function, should return a copy of the cube vector, 
    //but modifying it does not modify the real cube
    auto mc = cube.get_cube();
    //add an X to the returned copy
    mc[5]='X';
    for (char i: mc)
        std::cout << i;
    std::cout<<std::endl;
    //In the original cube, no X
    for (char i: cube.get_cube())
        std::cout << i;
    std::cout<<std::endl;
    return 0;
}