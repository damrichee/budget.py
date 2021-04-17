class Budget:
    def __init__(self, categories,):
        self.categories = categories
        self.balance = 1000

    def deposit(self, amount,):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def transfer(self, amount, categories):
        return "Transfer to " , categories
        

    def getBalance(self):
        return self.balance
        


foodCategories = Budget('food')
foodCategories.deposit(5000)
foodCategories.withdraw(5000)
foodCategories.transfer(200, Budget('clothing'))


print(foodCategories.getBalance())

clothingCategories = Budget('clothing')
clothingCategories.deposit(5000)
clothingCategories.withdraw(5000)

print(clothingCategories.getBalance())

entertainmentCategories = Budget('entertainment')
entertainmentCategories.deposit(5000)
entertainmentCategories.withdraw(1000)


print(entertainmentCategories.getBalance()) 
 
