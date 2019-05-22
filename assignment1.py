import random, time

#  Utilities
#----------------------------------------------------------------

# Random Arrays generator
# IN : nb of arrays, minimal size (all args are optionnal)
def randomArrays(nb = 160,size = 10):
    arr = []
    for i in range(0,nb):
        #print("Array "+str(i))
        temp = []
        for j in range(0,size):  
            val = random.randint(0,1000)
            #print("\tValue of "+str(j)+" = "+str(val))
            temp.append(val)
        arr.append(temp)
        if (i != 0 and i%40 == 0):
            size *= 10
            print(size)
    print("[SUCCESS] Array randomization finished")
    return arr

# Seconds to string
# IN : Running time in seconds
def stos(t):
    t = int(t)
    m = int(t // 60)
    if (m == 1):
        return str("1 minute and "+str(t-60)+" seconds")
    elif (m > 1):
        return str(str(m)+" minutes and "+str(t-(60*m))+" seconds")
    else:
        return str(str(t)+" seconds")

# Sort verification
# IN : Array of arrays to verify
def isSorted(a):
    flag = True
    for e in a:
        i = 1
        while i < len(e):
            if (e[i] < e[i-1]):
                flag = False
            i = i+1
    return flag

#  Insert sort
#----------------------------------------------------------------

# Insert sort
# IN : array to sort
def insertSort(array):
    a = array.copy() 
    n = len(a)
    for j in range(1,n):
        e = a[j]
        i = j-1
        while (i>-1 and a[i]>e):
            a[i+1] = a[i]
            i = i-1
        a[i+1] = e
    return a

#  Merge sort
#----------------------------------------------------------------

# Merge sort - Entry point
# IN : array to sort
def mergeSort(a):
    if (len(a) <= 1):
        #do nothing
        return a
    else:
        l = []
        r = []
        for x in range(0, len(a)):
            if (x < len(a)/2):
                l.append(a[x])
            else:
                r.append(a[x])
        
        l = mergeSort(l)
        r = mergeSort(r)

        return merge(l,r)

# Merge - Utility function for Merge Sort
def merge(l,r):
    d = []
    nlen = len(r)+len(l)
    l.append(999999999)
    r.append(999999999)
    i = 0
    j = 0
    for k in range(0, nlen):
        if l[i] <= r[j]:
            d.append(l[i])
            i = i+1
        else:
            d.append(r[j])
            j = j+1    
    return d

#  Heapsort
#----------------------------------------------------------------

# Heapsort - Entry point
# IN : array to sort
def heapsort(a):
    n = len(a)
    buildMaxHeap(a)
    for i in range(n, 1):
        a[1], a[i] = a[i], a[1]
        n = n-1
        maxHeapify(a, 1)

# MaxHeapify - Utility function for Heapsort
def maxHeapify(a, i):
    l = 2*i
    r = 2*i + 1
    if l <= len(a) and a[l]>a[i]:
        largest = l
    else:
        largest = i
    if r <= len(a) and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        maxHeapify(a, largest)

# BuildMaxHeap - Utility function for Heapsort
def buildMaxHeap(a):
    for i in range(int(len(a)/2), 0):
        maxHeapify(a, i)


#  Quicksort
#----------------------------------------------------------------

# Quicksort - Entry point
# IN : array to sort, beginning point, finish point
def quicksort(a, p, r):
    if (p < r):
        q = partition(a, p, r)
        quicksort(a, p, q-1)
        quicksort(a, q+1, r)

# Partition - Utility function for Quicksort
def partition(a, p, r):
    x = a[r]
    i = p-1
    for j in range(p, r):
        if (a[j] < x):
            i = i+1
            a[i], a[j] = a[j],a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1

# Generate an array of arrays of various sizes with random values
test = randomArrays()

# Copys this array to work on the same environment for each algorithm
test2 = test.copy()
test3 = test.copy()
test4 = test.copy()

# Contains the outputs
out = []

# Insertion sort
istart = time.time()
for it in range(0,len(test)):
    out.append(insertSort(test[it]))
    print("Processed insert sort "+str(it+1)+" out of "+str(len(test)))
iend = time.time()
itimeFinal = iend-istart  

#Merge sort
mstart = time.time()
for it in range(0,len(test2)):
    out.append(mergeSort(test2[it]))
    print("Processed merge sort "+str(it+1)+" out of "+str(len(test2)))
mend = time.time()
mtimeFinal = mend-mstart  

# Heap sort
hstart = time.time()
for it in range(0,len(test3)):
    heapsort(test3[it])
    out.append(test3[it])
    print("Processed heap sort "+str(it+1)+" out of "+str(len(test3)))
hend = time.time()
htimeFinal = hend-hstart  

# Quick sort
qstart = time.time()
for it in range(0,len(test4)):
    quicksort(test4[it], 0, len(test4[it])-1)
    out.append(test4[it])
    print("Processed quick sort "+str(it+1)+" out of "+str(len(test4)))
qend = time.time()
qtimeFinal = qend-qstart  

# Is the output conform to what we are expecting ? (all arrays sorted)
if (isSorted(out)):
    # OK
    print("Successfully passed sorting validation.")

# Display the times
print("Run time for insert sort : "+stos(itimeFinal))
print("Run time for merge sort : "+stos(mtimeFinal))
print("Run time for heap sort : "+stos(htimeFinal))
print("Run time for quick sort : "+stos(qtimeFinal))