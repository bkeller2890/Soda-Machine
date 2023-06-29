print("Hello, and welcome to the soda machine!!!") 

#initial input to prompt the user to put change in
change = float(input("Please Insert change: "))

if change >= 1.75:
    
    #list of products available at this machine
    print("\nProducts available: \n")
    print("Select 1 for Coke")
    print("Select 2 for Sprite")
    print("Select 3 for Minute Maid Lemonade")
    print("Select 4 for Gatorade")
    print("Select 5 for Dr. Pepper")
    print("\n")
    

    #displays products available using a set notation 

    product = {1: "Coke", 2: "Sprite", 3: "Minute Maid Lemonade", 4: "Gatorade", 5: "Dr. Pepper"}
    
    #Second input that prompts the user to select a product from the machine
    selection = int(input("Selection: "))

    
    if selection >=1 and selection <= 5: 
        print("\nYou have selected: " + product[selection])
    else: 
        print("Invalid Selection")
    
    if change > 1.75:
           changeback = change - 1.75
           

           def change_amount(x):
                dollars = x// 1.00
                x %= 1.00
                
                quarters = x // 0.25
                x %= 0.25
                
                dimes = x // 0.10
                x %= 0.10
                
                nickels = x // 0.05
                x %= 0.05
                
                pennies = x
                
                return dollars, quarters, dimes, nickels, pennies
                
                
           
        
           dollars, quarters, dimes, nickels, pennies = change_amount(changeback)
           #to output currency in the proper format, be sure to round the float
           #up to two decimal places
           print()
           print(f"You got back {dollars} in dollars ")
           print(f"You got back {quarters} in quarters")
           print(f"You got back {dimes} in dimes")
           print(f"You got back {nickels} in nickels")
           print(f"You got back {pennies} in pennies")
           print()

          
    
    print("\nThank you, have a nice day!")

else: 
    print("Products cost $1.75 - please add more change")
