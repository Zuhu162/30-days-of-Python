items = [("Product1", 10), ("Product2", 20), ("Product3", 5)]

x = 1
items.sort(key=lambda item: item[1])
print(items)
