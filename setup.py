from distutils.core import setup, Extension

setup(name="fibonacci_and_sum",
      ext_modules=[Extension("fibonacci", ["fibonacci.c"])]
)





















# from distutils.core import setup, Extension
#
# setup(name="fibonacci_and_sum",
#       ext_modules=[Extension("fibonacci", ["fibonacci.c"]),
#                    Extension("listTest", ["listTest.c"])])
