## Note

Activity monitor will show `python 3.8`

### Go Into Desired Directory

```
 cd Refactored_Py_DS_ML_Bootcamp-master
```

### Open Jupyter Notebook

```
jupyter notebook
```

Jupyter Notebook should be open on `http://localhost:8888/tree`

### Execute In Code Cell

`SHIFT + ENTER`

### Go Down To Next Code Cell

`ALT + ENTER`

### create array and call numpy. then have it as 0-50 then create 2d matrix of 5 rows of 10 digits

```
import numpy as np
arr_2d = np.arange(50).reshape(5,10)
```

should become:

```
array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
       [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
       [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]])
```

- Space Evenly

```
np.arange(0,11,2) # == array([ 0,  2,  4,  6,  8, 10])
```

- Linspace

```
np.linspace(0,1, 20) # ==

array([0.        , 0.05263158, 0.10526316, 0.15789474, 0.21052632,
       0.26315789, 0.31578947, 0.36842105, 0.42105263, 0.47368421,
       0.52631579, 0.57894737, 0.63157895, 0.68421053, 0.73684211,
       0.78947368, 0.84210526, 0.89473684, 0.94736842, 1.        ])
```
