
# simple how to ceate dictonry

student = {}
print(student)


# Dictonry with data  =  Key ": valuve"
student = {
    "name": "Rahul",
    "age": 25,
    "city": "Delhi"
}

print(student)

# vlue acces 
print(student["name"])
print(student["age"])


# add  new value 

student["email"] = "rahul@gmail.com"

print(student)

# with loops 

for key, value in student.items():
    print(key, value)

# employe add of dic

employee = {
    "id": 101,
    "name": "Rahul Singh",
    "email": "rahul@gmail.com",
    "phone": "9876543210",
    "salary": 50000
}

print(employee["name"])
print(employee["salary"])

# nasted dict  inside dic 
employee = {
    "id": 101,
    "name": "Rahul",
    "address": {
        "city": "Delhi",
        "state": "Delhi",
        "country": "India"
    }
}

print(employee["address"]["city"])