# C++ version of Cubert, courtesy of chatGPT
(yes I did literally copy and paste the other version into chatgpt to make this)

This has the exact same functionality as the python version, but if you plan to make your solver in c++, it might be easier to start with this version of the Cubert class.

To compile and run the main program, as with the python version, simply type 
```
make
```
 (if make is installed on your system), or compile it with
```
g++ main.cpp Cubert.cpp -o main
```

Then, run it with `./main "[optional seed]"` and the output will be the same as before
eg. `./main "w2g'r2w'"`

Following the example of main.cpp, and the incoherent example of test.cpp, you can make your own main program using the Cubert library, so you don't even have to deal with the command line. This is useful if you intend to do a graph-like exploration, and would like to save a copy of the current cube state, or explore multiple directions at once. you simply need to include `#include "Cubert.hpp"` at the top of your file, and compile it as shown above for `main`, or modify the makefile accordingly.
