#include <iostream>
#include <array>
#include <vector>
#include "Cubert.hpp"
//private:
void Cubert::perm_cycle(std::array<int, 2> a, std::array<int, 2> b, std::array<int, 2> c, std::array<int, 2> d) {
    int p_a = cube[a[0] * 9 + a[1]];
    int p_b = cube[b[0] * 9 + b[1]];
    int p_c = cube[c[0] * 9 + c[1]];
    int p_d = cube[d[0] * 9 + d[1]];

    //copy to next location
    cube[a[0] * 9 + a[1]] = p_d;
    cube[b[0] * 9 + b[1]] = p_a;
    cube[c[0] * 9 + c[1]] = p_b;
    cube[d[0] * 9 + d[1]] = p_c;
}
// public:
void Cubert::w_move(int direction) {
    int f = 0; // face
    std::array<int, 4> a = {4, 3, 2, 1}; // adjacents
    // direction=0 or 1 (Cw/ccw)
    if (direction == 0) {
        perm_cycle({f, 0}, {f, 2}, {f, 8}, {f, 6});
        perm_cycle({f, 1}, {f, 5}, {f, 7}, {f, 3});
        perm_cycle({a[0], 0}, {a[1], 0}, {a[2], 0}, {a[3], 0});
        perm_cycle({a[0], 1}, {a[1], 1}, {a[2], 1}, {a[3], 1});
        perm_cycle({a[0], 2}, {a[1], 2}, {a[2], 2}, {a[3], 2});
    }
    if (direction == 1) {
        perm_cycle({f, 6}, {f, 8}, {f, 2}, {f, 0});
        perm_cycle({f, 3}, {f, 7}, {f, 5}, {f, 1});
        perm_cycle({a[3], 0}, {a[2], 0}, {a[1], 0}, {a[0], 0});
        perm_cycle({a[3], 1}, {a[2], 1}, {a[1], 1}, {a[0], 1});
        perm_cycle({a[3], 2}, {a[2], 2}, {a[1], 2}, {a[0], 2});
    }
}

void Cubert::o_move(int direction) {
    int f = 1; // face
    std::array<int, 4> a = {0, 2, 5, 4}; // adjacents
    // direction=0 or 1 (Cw/ccw)
    if (direction == 0) {
        perm_cycle({f, 0}, {f, 2}, {f, 8}, {f, 6});
        perm_cycle({f, 1}, {f, 5}, {f, 7}, {f, 3});
        perm_cycle({a[0], 0}, {a[1], 0}, {a[2], 0}, {a[3], 8});
        perm_cycle({a[0], 3}, {a[1], 3}, {a[2], 3}, {a[3], 5});
        perm_cycle({a[0], 6}, {a[1], 6}, {a[2], 6}, {a[3], 2});
    }
    if (direction == 1) {
        perm_cycle({f, 6}, {f, 8}, {f, 2}, {f, 0});
        perm_cycle({f, 3}, {f, 7}, {f, 5}, {f, 1});
        perm_cycle({a[3], 8}, {a[2], 0}, {a[1], 0}, {a[0], 0});
        perm_cycle({a[3], 5}, {a[2], 3}, {a[1], 3}, {a[0], 3});
        perm_cycle({a[3], 2}, {a[2], 6}, {a[1], 6}, {a[0], 6});
    }
}


void Cubert::g_move(int direction) {
    int f = 2, a[4] = {0, 3, 5, 1};
    if (direction == 0) {
        perm_cycle({f, 0}, {f, 2}, {f, 8}, {f, 6});
        perm_cycle({f, 1}, {f, 5}, {f, 7}, {f, 3});
        perm_cycle({a[0], 6}, {a[1], 0}, {a[2], 2}, {a[3], 8});
        perm_cycle({a[0], 7}, {a[1], 3}, {a[2], 1}, {a[3], 5});
        perm_cycle({a[0], 8}, {a[1], 6}, {a[2], 0}, {a[3], 2});
    }
    if (direction == 1) {
        perm_cycle({f, 6}, {f, 8}, {f, 2}, {f, 0});
        perm_cycle({f, 3}, {f, 7}, {f, 5}, {f, 1});
        perm_cycle({a[3], 8}, {a[2], 2}, {a[1], 0}, {a[0], 6});
        perm_cycle({a[3], 5}, {a[2], 1}, {a[1], 3}, {a[0], 7});
        perm_cycle({a[3], 2}, {a[2], 0}, {a[1], 6}, {a[0], 8});
    }
}

void Cubert::r_move(int direction) {
    int f = 3; // face
    std::array<int, 4> a = {0, 4, 5, 2}; // adjacents
    // direction=0 or 1 (Cw/ccw)
    if (direction == 0) {
        perm_cycle({f, 0}, {f, 2}, {f, 8}, {f, 6});
        perm_cycle({f, 1}, {f, 5}, {f, 7}, {f, 3});
        perm_cycle({a[0], 8}, {a[1], 0}, {a[2], 8}, {a[3], 8});
        perm_cycle({a[0], 5}, {a[1], 3}, {a[2], 5}, {a[3], 5});
        perm_cycle({a[0], 2}, {a[1], 6}, {a[2], 2}, {a[3], 2});
    } else if (direction == 1) {
        perm_cycle({f, 6}, {f, 8}, {f, 2}, {f, 0});
        perm_cycle({f, 3}, {f, 7}, {f, 5}, {f, 1});
        perm_cycle({a[3], 8}, {a[2], 8}, {a[1], 0}, {a[0], 8});
        perm_cycle({a[3], 5}, {a[2], 5}, {a[1], 3}, {a[0], 5});
        perm_cycle({a[3], 2}, {a[2], 2}, {a[1], 6}, {a[0], 2});
    }
}


void Cubert::b_move(int direction) {
    int f = 4; // face
    std::array<int, 4> a = {0, 1, 5, 3}; // adjacents
    // direction=0 or 1 (Cw/ccw)
    if (direction == 0) {
        perm_cycle({f, 0}, {f, 2}, {f, 8}, {f, 6});
        perm_cycle({f, 1}, {f, 5}, {f, 7}, {f, 3});
        perm_cycle({a[0], 0}, {a[1], 6}, {a[2], 8}, {a[3], 2});
        perm_cycle({a[0], 1}, {a[1], 3}, {a[2], 7}, {a[3], 5});
        perm_cycle({a[0], 2}, {a[1], 0}, {a[2], 6}, {a[3], 8});
    }
    if (direction == 1) {
        perm_cycle({f, 0}, {f, 6}, {f, 8}, {f, 2});
        perm_cycle({f, 1}, {f, 3}, {f, 7}, {f, 5});
        perm_cycle({a[3], 2}, {a[2], 8}, {a[1], 6}, {a[0], 0});
        perm_cycle({a[3], 5}, {a[2], 7}, {a[1], 3}, {a[0], 1});
        perm_cycle({a[3], 8}, {a[2], 6}, {a[1], 0}, {a[0], 2});
    }
}

void Cubert::y_move(int direction) {
    int f = 5; // face
    std::array<int, 4> a = {1, 2, 3, 4}; // adjacents
    // direction=0 or 1 (Cw/ccw)
    if (direction == 0) {
        perm_cycle({f, 0}, {f, 2}, {f, 8}, {f, 6});
        perm_cycle({f, 1}, {f, 5}, {f, 7}, {f, 3});
        perm_cycle({a[0], 6}, {a[1], 6}, {a[2], 6}, {a[3], 6});
        perm_cycle({a[0], 7}, {a[1], 7}, {a[2], 7}, {a[3], 7});
        perm_cycle({a[0], 8}, {a[1], 8}, {a[2], 8}, {a[3], 8});
    }
    if (direction == 1) {
        perm_cycle({f, 0}, {f, 6}, {f, 8}, {f, 2});
        perm_cycle({f, 1}, {f, 3}, {f, 7}, {f, 5});
        perm_cycle({a[3], 6}, {a[2], 6}, {a[1], 6}, {a[0], 6});
        perm_cycle({a[3], 7}, {a[2], 7}, {a[1], 7}, {a[0], 7});
        perm_cycle({a[3], 8}, {a[2], 8}, {a[1], 8}, {a[0], 8});
    }
}

Cubert::Cubert(std::string seed) {
    cube = {'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
            'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
            'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
            'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
            'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
            'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'};

    run_moves(seed);
}
Cubert::Cubert() {
    cube = {'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
            'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
            'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g',
            'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r',
            'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',
            'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y'};
}
Cubert::Cubert(Cubert &c) {
    cube=std::vector<char>(c.cube);
}

void Cubert::print_cube() {
    std::cout << "{";
    for (int i = 0; i < 6; i++) {
        std::cout << "{";
        for (int j = 0; j < 9; j++) {
            std::cout << cube[i*9 + j];
        }
        if (i != 5) {
            std::cout << "}," << std::endl;
        } else {
            std::cout << "}}" << std::endl;
        }
    }
}
void Cubert::run_moves(std::string command) {
    int i = 0;
    while (i < command.length()) {
        char current = command[i];
        int dir, times;
        if (i + 1 < command.length() && command[i + 1] == '\'') {
            dir = 1;
            i = i + 2;
            times = 1;
        } else if (i + 1 < command.length() && command[i + 1] == '2') {
            dir = 0;
            i = i + 2;
            times = 2;
        } else {
            dir = 0;
            i = i + 1;
            times = 1;
        }

        int move_idx;
        if (current == 'w') {
            move_idx = 0;
        } else if (current == 'o') {
            move_idx = 1;
        } else if (current == 'g') {
            move_idx = 2;
        } else if (current == 'r') {
            move_idx = 3;
        } else if (current == 'b') {
            move_idx = 4;
        } else if (current == 'y') {
            move_idx = 5;
        }

        for (int j = 0; j < times; j++) {
            (this->*moves[move_idx])(dir);
        }
    }
}
