# balance = float(input("Welcome User, Please enter your balance"))
balance = 500 #alternative

sel_1 = input(f"""

    Your balance is {balance}
    
    Press 1. to buy bundle
          2. for Mobile money services(Lumicash)
          #. to exit \n""")
if sel_1 == "#":
    print("Exiting...")
    exit

if sel_1 == "1":
    print("""
                 1. Social media bundles
                 2. Regular bundles
                 3. Midnight bundles
                 4. Promotion""")
    sel1 = int(input())
    if sel1 == 1:
            print("""
                 Facebook + Instagram + Twitter + Tiktok + Snapchat
                 1. 1 day package = 250 
                 2. 3 day package = 650
                 3. 1 week package = 1000""")
            sel1A = int(input())
            if sel1A == 1:
                print("""
                 1. For you
                 2. For others """)
                sel1A1 = int(input())
                if sel1A1 == 1:
                    
                    print("""
                 1. Cofirm
                 2. Cancel """)
                sel1A1A = int(input())
                if sel1A1A == 1:
                    print("""
                  You have successfully activated a social media package to be used until tomorrow at this time! Enjoy your time with your Lumitel""")
                    
#             elif sel1A == 2:
                #call function on 25 to 38
                #use function to print stuff
                # functions when it comes to back options
                #include conditions
                
#Include back options #add the option to refuse invalid inputs but give user chance to enter correct input.