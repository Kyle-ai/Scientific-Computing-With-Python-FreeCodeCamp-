#1.A deposit method that accepts an amount and description. If no description is
#given, it should default to an empty string. The method should append an object
#to the ledger list in the form of {"amount": amount, "description": description}.

#2.A withdraw method that is similar to the deposit method, but the amount passed
#in should be stored in the ledger as a negative number. If there are not enough
#funds, nothing should be added to the ledger. This method should return True if
#the withdrawal took place, and False otherwise.

#3.A get_balance method that returns the current balance of the budget category
#based on the deposits and withdrawals that have occurred.

#4.A transfer method that accepts an amount and another budget category as
#arguments. The method should add a withdrawal with the amount and the description
#"Transfer to [Destination Budget Category]". The method should then add a deposit
#to the other budget category with the amount and the description "Transfer from
#[Source Budget Category]". If there are not enough funds, nothing should be
#added to either ledgers. This method should return True if the transfer took
#place, and False otherwise.

#5.A check_funds method that accepts an amount as an argument. It returns False
#if the amount is greater than the balance of the budget category and returns True
#otherwise. This method should be used by both the withdraw method and transfer
#method.

#6.When the budget object is printed it should display:
#A title line of 30 characters where the name of the category is centered in a
#line of * characters. A list of the items in the ledger. Each line should show
#the description and amount. The first 23 characters of the description should be
#displayed, then the amount. The amount should be right aligned, contain two
#decimal places, and display a maximum of 7 characters. A line displaying the
#category total.

class Category:
    def __init__ (self, category):
        self.ledger = []
        self.amount = 0
        self.category = category

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.amount -= amount
            self.ledger.append({"amount": -amount,"description":"Transfer to "+category.category})
            category.ledger.append({"amount": amount,"description": "Transfer from "+self.category})
            #print(self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.amount < amount:
            return False
        else:
            return True

    def withdraw(self,amount,description=''):
        if self.check_funds(amount) ==True:
            self.amount -=amount
            self.ledger.append({"amount":-amount,"description":description})
            return True
        else:
            return False


    def deposit(self, amount, description=''):
        self.amount += amount
        self.ledger.append({"amount":amount,"description":description})

    def get_balance(self):
        return self.amount

    def __str__(self):
        result=""
        result+="*************Food*************"+"\n"
        for transaction in self.ledger:
          amount=0
          description=""
          for key,value in transaction.items():
              if key=="amount":
                amount = value
              elif key=="description":
                description=value
          if len(description)>23:
            description=description[:23]
          amount = str(format(float(amount),'.2f'))
          if len(amount)>7:
            amount= amount[:7]
          result+= description + str(amount).rjust(30-len(description))+"\n"
        result+="Total: "+str(format(float(self.amount),'.2f'))
        return result

def create_spend_chart(categories):
    output = "Percentage spent by category"
    x = len(categories)
    y = 100

  #calculate total & percentages for each category
    cat_percentage = list()
    total_spent = 0
    for item in categories:
        total_spent += item.withdrawls()
    for item in categories:
        percentage = item.withdrawls() / total_spent
        cat_percentage.append( int( (percentage // .1) * 10 ) )

    while y >= 0:
        output += "\n"
    #input the correct right aligned Y axis value
        output += str(y) + "| " if y == 100 else " " + str(y) + "| " if y < 100 and y > 0 else "  0| "
#loop through each category column and check if a bar value exists
        col = 0
        while col < x:
            if cat_percentage[col] >= y:
        # print(percentages[col], y)
                output += "o  "
            else:
                output += " "*3
            col += 1
        y -= 10
    output += "\n" + " "*4 + "-" + "-"*x*3
  #label x access using double loop for names
    max_name_length = 0
    for cat in categories:
        if len(cat.name) > max_name_length:
            max_name_length = len(cat.name)
    z = 0
    while z < max_name_length:
        output += "\n" + " "*5
        for cat in categories:
            try: output += cat.name[z] + " "*2
            except: output += " "*3
        z += 1
    return output

food =Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing =Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto =Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
