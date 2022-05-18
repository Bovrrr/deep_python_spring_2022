#include <Python.h>

int fibonacci(int n)
{
    if (n < 2)
        return 1;
    return fibonacci(n-2) + fibonacci(n-1);
}

static PyObject* utils_fibonacci(PyObject *self, PyObject *args)
{
    PyObject *result = NULL;

    int n;
    if (PyArg_ParseTuple(args, "i", &n)) {
        result = Py_BuildValue("L", fibonacci(n));
    }
    return result;
}

static char fibonacci_docs[] =
    "fibonacci(n): Return n'th Fibonacci sequence number\n";

static PyObject* utils_sum(PyObject *self, PyObject *args)
{
    PyObject *result = NULL;
    long max_len;

    if (!PyArg_ParseTuple(args, "Ol", &result, &max_len)) {
        printf("ERROR: Failed to parse argument\n");
        return NULL;
    }
    long len = PyList_Size(result);
    long res = 0;
    for (int i = 0; i < max_len && i < len; ++i) {
        PyObject *tmp = PyList_GetItem(result, i);
        res += PyLong_AsLong(tmp);
    }
    return Py_BuildValue("i", res);
}

static char sum_docs[] =
    "sum(List[int], int): Return sum of sequence number\n";

static PyObject* utils_dummy(PyObject *self, PyObject *args)
{
    return Py_BuildValue("[i, i]", 100, 500);
}

static char dummy_docs[] =
    "dummy(): return list of two integers\n";

static PyMethodDef utils_module_methods[] = {
    {"fibonacci", (PyCFunction)utils_fibonacci, METH_VARARGS, fibonacci_docs},
    {"accumulate", (PyCFunction)utils_sum, METH_VARARGS, sum_docs},
    {"dummy", (PyCFunction)utils_dummy, METH_NOARGS, dummy_docs},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef utils_module_definition = {
    PyModuleDef_HEAD_INIT,
    "utils",
    "Extension mudule that provides fibonacci sequence function",
    -1,
    utils_module_methods
};

PyMODINIT_FUNC PyInit_utils(void) {
    Py_Initialize();
    return PyModule_Create(&utils_module_definition);
}
