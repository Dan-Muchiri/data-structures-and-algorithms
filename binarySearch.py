if __name__ == '__main__':
    # Problem
    # We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access the elements from the list.

    #Input
    #Cards: number list in decreasing order
    #Query: number, whose position in array to be determined

    #Output
    #Position: Index position of query

    #Tests
    tests =[]
    #1. Query in middle:
    tests.append({
        'input':{
            'cards':[13,11,10,7,4,3,1],
            'query':11
        },
        'output': 1
    })
    #2. Query is first element:
    tests.append({
        'input':{
            'cards':[13,11,10,7,4,3,1],
            'query':13
        },
        'output': 0
    })
    #3. Qeury is last element:
    tests.append({
        'input':{
            'cards':[13,11,10,7,4,3,1],
            'query':1
        },
        'output': 6
    })
    #4. Cards has one element:
    tests.append({
        'input':{
            'cards':[1],
            'query':1
        },
        'output': 0
    })
    #5. Cards do not have query:
    tests.append({
        'input':{
            'cards':[13,11,10,7,4,3],
            'query':1
        },
        'output': -1
    })
    #6.Cards is empty:
    tests.append({
        'input':{
            'cards':[],
            'query':1
        },
        'output': -1
    })
    #Numbers not unique:
    tests.append({
        'input':{
            'cards':[13,13,11,11,10,10,10,7,7,7,7,7,4,3,3,3],
            'query':11
        },
        'output': 3
    })

    # Solution
    # 1. Look at the middle index.
    # 2. If it is equal to query, return index
    # 3. If it is less than query decrease the end point to below mid point.
    # 4. If it is more than query increase the start point to above mid point.
    # 5  If none found return -1


    def locate_card(cards,query):
        start = 0
        end = len(cards)-1

        while start<=end:
            mid_index = (start + end)//2
            mid_no =cards[mid_index]

            print('start:', start, 'end:',end, 'mid:', mid_index, 'midNo:', mid_no)

            if mid_no==query:
                return mid_index
            elif mid_no<query:
                end = mid_index-1
            elif mid_no>query:
                start = mid_index+1

        return -1

                
                




    for test in tests:
        if locate_card(**test['input']) == test['output']:
            print ('Correct')
        else:
            print ('Wrong')

