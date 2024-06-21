# Compiler and compiler flags
CC = gcc
SWIGFLAGS = -c++ -java -package JFastfiz -Iinclude -outdir $(MODULEDIR)
CFLAGS = -fPIC -std=c++11 \
         -Iinclude \

# Determine OS
UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Linux)
	JDKLOC := $(shell readlink -f $(shell which javac) | sed "s:bin/javac::")
    CFLAGS += -I$(JDKLOC)/include -I$(JDKLOC)/include/linux
endif

ifeq ($(UNAME_S),Darwin)
	JDKLOC := $(shell /usr/libexec/java_home)
    CFLAGS += -I/opt/homebrew/Cellar/gsl/2.8/include -I$(JDKLOC)/include -I$(JDKLOC)/include/darwin
    LDFLAGS = -L/opt/homebrew/Cellar/gsl/2.8/lib -lgsl
endif

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
