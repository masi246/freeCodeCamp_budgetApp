class Category:
  '''When objects are created, they are passed in the name of the category. 
    The class should have an instance variable called ledger that is a list. '''

  def __init__(self, name):
    self.name = name
    self.ledger = list()

  def deposit(self, amount, description=""):
    '''accepts an amount and description. If no description is given, 
        it should default to an empty string. Will append an object to the ledger 
        list in the form of  {"amount": amount, "description": description}'''
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    '''A withdraw method that is similar to the deposit method, but the amount passed in should 
        be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to 
        the ledger. This method should return True if the withdrawal took place, and False otherwise.'''
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    '''returns the current balance of the budget category based on the deposits and withdrawals that have occurred.'''
    balance = sum([i["amount"] for i in self.ledger])
    return balance

  def transfer(self, amount, category):
    '''accepts an amount and another budget category as arguments. If there are not enough funds, nothing 
        should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.'''
    if (self.check_funds(amount)):
      self.withdraw(amount, f"Transfer to {category.name}")
      category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def check_funds(self, amount):
    '''accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise.'''
    if self.get_balance() >= amount:
      return True
    else:
      return False

  def __str__(self):
    '''returns the string version of transactions'''
    total = 0
    output = f"{self.name:*^30}\n"
    for item in self.ledger:
      output += f"{item['description'][0:23]:23}{item['amount']:>7.2f}\n"
      total += item['amount']
    output += f"Total: {str(total)}"
    return output
