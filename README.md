
# NumPy Analyzer (DataAnalytics)

## 📌 Overview
**NumPy Analyzer** is a menu-driven Python console application designed to help students and beginners understand and practice **NumPy array operations** interactively.  
It supports **1D, 2D, and 3D arrays** and covers most concepts required for **AI & ML / Data Analytics coursework**.

## 🚀 Features

### 1️⃣ Array Creation
- Create **1D arrays**
- Create **2D matrices**
- Create **3D arrays**
- Automatically displays array shape


### 1D Array
```python
element = list(map(int, input().split()))
self.arr = np.array(element)
print(self.arr.shape)
```

### 2D Array
```python
element = list(map(int, input().split()))
self.arr1 = np.array(element).reshape(row, col)
print(self.arr1.shape)
```

### 3D Array
```python
element = list(map(int, input().split()))
self.arr2 = np.array(element).reshape(layer, row, col)
print(self.arr2.shape)
```

---

### 2️⃣ Indexing & Slicing
#### Indexing
- 1D indexing
- 2D indexing (row, column)
- 3D indexing (layer, row, column)
- Handles invalid index errors

### 1D Indexing
```python
print(self.arr[idx])
```

### 2D Indexing
```python
print(self.arr1[r, c])
```

### 3D Indexing
```python
print(self.arr2[l, r, c])
```

Error handling:
```python
except IndexError:
    print("Invalid Index")
```


#### Slicing
- 1D slicing (start, stop, step)
- 2D slicing (rows & columns)
- 3D slicing (layers, rows, columns)
### 1D Slicing
```python
self.arr[start:end:step]
```

### 2D Slicing
```python
self.arr1[rs:re:rst, cs:ce:cst]
```

### 3D Slicing
```python
self.arr2[ls:le:lst, rs:re:rst, cs:ce:cst]
```
---

### 3️⃣ Combine & Split Arrays (2D)
- **Combine** two matrices using vertical stacking
### Combine (Vertical Stack)
```python
combine = np.vstack((self.arr1, ar))
```
- **Split** a matrix into multiple parts using `array_split`
```python
np.array_split(self.arr1, n, axis=0)
```

---

### 4️⃣ Search, Sort & Filter
- Search values using `np.where`
- Sort rows using `np.sort`
- Filter values greater than a threshold
### Search
```python
np.where(self.arr1 == val)
```

### Sort
```python
np.sort(self.arr1, axis=1)
```

### Filter
```python
self.arr1[self.arr1 > th]
```

---

### 5️⃣ Mathematical Operations
```python
res = self.arr1 + n_arr   # Addition
res = self.arr1 - n_arr   # Subtraction
res = self.arr1 * n_arr   # Multiplication
res = self.arr1 / n_arr   # Division
```
---

### 6️⃣ Aggregates & Statistics
```python
self.arr1.sum()
self.arr1.mean()
np.median(self.arr1)
self.arr1.std()
self.arr1.var()

---

### 7️⃣ Min, Max & Percentiles
```python
np.min(self.arr1)
np.max(self.arr1)
np.percentile(self.arr1, p)

---

### 8️⃣ Correlation
- Computes correlation matrix using `np.corrcoef`
- Useful in data analysis & ML
```python
np.corrcoef(self.arr1, rowvar=False)

---

### 9️⃣ Dot Product & Matrix Multiplication
- **Dot Product** (flattened vectors)
np.dot(self.arr1.flatten(), arr2.flatten())

- **Matrix Multiplication** with dimension validation
result = self.arr1 @ mat_b
---

## 🧠 Concepts Covered
- NumPy arrays
- Reshaping
- Indexing & slicing
- Broadcasting
- Aggregations
- Statistics
- Linear algebra basics

---

## 🛠 Requirements
- Python 3.x
- NumPy

Install NumPy if not available:
```bash
pip install numpy
```

---

## ▶️ How to Run
1. Save the file as:
```bash
Numpy Analyser.py
```
2. Run the program:
```bash
python "Numpy Analyser.py"
```
3. Follow the on-screen menu options

---
---

## ⚠️ Notes
- Always create arrays before performing operations
- 2D array is mandatory for most advanced operations
- Input validation is added to avoid crashes

---

## 🎓 Educational Use
This project is **perfect for practical exams**, assignments, and understanding NumPy deeply with hands-on practice.

