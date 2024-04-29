if __name__ == '__main__':
    # Problem
    # We need to write a program to find the fist and last position of a given number in a list of numbers arranged in ascending order. We also need to minimize the number of times we access the elements from the list.

    #Input
    #Cards: number list in ascending order
    #Query: number, whose position in array to be determined

    #Output
    #Start and end position

    #Tests
    tests =[]
    #1. Query in middle:
    tests.append({
        'input':{
            'cards':[2,2,2,4,4,6,6,6,6,8,8,9,9,9,9,9,10,10],
            'query':9
        },
        'output': [11,15]
    })
    #2. Query is first element:
    tests.append({
        'input':{
            'cards':[2,2,2,4,4,6,6,6,6,8,8,9,9,9,9,9,10,10],
            'query':2
        },
        'output': [0,2]
    })
    #3. Qeury is last element:
    tests.append({
        'input':{
            'cards':[2,2,2,4,4,6,6,6,6,8,8,9,9,9,9,9,10,10],
            'query':10
        },
        'output': [16,17]
    })
    #4. Cards has one element:
    tests.append({
        'input':{
            'cards':[1],
            'query':1
        },
        'output': [0,0]
    })
    #5. Cards do not have query:
    tests.append({
        'input':{
            'cards':[2,2,2,4,4,6,6,6,6,8,8,9,9,9,9,9,10,10],
            'query':5
        },
        'output': [-1,-1]
    })
    #6.Cards is empty:
    tests.append({
        'input':{
            'cards':[],
            'query':1
        },
        'output': [-1,-1]
    })

    # Solution
    # 1. Binary search
    # 2. Search first
    # 2. Search last

    def locate_card(cards, query):
        start = 0
        end = len(cards) - 1

        while start <= end:
            mid = (start + end) // 2
            number = cards[mid]

            if number == query:
                first = search_first(cards, start, mid, number)
                last = search_last(cards, mid, end, number)
                return [first, last]
            elif number < query:
                start = mid + 1
            else:
                end = mid - 1
        return [-1, -1]
    
    def search_first(cards, left, right, number):
        while left < right:
            mid = ((right-1) + left) // 2
            if cards[mid] < number:
                left = mid + 1
            else:
                right = mid
        return left if cards[left] == number else -1

    def search_last(cards, left, right, number):
        while left < right:
            mid = (right + (left + 1)) // 2
            if cards[mid] > number:
                right = mid - 1
            else:
                left = mid
        return right if cards[right] == number else -1


    for test in tests:
        if locate_card(**test['input']) == test['output']:
            print ('Correct')
        else:
            print ('Wrong')

