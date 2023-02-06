#OS Stuff
ifeq ($(OS),Windows_NT) 
RM = del /Q /F
CP = copy /Y
ifdef ComSpec
SHELL := $(ComSpec)
endif
ifdef COMSPEC
SHELL := $(COMSPEC)
endif
else
RM = rm -rf
CP = cp -f
endif
#<------

#list all your programs/test exe output files here
#This makefile assumes that each executable corresponds to a
#*.cpp file with the same name, eg main.cpp -> main
#once you add a program that includes "Cubert.hpp", add it 
# to the programs list separated by a space
programs = main test


#auto find correspeonding .cpp and .o files
cpp_files = $(programs:=.cpp) Cubert.cpp
o_files=$(programs:=.o) Cubert.o

#If you're on windows, it might add a .exe against your will
exe_files=$(programs:=.exe) 

all: $(programs)

.PHONY: clean
.SECONDARY: $(o_files)


%: %.o Cubert.o
	g++ $(LDFLAGS) $+ $(LOADLIBES) $(LDLIBS) -o $@

clean:
	-$(RM) $(o_files) $(programs) $(exe_files) -f