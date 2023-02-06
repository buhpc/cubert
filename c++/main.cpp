/*
    An example main program that uses the Cubert library
    When creating your own solver, you can create a Cubert
    object, and call its public functions in a similar way.
    You have the choice of running moves using the run_moves function,
    which takes in a string of 0 or more moves in text format, or
    calling the face rotations directly, i.e. cube.w_move(direction)
    at anytime, you can print out the current state of the cube with print_cube

    Please refrain from modifying the Cubert.cpp file, as it has been set up to 
    provide safe operations that won't cause illegal moves, or corrupt the cube
*/

#include <iostream>
#include <string>
#include "Cubert.hpp"

int main(int argc, char* argv[]) {
    std::string command = "";
    if (argc > 1) {
        command = argv[1];
    }
    std::cout << "seed: " << command << std::endl;
    Cubert cube(command);
    cube.print_cube();

    while (true) {
        std::cout << "Enter your command(s): ";
        std::cin >> command;
        if (command == "exit") {
            return 0;
        }

        cube.run_moves(command);
        cube.print_cube();
    }
    return 0;
}
