class Card:
    balance = 0
    #  constructor defines things that should run every time you call the classi

    def __init__(self,bal):
        self.balance=bal

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount + (0.2*amount)
            return self.printReceipt(self.balance,amount)
        else:
            return "Insufficient Balance "

    def printReceipt(self,balance,withdrawal):
        return """AMOUNT :......()
                  BALANCE :.....()
        """.format(withdrawal,balance)