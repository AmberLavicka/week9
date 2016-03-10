# Binary search algorithm

def find(sorted_items, item):
  if len(sorted_items) == 0:
    return False

  if len(sorted_items) == 1:
    return sorted_items[0] == item

#  if len(sorted_items) > 1:
#    for item in sorted_items:
#      position = round(len(sorted_items)/2)
#      if sorted_items[position] == item:
#        return True
#      position = position / 2

  # Uh oh... now what?
  #

  start = 0
  end = len(sorted_items) - 1

  while start <= end:
    midpoint = (start + end) // 2
# gives you the integer     
    if sorted_items[midpoint] == item:
      return True
# return statements gets you out of function
    if sorted_items[midpoint] > item:
      end = midpoint - 1
    else:
      start = midpoint + 1
  
  return False


numbers = list(range(80))

assert True == find(numbers, 20)
assert True == find(numbers, 79)
assert False == find(numbers, 101)
