#1: Write a Python function called max_num()to find the maximum of three numbers.

def max_num(num1,num2,num3):
    numbers = [num1, num2, num3]
    return max(numbers)

# print(max_num(1,2,3))
# print(max_num(100,50,1))
# print(max_num(15,30,2))

#2: Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    if len(list) == 0:
        return 0

    else:
        product = 1
        for i in list:
            product = product*i
        return product

# print(mult_list([1,2,3]))
# print(mult_list([]))
# print(mult_list([15,2]))

#3: Write a Python function called rev_string() to reverse a string.

def rev_string(stringy):
    return stringy[::-1]

# print(rev_string(""))
# print(rev_string("apple"))
# print(rev_string("mt string"))


#4: Write a Python function called num_within() to check whether a number falls in a given range.
"""The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False."""

def num_within(num, start_of_range_num, end_of_range_number):
    if num < start_of_range_num or num > end_of_range_number:
        return False
    elif num >= start_of_range_num and num <= end_of_range_number:
        return True

# print(num_within(3,2,4))     
# print(num_within(3,1,3))     
# print(num_within(10,2,5))



#5: Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
"""The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together."""

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate numbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)