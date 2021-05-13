from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    def hoare(lst,low,high,pivot_fn):
        pivot = pivot_fn(lst,low,high)
        l = low
        h = high
        while True:
            while True:
                if l == high or lst[l] >= pivot:
                    break
                l+=1

            while True:
                if lst[h] <= pivot:
                    break
                h-=1
            if l >= h:
                return [lst,h]
            else:
                temp = lst[l]
                lst[l] = lst[h]
                lst[h] = temp
            
    if high-low <= 1:
        if low >=0 and high< len(lst) and low<= high and lst[high] < lst[low]:
            temp = lst[low]
            lst[low] = lst[high]
            lst[high] = temp
        return lst
    else:
        x = hoare(lst,low,high,pivot_fn)
        lst = x[0]
        lst = qsort(lst,low,x[1],pivot_fn)
        lst = qsort(lst,x[1]+1,high,pivot_fn)
    return lst
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    return low
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    return random.randint(low, high)
    
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    frst = lst[low]
    midd = lst[(low+high)//2]
    last = lst[high]
    if (frst>= midd and frst<=last) or (frst>=last and frst<=midd):
        return low
    elif (last>=midd and last<=frst) or (last>=frst and last<=midd):
        return high
    else:
        return (low+high)//2
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()
