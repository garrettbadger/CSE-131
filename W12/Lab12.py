def main():
    array = get_array()
    sort(array)
    print(array)

def sort(array):
    sort_recursive(array, 0, len(array)-1)

def sort_recursive(array, i_begin, i_end):
    if i_end - i_begin < 1 or i_end < 0:
        return
    i_pivot = segregate(array, i_begin, i_end)
    sort_recursive(array, i_begin, (i_pivot - 1))
    sort_recursive(array, (i_pivot + 1), i_end)
    
def segregate(array, i_begin, i_end):
    if i_begin == i_end:
        return i_begin
    i_pivot = (i_begin + i_end) // 2
    i_up = i_begin
    i_down = i_end

    while i_up < i_down:
        while i_up < i_down and array[i_up] < array[i_pivot]:
            i_up += 1
        while i_up < i_down and array[i_down] >= array[i_pivot]:
            i_down -= 1
        if i_up < i_down:
            if i_down == i_pivot:
                i_pivot = i_up
            elif i_up == i_pivot:
                i_pivot = i_down
            array[i_up], array[i_down] = array[i_down], array[i_up]
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
    return i_up


    
    
def get_array():
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
    return array
   

if __name__ == '__main__':
    main()