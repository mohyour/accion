class BankAccount:
  #class variables - the same accross object at instantiation
  balance = 0
  #instance variable - different for different objects
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_customer_detail(self):
    return {"name": self.name, "age": self.age, "balance": self.balance}


  # Instance method
  def fund(self, amount):
    self.balance = amount + self.balance
    print('Account funded')

  def withdrawal(self, amount):
    if self.balance < amount:
      return ("Insufficient balance")
    self.balance = self.balance - amount
    return self.balance
#object - is an instance of a class

#instantiating an object - Initializing
ade = BankAccount('ade', '22')
bola = BankAccount('bola', '17')

ade.fund(5000)
print(ade.withdrawal(20000))
detail = ade.get_customer_detail()
print(detail['name'])
