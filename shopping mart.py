#shopping mart
items=["pen", "notebook", "bottle", "shirt", "cap"]
cost=[10,60,250,200,160]
choice="y"
amount=0
while choice=="y":
  print("="*20)
  print("WELCOME TO OUR SHOPPING MART")
  print("Here is the list of items:\n", items)
  print("="*20, "\n")

  obj=input("What do you want to buy: ")
  idx = items.index(obj)   #index of object
  price = cost[idx]        #price of 1 object
  print("cost of ", obj,"is", price)

  qty=int(input("Quantity to buy: "))
  amount+=(qty*price)
  print("Your total amount:", amount)
  choice=input("do you want to continue (y/n): ")

print("YOUR TOTAL BILL IS", amount)
print("")
print("Thank you, visit again!")



