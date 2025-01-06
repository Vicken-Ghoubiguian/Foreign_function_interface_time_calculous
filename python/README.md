# Python samples

## Contents

* [How to deploy the 'time_calculous' C library example by example ?](#how_to_deploy_example_by_example),
* [Useful links](#useful_links),

<a name="how_to_deploy_example_by_example"></a>
## How to deploy the 'time_calculous' C library example by example ?

<a name="in_general"></a>
### In general

To begin, you have to create your project's directory following the command bellow :

```bash
mkdir your_project_directory
```

In a second time, you have to position using the command bellow :

```bash
cd your_project_directory
```

In a third time, create a Python file using the command bellow :

```bash
touch main.py
```

In a fourth time, you have to clone the [time_calculous](https://github.com/Vicken-Ghoubiguian/time_calculous) C library in the `your_project_directory` directory using the command bellow :

```bash
git clone https://github.com/Vicken-Ghoubiguian/time_calculous
```

After this, you have to generate the '.so' file (that is the shared library file) following the command bellow (again) :

```bash
cc -fPIC -shared -o time_calculous.so time_calculous/time_calculous/time_calculous.c
```

After that, in a fifth time, you have to open the new created file following the command bellow :

```bash
nano main.py
```

Then, you have to write the code below inside the 'main.py' file (all explanations are given in the comments) :

```python
#
from ctypes import *

#
so_time_calculous_file = "time_calculous.so"

#
time_calculous_functions = CDLL(so_time_calculous_file)

#
print(time_calculous_functions.number_of_weeks_in_a_year_according_to_the_iso_norm(2025))

#
print(time_calculous_functions.wished_number_in_year_is_day_in_choosen_year(1, 1, 2025))

#
printf(time_calculous_functions.number_of_days_in_choosen_month_in_choosen_year(1, 2025))
```

Finally, you can execute this script using the last command bellow :

```bash
python main.py
```

Congratulations ! It is now YOUR turn to play with all of that examples in the 'python' folder of this repository.

<a name="for_simpliest"></a>
### For 'simpliest_sample'

<a name="for_tkinter"></a>
### For 'tkinter_sample'

<a name="for_flask"></a>
### For 'flask_sample'

<a name="for_flask_restx"></a>
### For 'flask_restx_sample'

<a name="useful_links"></a>
## Useful links

* [Calling C Functions from Python](https://www.digitalocean.com/community/tutorials/calling-c-functions-from-python),
* [ctypes — A foreign function library for Python](https://docs.python.org/3/library/ctypes.html)
