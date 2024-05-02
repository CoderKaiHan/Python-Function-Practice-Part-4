#function 2 - max_num

def max_num(a,b,c):
    i= a
    if i>=b:
        i = a
    else:
        i = b
        if i>=c:
            i = b
        else:
            i = c
    print("The largest number among", a, ",", b, "and", c, "is", i)

max_num(10,20,30)    

def max_num2(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    print("The largest number among", a, ",", b, "and", c, "is", max_value)

max_num2(10, 5, 8)


#function 2 - mult_list

def mult_list(list):
    product = 1
    for num in list:
        product = product * num
    print("The product of all numbers in", list, "is", product)

mult_list([10, 2, 5])


#function 3 - rev_string

def rev_string(string, i=0):
    if i == len(string) - 1:
        return string[i]
    else:
        return rev_string(string, i + 1) + string[i]

print(rev_string("hello"))


#function 4 - num_within

def num_within(x, start, end):
    if x >= start and x <= end:
        return True
    else:
        return False
    
print("The result of num_within(3,2,4) is", num_within(3,2,4))



#function 5 - pascal
#Can't figure out this one. Copied from the solution guide .....

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
        #intermediate nunmbers get added from previous rows
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

pascal(5)