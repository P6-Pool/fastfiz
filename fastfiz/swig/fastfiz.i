%module fastfiz

%{
#include "FastFiz.h"
#include "Rules.h"
#include "Noise.h"
#include "AIBase.h"
#include "LogFile.h"
#include "StopWatch.h"
%}

// %ignore operator<;
%ignore operator>>;

%include "FastFiz.h"
%include "Rules.h"
%include "Noise.h"
%include "AIBase.h"
%include "LogFile.h"
%include "StopWatch.h"

