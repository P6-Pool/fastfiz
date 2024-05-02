# Compiler and compiler flags
CC = gcc
JDKLOC := $(shell readlink -f $(shell which javac) | sed "s:bin/javac::")
SWIGFLAGS = -c++ -java -package JFastfiz -Iinclude -outdir $(MODULEDIR)
CFLAGS = -fPIC -std=c++11 \
         -Iinclude \
         -I$(JDKLOC)/include \
         -I$(JDKLOC)/include/linux

# Source files
SRCDIR = src
SRCFILES = $(wildcard $(SRCDIR)/*.cpp)
SRCWRAP = swig/fastfiz_wrap.cxx

# Object files
OBJFILES = $(SRCFILES:.cpp=.o)

# Target bundle
TARGET = libfastfiz.so

# Target module
MODULEDIR = ../JFastfiz

# Main target
all: $(TARGET)

# Compile fastfiz_wrap.cxx
$(SRCWRAP): swig/fastfiz.i
	swig $(SWIGFLAGS) $<

# Compile source files
%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

# Link object files to create the final shared library
$(TARGET): $(OBJFILES) $(SRCWRAP)
	$(CC) $(CFLAGS) -shared $(OBJFILES) $(SRCWRAP) -o $@ $(LDFLAGS) -lgsl -lstdc++

# Clean rule
clean:
	rm -f $(OBJFILES) $(SRCWRAP) $(TARGET)
	rm -f $(MODULEDIR)/*.java
