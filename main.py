#Start program and welcome user
name = input("What is your name?\n")
print("Hello " + name + ", welcome to Kilandra's Sporting Goods store!")

#Create Good/Service class
class SportingGoods:
  def __init__(self, name, price, quantity, category): #iniitialize the attributes
    if isinstance(price, str):
      self.price = float(price.strip("$"))
    elif isinstance(price, float):
      self.price = price
    else:
      raise ValueError("Price must be a string or float")
      
    self.name = name
    self.quantity = quantity 
    self.category = category

  #Add specified quantity to inventory
  def addItem(self, quantity):
    self.quantity += quantity

  #Remove specified quantity from inventory
  def removeItem(self, quantity):
    if self.quantity >= quantity:
      self.quantity -= quantity
      print("Removed", quantity, self.name + "(s) from inventory.")
    else:
      print("Sorry, we don't have enough", self.name + "(s) in stock.")

#Create user class
class User:
  def __init__(self, name):
    self.name = name
    self.cart = []

  #Add item to cart
  def addItemToCart(self, itemName, quantity, GoodsDatabase):
      if quantity <= 0:
          print("Please enter a valid quantity.")
          return

      itemFound = False
      for item in GoodsDatabase:
        if item.name == itemName:
            itemFound = True
            if item.quantity >= quantity:
              item.quantity -= quantity #Decrease quantity in stock
              self.cart.append((item.name, quantity))
              print(quantity, item.name + "(s) added to cart.")
              return
            else:
                print("Sorry, we don't have enough", item.name + "(s) in stock.")
                return #if quantity is not sufficient

      if not itemFound:
          print("Sorry, we don't have", itemName + " in stock.")  
  #Remove items from cart
  def removeItemFromCart(self, GoodsDatabase):
    itemName = input("Enter the name of the item you want to remove from your cart: ")
    quantity = int(input("Enter the quantity you want to remove: "))

    for item in user.cart:
      if item[0] == itemName:
        #Find item in GoodsDatabase and increment quantity
        for goodsItem in GoodsDatabase:
            if goodsItem.name == itemName:
              goodsItem.quantity += quantity #increment quantity
              break

        #Update the cart with new quantity
        newQuantity  = item[1] - quantity
        if newQuantity > 0:
          self.cart.remove(item)
          self.cart.append((itemName, newQuantity))
        else:
          self.cart.remove(item)

        print(quantity, itemName + "(s) removed from cart.")
        return
    else:
      print("Item not found in cart.")

  #View what is in users cart currently
  def viewCart(self):
    if self.cart:
        print("Your Shopping Cart:")
        for item, quantity in self.cart:
            print("- ", quantity, item + "(s)")
    else:
        print("Your cart is empty.")  

  #View available items
  def viewAvailableItems(self, GoodsDatabase):
    print("\nAvailable items:")
    for item in GoodsDatabase:
      print(item.name, "-", "${:.2f}".format(item.price), "-", item.quantity, "in stock")

  #Update quantity in database
  def updateQuantityInDatabase(self, GoodsDatabase):
    for itemName, totalQuantity in self.cart:
      for items in GoodsDatabase:
        if items.name == itemName:
          items.quantity += totalQuantity #Add back removed item
          break 

  # Lookup information about an item
  def lookupItem(self, GoodsDatabase):
    itemName = input("Enter the name of the item you want to lookup: ")
    for item in GoodsDatabase:
      if item.name == itemName:
        print("Item:", item.name)
        print("Price:", item.price)
        print("Quantity in stock:", item.quantity)
        print("Category:", item.category)
        return
    print("Item not found in database.")

  #Calculate total price of items in cart and display checkout summary
  def checkout(self, GoodsDatabase):
      total_price = self.calculateTotalPrice(GoodsDatabase)
      print("Your Shopping Cart:")
      for item, quantity in self.cart:
          print("- ", quantity, item + "(s)")
      print("Total price:", "${:.2f}".format(total_price))

  #Calculate total price of items and display summary
  def calculateTotalPrice(self, GoodsDatabase):
      total_price = 0
      for item, quantity in self.cart:
          for goodsItem in GoodsDatabase:
              if goodsItem.name == item:
                  total_price += goodsItem.price * quantity
                  break
      return total_price
      
#Create sporting goods objects
basketball = SportingGoods("Basketball", 15.00, 10, "Ball")
football = SportingGoods("Football", 10.00, 10, "Ball")
baseball = SportingGoods("Baseball", 7.00, 10, "Ball")
cleats = SportingGoods("Cleats", 75.00, 5, "Footwear")
tennisball = SportingGoods("Tennisball", 2.00, 10, "Ball")

#Create sporting goods database
GoodsDatabase = [basketball, football, baseball, cleats, tennisball]

#Create user object
user = User(name)

#Create menu
def menu(user, GoodsDatabase): #Main menu loop to interact with user
  while True: #Display menu options and get user choice then execute
    print("\nPlease select an option:")
    print("1. View available items")
    print("2. Add item to cart")
    print("3. Remove item from cart")
    print("4. View cart")
    print("5. Lookup information about an item")
    print("6. Checkout")
    print("7. Add a new item to the database")
    print("8. Remove an item from the database")
    print("9. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
      user.viewAvailableItems(GoodsDatabase) #Calls view available items function
    elif choice == "2":
      itemName = input("Enter the name of the item you want to add to your cart: ")
      quantity = int(input("Enter the quantity you want to add: "))
      user.addItemToCart(itemName, quantity, GoodsDatabase) #addItemToCart
    elif choice == "3":
      user.removeItemFromCart(GoodsDatabase) #Call removetocart function
    elif choice == "4":
      user.viewCart() #Call viewcart function
    elif choice == "5":
      user.lookupItem(GoodsDatabase) #Call lookupItem function
    elif choice == "6":
      user.checkout(GoodsDatabase) #Call checkout function
    elif choice == "7":
      addNewItem(GoodsDatabase) #Call addNewItem function
    elif choice == "8":
      removeItem(GoodsDatabase) #Call removeItem function
    elif choice == "9":
      print("Thank you for shopping with us!")
      return  # Exit the function and program
    else:
      print("Invalid choice. Please try again.")

#Function to add an item to the database
def addNewItem(GoodsDatabase):
   #Prompt user for item details and add to the database 
  name = input("Enter the name of the new item: ")
  priceInput = input("Enter the price of the new item (e.g., 15.00): ")
  quantityInput = int(input("Enter the quantity in stock: "))
  category = input("Enter the category of the new item: ")

  try:
    price = float(priceInput.strip("$"))
    
    if price <= 0:
      print("Please enter a valid price.")
      return

    quantity = int(quantityInput)
    
    if quantity <= 0:
      print("Please enter a valid quantity.")
      return

    newItem = SportingGoods(name, price, quantity, category)
    GoodsDatabase.append(newItem)
    print(f"{name} added to the database.")
    user.viewAvailableItems(GoodsDatabase)  #Display updated list of items

  except ValueError:
    print("Invalid input. Price and quantity must be valid numbers.")
    

#Function to remove an item from the database
def removeItem(GoodsDatabase): 
   #Prompt user for item name and remove from the database if found
  name = input("Enter the name of the item you want to remove: ")
  for item in GoodsDatabase:
      if item.name == name:
          GoodsDatabase.remove(item)
          print(f"{name} removed from the database.")
          user.viewAvailableItems(GoodsDatabase)  #Display updated list of items
          return
  print("Item not found in the database.")

#Main Menu loop
if __name__ == "__main__":
  menu(user, GoodsDatabase)

