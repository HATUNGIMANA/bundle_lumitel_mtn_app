# balance = float(input("Welcome User, Please enter your balance"))
balance = 500 #alternative       
            
def main_menu():
    print(f"""

Your balance is {balance}
    
Press
1. to buy data bundles
2. for Mobile money services(Lumicash)
#. to exit \n""")
    

def bundle_options():
    print("""
1. Social media bundles
2. Regular bundles
3. Midnight bundles
4. Promotion""")
def bundle_1():
    print("""
Facebook + Instagram + Twitter + Tiktok + Snapchat
1. 1 day package = 250 
2. 3 day package = 650
3. 1 week package = 1000
0. Back""")
        
def forWho():
    print("""
1. For you
2. For others """)
def confirm(n, r):
    notif = f"""
1. Buy a {n} for {r} 
2. Cancel """
    print(notif)
    return notif
def successful(a, b):
    #a = "a 24 hour" #YOU CAN'T USE THIS, THE CODE WON'T BE FLEXIBLE FOR A AND B ARE FIXED OOH!!
    #b = "yourself"
    notification = f"You have successfully activated {a} social media package for {b}! Enjoy your time with your Lumitel"
    print(notification)
    return notification

main_menu()

sel_1= input()                  

if sel_1 == "#":
    print("Exiting...")
    
elif sel_1 == "1":
     bundle_options()
     sel1A = input()
     if sel1A == "1":
         bundle_1()
         sel1A1 = input()
         if sel1A1 == "1":
             print("For who are aou are going to buy the 24 hour package?")
             forWho()
             sel1A1A = input()
             if sel1A1A == "1":
                 confirm("24 hour package of 250","yourself")
                 sel00 = input()
                 if sel00 == "1":
                     successful("24 hour", "yourself")
                 elif sel00 == "2":
                     print("canceled")
             elif sel1A1A == "2":
                 recipient = int(input("Enter the recepient's number"))
                 confirm("24 hour package of 250", recipient)
                 sel00A = input()
                 if sel00A == "1":
                     successful("24 hour", recipient)
                     
         elif sel1A1 == "2":
             print("For who are aou are going to buy the 3 day package?")
             forWho()
             sel1A1B = input()
             if sel1A1B == "1":
                 confirm("3 day package of 650", "yourself")
                 sel01 = input()
                 if sel01 == "1":
                     successful("3 day", "yourself")
             elif sel1A1B == "2":
                recipient1 = input("Enter the number of the recepient:")
                confirm("3 day package of 650", recipient1)
                sel02 = input()
                if sel02 == "1":
                     successful("3 day", recipient1)
                     
         elif sel1A1 == "3":
             print("For who are you going to buy the 1 week package")
             forWho()
             sel1A1C = input()
             if sel1A1C == "1":
                 confirm("1 week package of 1000", "yourself")
                 sel03 = input()
                 if sel03 == "1":
                     successful("1 week", "yourself")
             elif sel1A1C == "2":
                 recipient11 = input("Enter the number of the recipient:")
                 confirm("1 week package of 1000", recipient11)
                 sel04 = input()
                 if sel04 == "1":
                     successful("1 week", recipient11)
                     
         elif sel1A1 == "0":
             bundle_options()
else:
    print("Wrong input, Try again")
    main_menu()
        #MAKE SUCCESSFUL MESSAGE A BIT MORE FLEXIBLE WHEN IT COMES TO WHO IS THE PACKAGE BOUGHT FOR
        #USE THE ARGUMENTS a AND b CORRECTLY (Done)
        #Next version: Make back options
        #EACH MENU SHOULD INCLUDE AN OPTION TO ENTER ITS OVERALL INPUT!
        
