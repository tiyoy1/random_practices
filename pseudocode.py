
# ##Pseudocode translation level 1 -> asking user for input then compares the input to a number
# item_price = int(input("Input your item price : "))

# if item_price > 100 :
#     final_price = item_price * 0.8
# else :
#     final_price = item_price * 0.95

# print(final_price)

# ##Pseudocode translation level 2 -> using while loop and break
# while True :
#     user_password = str(input("Insert your password : "))

#     if len(user_password) < 8 :
#         print("Please insert longer password")

#     else :
#         print("Password accepted!")
#         break

# #Pseudocode translation level 3 -> using lists, checking lists, and flagging boolean
# party_list = ["Alice", "Bob", "Charlie"]
# is_invited = False

# your_name = input("Insert your name : ")

# if your_name in party_list :
#     is_invited = True

# if is_invited == True :
#     print("welcome to the party")
# else :
#     print("Sorry, you are not invited")

# #level 3 Pseudocode
# # START 
# #     SET party_list = ["Alive", "Reno", "Keket"] 
# #     SET is_invited = False

# #     READ your_name 

# #     IF your_name IN party_list :
# #         SET is_invited = True

# #     IF is_invited == True :
# #         print("Nice one")
# #     ELSE  print ("lol no invited")

# # END

# # START
# # 	SET user_balance = $500
# # 	SET total_user_withdrawal = 0
# # 	SET atm_cash_reserve = $300
# # 	SET daily_limit = $200
# # 	SET session_active = TRUE

# # 	WHILE session_active == TRUE
# # 		IF total_user_withdrawal >= daily_limit THEN
# # 			PRINT "Daily withdrawal limit reached. Ending Session"
# # 			BREAK
		
# # 		PRINT "Current Balance : $" + user_balance
# # 		PRINT "Enter withdrawal amount (Multiple of 10):"
# # 		READ request_amount
		
# # 		IF request_amount MOD 10 != 0 THEN
# # 			PRINT "Error : amount must be in multiple of 10"
# # 		ELSE IF request_amount > user_balance THEN 
# # 			PRINT "Error : Insufficient funds in your account."
# # 		ELSE IF request_amount > atm_cash_reserve THEN
# # 			PRINT "ATM doesn't have enough reserve."
# # 		ELSE IF (total_user_withdrawal + request_amount) > daily_limit THEN
# # 			PRINT "Error: Transaction exceeds your remaining daily limit of $" + (daily_limit - total_user_withdrawal)
# # 		ELSE 
# # 			SET user_balance = user_balance - request_amount
# # 			SET atm_cash_reserve = atm_cash_reserve - request_amount
# # 			SET total_user_withdrawal = total_user_withdrawal + request_amount
			
# # 			PRINT "Dispensing $" + request_amount + "..."
# # 			PRINT "Remaining balance : $" + user_balance
# # 		PRINT "Would you like to do another transaction?"
# # 		READ user_choice
# # 		IF user_choice != "YES" THEN
# # 			SET session_active = FALSE
# # 			PRINT "Thank you for using the ATM. Goodbye!"
# # 		END IF
# # 	END WHILE
# # END

# user_balance = 500
# total_user_withdrawal = 0
# atm_cash_reserve = 300
# daily_limit = 200
# session_active = True

# while session_active == True :
#     if total_user_withdrawal >= daily_limit :
#         print("Daily withdrawal limit reached. Ending session")
#         break

#     print("Current balance : $" + str(user_balance))
#     request_amount = int(input("Enter withdrawal amount (Multiple of 10) : "))

#     if request_amount % 10 != 0 :
#         print("Error : amount must be in multiple of 10")
#     elif request_amount > user_balance :
#         print("Error : insufficient funds in your account")
#     elif request_amount > atm_cash_reserve :
#         print("ATM doesnt have enough reserve")
#     elif (total_user_withdrawal + request_amount) > daily_limit :
#         print("Error : Transaction exceeds your daily limit of $" + str((daily_limit - total_user_withdrawal)))
#     else :
#         user_balance = user_balance - request_amount
#         atm_cash_reserve = atm_cash_reserve - request_amount
#         total_user_withdrawal = total_user_withdrawal + request_amount

#         print("Dispensing $" + str(request_amount) + "...")
#         print("Remaining balance : $" + str(user_balance))

#     user_choice = input("Would you like another transaction? ")

#     if user_choice != "yes" :
#         session_active = False
#         print("Thank you for using this machine!")

# battery_level = 0

# while battery_level < 100 :
#     battery_level = battery_level + 10
#     print("Current battery : " + str(battery_level))

# print("Fully Charged!")

# grocery_list = ["Apple", "Milk", "Banana", "Eggs"]

# for item in grocery_list :
#     if item == "Milk":
#         print("Found the milk!")
#         break
#     else: 
#         print("Checking next item...")

# guest_list = ["guest", "VIP", "guest", "VIP", "VIP"]

# for guest in guest_list : 
    
#     guest_counter = guest.count("VIP")

#     if guest_counter == 3 :
#         print("There are 3 VIPs!")

number1 = int(input("put your first number here : "))
number2 = int(input("your 2nd number here : "))



print(number1+number2)