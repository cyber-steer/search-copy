#include <Python.h>

static PyObject* sum_list(PyObject* self, PyObject* args) {
    PyObject* input_list;

    if (!PyArg_ParseTuple(args, "O", &input_list)) {
        return NULL;
    }

    if (!PyList_Check(input_list)) {
        PyErr_SetString(PyExc_TypeError, "입력은 리스트여야 합니다.");
        return NULL;
    }

    Py_ssize_t size = PyList_Size(input_list);
    long long sum = 0;

    for (Py_ssize_t i = 0; i < size; ++i) {
        PyObject* item = PyList_GetItem(input_list, i);
        if (!PyLong_Check(item)) {
            PyErr_SetString(PyExc_TypeError, "리스트는 정수만 포함해야 합니다.");
            return NULL;
        }
        sum += PyLong_AsLongLong(item);
    }

    return Py_BuildValue("L", sum);
}

static PyMethodDef SumListMethods[] = {
    {"sum_list", sum_list, METH_VARARGS, "리스트의 모든 요소를 더합니다."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef sumlistmodule = {
    PyModuleDef_HEAD_INIT,
    "sumlist",
    NULL,
    -1,
    SumListMethods
};

PyMODINIT_FUNC PyInit_listTest(void) {
    return PyModule_Create(&sumlistmodule);
}