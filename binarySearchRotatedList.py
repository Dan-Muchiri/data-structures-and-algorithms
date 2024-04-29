if __name__ == '__main__':
    # Problem
    # We need to write a program to find the number of times a list of numbers arranged in increasing order is rotated. We also need to minimize the number of times we access the elements from the list.

    #Input
    #Cards: number list in increasing order

    #Output
    #Rotations: No of times rotated

    #Tests
    tests =[]
    #1. Rotated equal to number of items or not rotated at all:
    tests.append({
        'input':[2,3,4,5,6,7,8,9],
        'output': 0
    })
    #2. Rotated less than middle point:
    tests.append({
        'input':[8,9,2,3,4,5,6,7],
        'output': 2
    })
    #3. Rotated more than middle point:
    tests.append({
        'input':[4,5,6,7,8,9,2,3],
        'output': 6
    })
    #6.Cards is empty:
    tests.append({
        'input':[],
        'output': -1
    })

    # Solution
    # 1. Look at the middle index.
    # 2. If the previous element is greater than the middle element, return the middle index.
    # 3. If the element at the start is less than the middle element, it means the pivot is on the right side, so update the start.
    # 4. If the element at the end is greater than the middle element, it means the pivot is on the left side, so update the end.
    # 5. Repeat steps 1-4 until the start is greater than the end or the rotation is found.
    # 6. If no rotation is found, return -1.

    def check_rotations(cards):
        if not cards:
            return -1
        start = 0
        end = len(cards)-1

        while start<=end:
            mid_index = (start + end)//2
            mid_no =cards[mid_index]
            prev_no = cards[mid_index-1]

            print('start:', start, 'end:',end, 'mid:', mid_index, 'midNo:', mid_no)

            if prev_no>mid_no:
                return mid_index   
            elif cards[start]<mid_no:
                start = mid_index + 1
            elif cards[end]>mid_no:
                end = mid_index -1

        return 0
        



    for test in tests:
        if check_rotations(test['input']) == test['output']:
            print ('Correct')
        else:
            print ('Wrong')

