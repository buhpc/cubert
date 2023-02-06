#ifndef CUBERT_H
#define CUBERT_H

#include <iostream>
#include <array>
#include <vector>

class Cubert {
    private:
        void (Cubert::*moves[6])(int) = {&Cubert::w_move, &Cubert::o_move, &Cubert::g_move, 
                                   &Cubert::r_move, &Cubert::b_move, &Cubert::y_move};
        std::vector<char> cube;
        void perm_cycle(std::array<int, 2> a, std::array<int, 2> b, std::array<int, 2> c, std::array<int, 2> d);
    public:
        //create a cube with an optional seed input (string of starting moves)
        Cubert();
        Cubert(std::string seed);
        Cubert(Cubert &c);
        void w_move(int direction);
        void o_move(int direction);
        void g_move(int direction);
        void r_move(int direction);
        void b_move(int direction);
        void y_move(int direction);
        void print_cube();
        std::vector<char> get_cube() const {return cube;}
        void run_moves(std::string commands);
};

#endif