"""
sort    - will sort the original list
sorted  - create a copy of the list and updates and returns the copied list
"""
l1 = [9, 7, 1, 5, 2, 10, 4, 3, 6, 8]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending Order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending Order :{res_desc}")

print("-" * 60)

l1 = [9, 'zebra', 'apple', 7, 'yellow', 'blue', 1, 'white', 'dog', 5, 'pink', 'maroon', 2, 'gold', 'red', 10, 'cat', 'orange',  4, 'violet', 'hen', 3, 6, 8, 189, 1324, 29, 267,2014]
print(f"l1 :{l1}")

res = sorted(l1, key=ascii)

print(f"res :{res}")
# sort the data

"""
cities = ['hyderabad', 'thiruvananthapuram', 'mysore', 'ooty', 'mumbai', 'bangalore', 'pune', 'delhi', 'kolkata', 'vishakapatnam', 'chennai']

sort the cities based on their length
"""

