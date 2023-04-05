def main():
    array = [31, 72, 10, 32, 18, 95, 25, 50]
    print(sort(array))
def sort_recursive(array, i_begin, i_end):
    if i_end - i_begin < 1 or i_end < 0:
        return
    i_pivot = segregate(array, i_begin, i_end)
    sort_recursive(array, i_begin, i_pivot - 1)
    sort_recursive(array, i_pivot + 1, i_end)
    '''i_check2 = 0
    while(i_check1 != i_pivot and i_check2 != i_pivot):
            
        # Loop through all of the items from 1 to the pivot.
        for i_check1 in range(i_up, i_pivot+1, 1):
            #If the current item is bigger than the largest item, make the largest equal to the current.
            if array[i_check1] > array[i_pivot]:
                switch1 = i_check1
                break
            elif array[i_check1] == array[i_pivot]:
                switch1 = i_pivot
    # If the largest item is bigger than the pivot, switch them.
        for i_check2 in range(i_down, i_pivot-1, -1):
            if array[i_check2] < array[i_pivot]:
                switch2 = i_check2
                break
            elif array[i_check2] == array[i_pivot]:
                switch2 = i_pivot 
            
        array[switch1], array[switch2] = array[switch2], array[switch1]
    i_down = i_pivot
    i_up = 0
    sort(array, i_up, i_down) '''
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
            array[i_up], array[i_down] == array[i_down], array[i_up]
    array[i_up], array[i_pivot] = array[i_pivot], array[i_up]
def sort(array):
    print(sort_recursive(array, 0, len(array)-1))
    
    


        
   

if __name__ == '__main__':
    main()