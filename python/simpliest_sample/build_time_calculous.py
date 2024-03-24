#
from cffi import FFI

#
ffibuilder = FFI()

ffibuilder.cdef("""
 double sqrt(double x); // list all the function prototypes from the
 double sin(double x); // library that we want to use
 """)


#
ffibuilder.set_source("_my_math",
"""
 #include <math.h> // the C header of the library
""",
 library_dirs = [], # here we can provide where the library is located,
 # as we are using C standard library empty list is enough
 libraries = ['m'] # name of the library we want to interface
)

#
ffibuilder.compile(verbose=True)
