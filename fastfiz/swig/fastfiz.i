%module fastfiz

%{
#include "FastFiz.h"
#include "Rules.h"
%}

%ignore operator<;
%ignore operator>>;

%include "FastFiz.h"
%include "Rules.h"


