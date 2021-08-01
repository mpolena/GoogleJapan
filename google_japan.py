import argparse


def check_straight(lst):
    '''Checks if parameter passed in is a straight. Returns T/F.'''
    # Create a straight.  (passed in straight is assumed to be sorted)
    print(lst)
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
    lst.sort()
    
    first_list, rest_lst = [], []
    for num in lst: 
        #  Fill first list with 5 unique elements.
        if num not in first_list and len(first_list) < 5: 
            first_list.append(num)
        # Everything else goes to the rest list.
        else:
            rest_lst.append(num)
    # Sanity check.
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
    
    parser = argparse.ArgumentParser("Determine if a list of integers is a straight.")
    parser.add_argument('-l','--list', nargs='+', type=int, help='<Required> Set flag', required=True)
    
    for _, value in parser.parse_args()._get_kwargs():
        if value is not None:
            lst = value
    assert(type(lst)==list)
    #for l in lst:
    print(straight(lst))
