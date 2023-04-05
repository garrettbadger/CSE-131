# 1. Name:
#      Garrett Badger
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program uses recursion to sort a list.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this assignment was the recursion. Figuring out how to properly
#      utilize recursion took me the longest to figure out.
# 5. How long did it take for you to complete the assignment?
#      3

def main():
    # Start the program 
    get_array()
    

def sort(array):
    # This will call sort_recursive which starts the recursive sorting process.
    sort_recursive(array, 0, len(array)-1)

def sort_recursive(array, i_begin, i_end):\
    # Check the bounds of the sublist
    if i_end - i_begin < 1 or i_end < 0:
        return
    i_pivot = segregate(array, i_begin, i_end)
    sort_recursive(array, i_begin, (i_pivot - 1))
    sort_recursive(array, (i_pivot + 1), i_end)
    
    
def segregate(array, i_begin, i_end):
    '''This function's main purpose is to segregate the list by finding the pivot value.'''
    # Set up variables
    if i_begin == i_end:
        return i_begin
    i_pivot = (i_begin + i_end) // 2
    i_up = i_begin
    i_down = i_end
    # Use a loop to sort through values
    while i_up < i_down:
        # Here we determine if we have found the pivot or if we keep looking
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
        while i_up < i_down and array[i_down] >= array[i_pivot]:
            i_down -= 1
        # This is where we assign the pivot
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
        # Swap the values on either side of the pivot
            array[i_up], array[i_down] = array[i_down], array[i_up]
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    return i_up


    
    
def get_array():
    '''The main program lets the user decide to custom input a list to sort or run the test cases'''
    tests = input('T = run test cases C = custom input> ')
    if tests == 'T':
        test_cases()
    elif tests == 'C':
        stop = False
        array = []
        while not stop:
            user_in = input("Please input an alphanumeric character to put in the list (type \".\" to quit)")
            
            if user_in != '.':
                if len(user_in) == 1 and ord(user_in) < ord('a'):
                    user_in = '0' + user_in
                array.append(user_in)
            else:
                stop = True
        sort(array)

def test_cases():
    '''This function runs a variety of pre-made test cases as labeled by the print statements'''
    print("Unsorted list")
    test1=[10,1,5,3]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Unsorted alpha list")
    test1=['a','z','b','x','c','y']
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Unsorted negative list")
    test1=[0,-1,-50,-25,-17]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Unsorted float list")
    test1=[0,0.01,9999,0.0001,-9999]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Unsorted mixed case list")
    test1=['a','99','2','x','1','y']
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Single element list")
    test1=[1]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Reverse sorted list")
    test1=[5,4,3,2,1]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Sorted list")
    test1=[1,2,3,4,5]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Unsorted list with duplicates")
    test1=[10,1,5,3,10,5,1,3]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')
    print("Empty list")
    test1=[]
    print(f'Before sort array: {test1}')
    sort(test1)
    print(f'After sort array: {test1}')
    print('----------------')

if __name__ == '__main__':
    main()