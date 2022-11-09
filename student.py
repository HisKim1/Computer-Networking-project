#sample input from student

def sort(array):

    # Baseline
    if len(array) < 2:
        return array

    # Pivot the center value
    index = len(array) // 2
    p = array[index]

    # Divide the array based on the pivot
    less = []
    greater = []
    equal = []

    for item in array:
        # Less case
        if item < p:
            less.append(item)

        # Equal case
        elif item == p:
            equal.append(item)

        #Greater case
        elif item > p:
            greater.append(item)

        else:
            print("error")

        return sort(less) + equal + sort(greater)
