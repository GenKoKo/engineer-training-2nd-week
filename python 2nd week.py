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
