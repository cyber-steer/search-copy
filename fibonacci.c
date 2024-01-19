#include <Python.h>

static PyObject* fibonacci(PyObject* self, PyObject* args) {
    int n;

    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    int a = 0, b = 1, temp;

    while (n > 0) {
        temp = a;
        a = b;
        b = temp + b;
        n--;
    }

    return Py_BuildValue("i", a);
}

static PyMethodDef FibonacciMethods[] = {
    {"fibonacci", fibonacci, METH_VARARGS, "Calculate the Fibonacci number."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef fibonaccimodule = {
    PyModuleDef_HEAD_INIT,
    "fibonacci",
    NULL,
    -1,
    FibonacciMethods
};

PyMODINIT_FUNC PyInit_fibonacci(void) {
    return PyModule_Create(&fibonaccimodule);
}
