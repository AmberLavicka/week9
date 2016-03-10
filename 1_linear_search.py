# Linear search algorithm

def find(items, item):
  # 1. start at the first item of the list
  # 2. is it the item we're looking for?
  # 3. If so, we're done!
  # 4. If not, go to the next item, and go to step 2.

  for i in items:
    if i == item:
      return True

  return False

numbers = list(range(80))

assert True == find(numbers, 20)
assert True == find(numbers, 70)
assert False == find(numbers, 101)

#linear search because stepping thru one item at a time
