def removeList():
  
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  for elem in l2:
    l1.remove(elem)
  return l1

l1 = removeList()
print(l1)