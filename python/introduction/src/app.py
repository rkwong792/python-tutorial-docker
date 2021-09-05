# Python is a scripting language.

class Customer:
    # constructor
    def __init__(self, c="", f="", l=""):
        self.customerID = c
        self.firstName = f
        self.lastName = l

    # self = the actual object itself that the class represents
    # represents the instance of the class
    def fullName(self):
        return self.firstName + " " + self.lastName

def getCustomers():
    customers = {
        "a": Customer("a","James","Baker"),
        "b": Customer("b","Jonathan","D"),
        "c": Customer("c","Aleem","Janmohamed"),
        "d": Customer("d","Ivo","Galic")
    }
    return customers

customers = getCustomers()

# Method 1 iteration
for customerID in customers:
    print(customers[customerID].fullName())

# Method 2 iteration
for _, customer in customers.items():
    print(customer.fullName())