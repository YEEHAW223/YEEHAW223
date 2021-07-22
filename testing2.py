#def my_mean(a):
 #   return sum(a)/ len(a)
#my_mean(i)
#print("mean: "+ str(my_mean))

#listOfNum = [200, 55, 46 , 200 , 50, 40, 7, 200, 13, 18, 314, 15, 4, 13, 9, 17, 6, 10, 16, 5, 5, 26, 3, 165, 8, 13, 15, 11, 7, 4, 14, 10, 16, 2, 9, 6, 6, 2, 10, 5, 6, 10, 5, 9]
#newList = sorted(listOfNum)
#print(newlist)
# List of numbers

listOfNum = [200, 55, 46 , 200 , 50, 40, 7, 200, 13, 18, 314, 15, 4, 13, 9, 17, 6, 10, 16, 5, 5, 26, 3, 165, 8, 13, 15, 11, 7, 4, 14, 10, 16, 2, 9, 6, 6, 2, 10, 5, 6, 10, 5, 9]
newList = sorted(listOfNum)

# print the List
print("Initial List", listOfNum, sep='\n')

print("Sorting the List in ascending Order")

# Create a sorted copy of existing list
newList = sorted(listOfNum)
# print the List
print("New List", newList, sep='\n')
# print the List
print("Existing List", listOfNum, sep='\n')

# Sort the List in Place
listOfNum.sort()
# print the List
print("List Sorted in Ascending Order", listOfNum, sep='\n')
print("Sorting the List in Descending Order")

# Create a sorted copy of existing list
newList = sorted(listOfNum, reverse=True)
# print the List
print("New List", newList, sep='\n')
# print the List
print("Existing List", listOfNum, sep='\n')

# Sort the List in Place (Descending Order)
listOfNum.sort(reverse=True)
# print the List
print("List Sorted in Descending Order", listOfNum, sep='\n')
if __name__ == "__main__":
    main()