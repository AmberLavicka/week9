# Binary search algorithm, recursive 

def find(sorted_items, item):
  if len(sorted_items) == 0:
    return False

  if len(sorted_items) == 1:
    return sorted_items[0] == item

  if len(sorted_items) > 1:
    if len(sorted_items) == 0:
      return False
    else:
      midpoint = len(sorted_items)//2
      if sorted_items[midpoint]==item:
        return True
      else:
        if item<sorted_items[midpoint]:
          return find(sorted_items[:midpoint], item)
        else:   
          return find(sorted_items[midpoint+1:], item)
                              

numbers = list(range(80))

assert True == find(numbers, 20)
assert True == find(numbers, 79)
assert False == find(numbers, 101)
