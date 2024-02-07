#include <Python.h>

int fibonacci_logic(int n);

static PyObject* fibonacci(PyObject* self, PyObject* args) {
    int n;

    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    return Py_BuildValue("i", fibonacci_logic(n));
}

int fibonacci_logic(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci_logic(n - 1) + fibonacci_logic(n - 2);
    }
}

static PyMethodDef FibonacciMethods[] = {
    {"fibonacci", fibonacci, METH_VARARGS, "Calculate the Fibonacci number recursively."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibonacciModule = {
    PyModuleDef_HEAD_INIT,
    "fibonacci",
    NULL,
    -1,
    FibonacciMethods
};

PyMODINIT_FUNC PyInit_fibonacci(void) {
    return PyModule_Create(&fibonacciModule);
}
