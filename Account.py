class Account(obgect):
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
  def deposit(self, value):
    self.balance += value

if __name__ == '__main__':
  acc = Account('a', 100)
  acc.deposit(10)
