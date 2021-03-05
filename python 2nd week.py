# Q1
print("---Q1---")

def calculate(min, max):
    total = 0
    while min <= max:
        total += min
        min += 1
    
    print (total)


calculate(1,3)
calculate(4,8)


# Q2
print("---Q2---")

def avg(data):

    total = 0
    employees_no = 0
    while employees_no < len(data["employees"]):

        total += data["employees"][employees_no]["salary"]
        employees_no += 1
    
    average = total / len(data["employees"])

    print(average)
    
    
avg({"count":3,
    "employees":[{"name":"John","salary":30000},
                {"name":"Bob","salary":60000},
                {"name":"Jenny","salary":50000}]
    })


# Q3
print("---Q3---")

def maxProduct(nums):
    
    dict = {}
    x = 0
    for i in nums:
        dict[x] = i
        x += 1
    

    biggest = 0
    for j,k in dict.items():
        
        y = len(dict) - j -1
        while y > 0:
            result = k*dict[j+1]

            if result > biggest:
                biggest = result

            j += 1
            y -= 1
    
    print(biggest)

maxProduct([5, 20, 2, 6])
maxProduct([10,-20,0,3])
# maxProduct([10,-20,0,3,1,3,5,10,20,15,13,-17])

# Q4
print("---Q4---")

def twoSum(nums, target):
    dict = {}
    x = 0
    for i in nums:
        dict[x] = i
        x += 1
    
    for j,k in dict.items():
        
        z = j + 1
        y = len(dict) - j - 1
        while y > 0:
            add = k + dict[z]
            if add == target:
                return [j, z]

            y -= 1
            z += 1
    

result = twoSum([2, 11, 7, 15], 9)
print(result)


# Q5
print("---Q5---")

def maxZeros(nums):

    temp_longest = 0
    longest = 0

    for i in nums:
        if i == 0:
            temp_longest += 1
            if temp_longest > longest:
                longest = temp_longest

        else:
            temp_longest = 0
    
    print(longest)



maxZeros([0, 1, 0, 0]);  
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); 
maxZeros([1, 1, 1, 1, 1]);  