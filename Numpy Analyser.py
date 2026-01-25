import numpy as np


class DataAnalytics:
    def __init__(self, arr=None, arr1=None, arr2=None):
        self.arr = arr
        self.arr1 = arr1
        self.arr2 = arr2

    def create_arr(self):
        while True:
            print("Array Creation:")
            print("1. 1D array")
            print("2. 2D array")
            print("3. 3D array")
            print("4. Go back")
            ch = int(input("Select the type of array:"))
            if ch == 1:
                element = list(map(int,input("Enter elements separated by space:").split()))
                self.arr = np.array(element)

                print("\nArray created successfully:\n", self.arr)
                print("\nShape:", self.arr.shape)

            elif ch == 2:
                try:
                    row = int(input("Rows:"))   
                    col = int(input("columns:")) 
                    element = list(map(int,input(f"Enter {row*col} elements separated by space:").split()))
                    self.arr1 = np.array(element).reshape(row,col)
                    
                    print("\nArray created successfully:\n", self.arr1)
                    print("\nShape:", self.arr1.shape)
                except:
                    print(f"Invalid..Please enter {row*col} element")

            elif ch == 3:
                try:
                    layer = int(input("Layer:"))
                    row = int(input("Rows:"))   
                    col = int(input("columns:")) 
                    element = list(map(int, input(f"Enter {layer*row*col} elements separated by space: ").split()))
                    self.arr2 = np.array(element).reshape(layer,row,col)
                    
                    print("\nArray created successfully:\n", self.arr2)
                    print("\nShape:", self.arr2.shape)
                except:
                    print(f"Invalid..Please enter {layer*row*col} element")                    

            elif ch == 4:
                break
            else:
                print("Invalid choice")

            print("-"*25)
  
    def index_or_slice(self):
        while True:
            print("\nArray Indexing/Slicing:")
            print("1.Indexing")
            print("2.Slicing")
            print("3.Go back")

            ch = int(input("Enter your choice: "))

            if ch == 1:
                while True:
                    print("\nIndexing Menu:")
                    print("1. 1D Indexing")
                    print("2. 2D Indexing")
                    print("3. 3D Indexing")
                    print("4.Go Back")

                    ch = int(input("Enter choice: "))
                    
                    try:
                        if ch == 1:
                            print(self.arr)
                            idx = int(input("Enter index: "))
                            print("Value:", self.arr[idx])

                        elif ch == 2:
                            print(self.arr1)
                            r = int(input("Enter row index: "))
                            c = int(input("Enter column index: "))
                            print("Value:", self.arr1[r, c])

                        elif ch == 3:
                            print(self.arr2)
                            l = int(input("Enter layer index: "))
                            r = int(input("Enter row index: "))
                            c = int(input("Enter column index: "))
                            print("Value:", self.arr2[l, r, c])
                        elif ch == 4:
                            break
                        else:
                            print("Invalid choice")
                    
                    except IndexError:
                        print("Invalid Index")
           
            elif ch == 2:
                while True:
                    print("\nSlicing Menu:")
                    print("1. 1D slicing")
                    print("2. 2D slicing")
                    print("3. 3D slicing")
                    print("4. Go Back")

                    ch = int(input("Enter choice: "))
                    try:
                        if ch == 1:
                            print(self.arr)
                            s = int(input("start: "))
                            e = int(input("stop :"))
                            st = int(input("step :"))
                            print("Result:",self.arr[r:e:st])
                        
                        elif ch == 2:
                            print(self.arr1)
                            rs = int(input("Row start: "))
                            re = int(input("Row end: "))
                            rst = int(input("step :"))
                            cs = int(input("Col start: "))
                            ce = int(input("Col end: "))
                            cst = int(input("step :"))
                            print("Result:\n", self.arr1[rs:re:rst, cs:ce:cst])
                        
                        elif ch == 3:
                            print(self.arr2)
                            ls = int(input("Layer start: "))
                            le = int(input("Layer end: "))
                            lst = int(input("step :"))
                            rs = int(input("Row start: "))
                            re = int(input("Row end: "))
                            rst = int(input("step :"))
                            cs = int(input("Col start: "))
                            ce = int(input("Col end: "))
                            cst = int(input("step :"))
                            print("Result:\n", self.arr2[ls:le:lst, rs:re:rst, cs:ce:cst])
                        
                        elif ch == 4:
                            break

                        else:
                            print("Invalid")
                    except IndexError:
                        print("Invalid Index")
            elif ch == 3:
                break
            else:
                print("Invalid")


    def combine_split_array(self):
        while True:
            print("\nCombine or Split Arrays on 2D:")
            print("1.Combine Array")
            print("2.Split Array")
            print("3.Go Back")

            try:
                ch = int(input("Enter choice: "))
                if ch == 1:
                    elements = list(map(int,input(f"Enter {self.arr1.size} elements").split()))
                    if len(elements) != self.arr1.size:
                        print(f"You must enter exactly {self.arr1.size} elements!")
                        continue
                    ar = np.array(elements).reshape(self.arr1.shape)
                    combine = np.vstack((self.arr1,ar))
                    print("Combine Array:",combine)
                elif ch == 2:
                    n = int(input("Enter num you want to split: "))
                    result = np.array_split(self.arr1,n,axis=0)
                    print("\nSplit Array:")
                    for i in result:
                        print(i)
                elif ch == 3:
                    break
            except:
                print("Invalid input! Please enter numbers correctly")

    def ser_sor_fil(self):
        print(self.arr1)
        while True:
            print("\nSearch, Sort, and Filter:")
            print("1.Search Array")
            print("2.Sort Array")
            print("3.Filter Array")
            print("4.Go Back")

            ch = int(input("Enter choice: "))
            try:
                if ch == 1:
                    val = int(input("Enter value to search: "))
                    result = np.where(self.arr1 == val)
                    print(result)
                if ch == 2:
                    sorted_arr = np.sort(self.arr1 , axis=1)
                    print(sorted_arr)
                if ch == 3:
                    th = int(input("Enter value and show gt value:"))
                    flt = self.arr1[self.arr1 > th]
                    print(flt)
                elif ch == 4:
                    break
            except IndexError:
                print("Invalid")

    def math_ope(self):
        while True:
            print(" Mathematical Operations:")
            print("1.Addition")
            print("2.Subtraction")
            print("3.Multiplication")
            print("4.Division")
            print("5.Go Back")

        
            ch = int(input("Enter choice: "))
            
            if ch == 5:
                break
            print(self.arr1)
            
            element = list(map(int,input(f"Enter New {self.arr1.size} Element: ").split()))
            if len(element) != self.arr1.size:
                print(f"You must enter exactly {self.arr1.size} elements!")
                continue
            n_arr = np.array(element).reshape(self.arr1.shape)
            print(n_arr)

            if ch == 1:
                res = self.arr1 + n_arr
                print("\nAddition\n",res)
            elif ch == 2:
                res = self.arr1 - n_arr
                print("\nSubtraction\n",res)
            elif ch == 3:
                res = self.arr1 * n_arr
                print("\nMultiplication\n",res)
            elif ch == 4:
                res = self.arr1 / n_arr
                print("\nDivision\n",res)
            else:
                print("Invalid")
            
            print("-"*25)

    def aggregates_statistics(self):
        while True:
            print("\nAggregates and Statistics:")
            print("1.sum")
            print("2.Mean")
            print("3.Median")
            print("4.Standard Deviation")
            print("5.Variance")
            print("6.Go back")
            
            ch = int(input("Enter choice: "))
            
            if ch == 6:
                break
            print(self.arr1)
            if ch == 1:
                print("Sum is: ",self.arr1.sum())
            elif ch == 2:
                print("Mean is: ",self.arr1.mean())
            elif ch == 3:
                print("Median is: ",np.median(self.arr1))
            elif ch == 4:
                print("Standard Deviation is: ",self.arr1.std())
            elif ch == 5:
                print("Variance is: ",self.arr1.var())
            else:
                print("Invalid")
            print("-"*25)
    
    def min_max_perc(self):
          while True:
            print("\nMin,Max,Percentiles:")
            print("1.Min")
            print("2.Max")
            print("3.Percentiles")
            print("4.Go back")
            
            ch = int(input("Enter choice: "))
            if ch == 4:
                break
            print(self.arr1)
            if ch == 1:
                print("Minimum: ",np.min(self.arr1))
            elif ch == 2:
                print("Minimum: ",self.arr1.max())
            elif ch == 3:
                p = int(input("Enter percentile (0–100): "))

                if 0 <= p <= 100:
                    print(f"{p}th Percentile:", np.percentile(self.arr1, p))
                else:
                    print("Percentile must be between 0 and 100")

            else:
                print("Invalid Choice")

    def Correlation(self):
        cor = np.corrcoef(self.arr1, rowvar=False)
        print(cor)

    def  Dot_Matrix(self):
        while True:
            print("1. Dot Product")
            print("2. Matrix Multiplication")
            print("3.Go back")
            ch = int(input("Enter choice: "))
            if ch == 1:
                print(self.arr1)
                print("\nDot Product")

                element = list(map(int, input(f"Enter {self.arr1.size} elements): ").split()))
                if len(element) != self.arr1.size:
                    print(f"You must enter exactly {self.arr1.size} elements!")
                    return
                arr2 = np.array(element)

                result = np.dot(self.arr1.flatten(), arr2.flatten())
                print("Dot Product:", result)

            elif ch == 2:
                print("\nMatrix A:")
                print(self.arr1)
                rows_a, cols_a = self.arr1.shape
                print(f"Matrix A shape: {rows_a} x {cols_a}")

                try:
                    print(f"Matrix B must have {cols_a} rows.")
                    cols_b = int(input("Enter number of columns for Matrix B: "))
                    elements = list(map(int, input(f"Enter {cols_a*cols_b} elements separated by space: ").split()))

                    if len(elements) != cols_a * cols_b:
                        print(f"You must enter exactly {cols_a*cols_b} elements!")
                        return
                    mat_b = np.array(elements).reshape(cols_a, cols_b)
                    result = self.arr1 @ mat_b

                    print("\nMatrix B:")
                    print(mat_b)
                    print("\nResult:")
                    print(result)

                except:
                    print("Invalid input")
            elif ch == 3:
                break
            else:
                print("Invalid")

def main():
    da = DataAnalytics()      

    while True:
        print("-"*25)
        print("1. Create Array")
        print("2. Index/Slice Array")
        print("3. Combine Arrays/Split Array")     
        print("4. Search, Sort, or Filter Arrays") 
        print("5. Mathematical Operations") 
        print("6. Compute Aggregates and Statistics") 
        print("7. Min,Max,Percentiles")
        print("8. Correlation")
        print("9. Dot/Matrix Operations")
        print("10. Exit") 
        ch = int(input("Enter your Choice: "))

        if ch == 1:
            da.create_arr()

        elif ch == 2:
            if da.arr is None and da.arr1 is None and da.arr2 is None:
                print("Please enter array first!")
            else:
                da.index_or_slice()

        elif ch == 3:
            if da.arr1 is None:
                print("Please create 2D array first!")
            else:
                da.combine_split_array()

        elif ch == 4:
            if da.arr1 is None:
                print("Please create 2D array first!")
            else:
                da.ser_sor_fil()

        elif ch == 5:
            if da.arr1 is None:
                print("Please create 2D array first!")
            else:
                da.math_ope()

        elif ch == 6:
            if da.arr1 is None:
                print("Please create 2D array first!")
            else:
                da.aggregates_statistics()

        elif ch == 7:
            if da.arr1 is None:
                print("Please create 2D array first!")
            else:
                da.min_max_perc()

        elif ch == 8:
            if da.arr1 is None:
                print("Please create 2D array first!")
            else:
                da.Correlation()

        elif ch == 9:
            if da.arr1 is None:
                print("Please create 2D array first!")
            else:
                da.Dot_Matrix()

        elif ch == 10:
            break

    

if __name__ == "__main__":
    main()