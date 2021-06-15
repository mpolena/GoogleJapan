def check_straight(lst):
    '''Checks if parameter passed in is a straight. Returns T/F.'''
    # Create what the straight is supposed to be.
    l = list(range(lst[0],lst[0]+len(lst)))
    t_f = False
    # Compare the two.
    if l == lst:
        t_f = True
    return t_f

def straight(lst): 
    '''Checks if passed list contains one or more straights.'''
    
    if len(lst)%5 != 0:
        return False
    
    first_list, rest_lst = [], []
    lst.sort()
    for num in lst: 
        # For every number in the list
        if num not in first_list and len(first_list) < 5: 
            first_list.append(num)
        else:
            rest_lst.append(num)
    try:
        assert(len(first_list) == 5)
    except AssertionError:
        return False
    # if check_straight returns False, done
    if not check_straight(first_list):
        return False
    # else recurse with remaining list.
    elif len(rest_lst) >= 5:
        return straight(rest_lst)
    return True

if __name__ == "__main__":
    lst1 = [1,2,3,4,5,
            10,6,7,8,9,
            10,11,12,13,14]
    lst2 = [1,2,3,3,4,4,5,5,6,7]
    lst3 = [1,2,3,4,5,
            10,6,7,8,9,
            10,11,12,13,70]
    lst4 = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9]
    lst5 = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 9, 7, 5, 6, 8]

    lst = [lst1, lst2, lst3, lst4, lst5]
    for i in lst:
        #print(sorted(i))
        print(straight(i))
