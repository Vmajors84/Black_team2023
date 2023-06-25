import uuid

instances = int(input("How many EC2 instances do you need names for? "))
department = input("What is the name of your department? ")

for n in range(instances):
    print("{}{}".format(department, uuid.uuid4()))
