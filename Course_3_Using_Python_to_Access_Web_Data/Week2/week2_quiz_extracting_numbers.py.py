import re
total = 0
hand = open('regex_sum_33185.txt') 
inp = hand.read()
cnt = re.findall('[0-9]+',inp)
print("List with numbers as string")
print("---------------------------")
print(cnt)
print("                            ")
print("---------------------------")
print("Converting string to int")
numlist = [int(i) for i in cnt]
print("---------------------------")
print("Final list")
print(numlist) 
print("---------------------------")

score=sum(numlist) 

print("Sum of all elements in given list: ", score)

