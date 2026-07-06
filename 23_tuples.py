#tuples

#if __name__ == '__main__':
 #   n = int(raw_input())
  #  integer_list = map(int, raw_input().split())
   # t = tuple(integer_list)
    #print hash(t)

#raw_input only works with Python 2

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))

#This should be correct but just to pass in hackerRank tutorial use the above code since hackerRank uses an older version of python