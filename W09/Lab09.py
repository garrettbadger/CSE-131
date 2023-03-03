# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This program is meant to sort a python array by sorting finding presorted sub-arrays and combining them.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was coming up with the combine portion of the program.
#      I ended up going off of the instructors solution instead of my own to create the program.
# 5. How long did it take for you to complete the assignment?
#      It probably took me around 4 hours.
def main():
    '''The main program lets the user decide to custom input a list to sort or run the test cases'''
    tests = input('T = run test cases C = custom input> ')
    if tests == 'T':
        test_cases()
    elif tests =='C':
        stop = False
        array = []
        while not stop:
            user_in = input("Please input an alphanumeric character to put in the list (type \".\" to quit)")
            if user_in != '.':
                array.append(user_in)
            else:
                stop = True
        print(sort(array))
    else:
        print('You did not enter T or C please enter one of those to run the program.')
    
def test_cases():
    '''This function runs a variety of pre-made test cases as labeled by the print statements'''
    print("Unsorted list")
    test1=[10,1,5,3]
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Unsorted alpha list")
    test1=['a','z','b','x','c','y']
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Unsorted negative list")
    test1=[0,-1,-50,-25,-17]
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Unsorted float list")
    test1=[0,0.01,9999,0.0001,-9999]
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Unsorted mixed case list")
    test1=['a','99','2','x','1','y']
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Single element list")
    test1=[1]
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Reverse sorted list")
    test1=[5,4,3,2,1]
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Sorted list")
    test1=[1,2,3,4,5]
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    print("Unsorted list with duplicates")
    test1=[10,1,5,3,10,5,1,3]
    print(f'Before sort array: {test1}')
    print(f'After sort array: {sort(test1)}')
    print('----------------')
    
def sort(array):
    '''This function sorts the array that is passed in into sorted sub-lists'''
    size = len(array)
    src = array
    des = [0] * size
    num = 2
    while num > 1:
        num = 0
        begin1 = 0
        while begin1 < size:
            end1 = begin1 + 1
            while end1 < size and src[end1 - 1] <= src[end1]:
                end1 += 1
            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            while end2 < size and src[end2 - 1] <= src[end2]:
                end2 += 1
            num += 1
            #Combine the two sorted sub arrays into the destination array
            des = combine(src, des, begin1, begin2, end2)
            begin1 = end2
        #Switch the source and destination arrays
        src, des = des, src
    return src

def combine(src, des, begin1, begin2, end2):
    '''This function combines the two sorted sub-lists'''
    end1 = begin2
    for i in range(begin1, end2):
        if ((begin1 < end1) and (begin2 == end2 or src[begin1] < src[begin2])):
            des[i] = src[begin1]
            begin1 += 1
        else:
            des[i] = src[begin2]
            begin2 += 1
    return des

if __name__ == "__main__":
    main()