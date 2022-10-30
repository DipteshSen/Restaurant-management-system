# A program for Micro Project on Restaurant Management System
import os

#Main Menu
def mm() :
    ch = 0
    print("\t\tMAIN MENU\n")
    print("Press 1 for Starters")
    print("Press 2 for Main Course")
    print("Press 3 for Desserts")
    print("Press 0 to Exit")
    print()
    print("Enter Your Choice:")
    ch = int(input())
    return ch

#Starters Menu
def starters() :
    samt = 0
    ch = 0
    while (1):
        print("\nWelcome to the Starters Menu\n")
        print("Enter \'1\' for Veg Starters\nEnter \'2\' for Non-Veg Starters\nEnter \'0\' for Main Menu:")
        ch = int(input())
        if(ch == 0) :
            return samt
        elif (ch == 1) :
            samt += vs()
        elif(ch == 2) :
            samt += nvs()
        else :
            err()
    return samt

#Veg Starters
def vs() :    
    vstr = 0
    tvstr = 0
    amt = 0
    tamt = 0
    choice = 1
    print("\nVegetarian Starters:\n")
    print("\nVeg Starters \t\t\t Price in Rs.\n")
    print("1.  Paneer Tikka \t\t\t 110")
    print("2.  Veg Seekh Kebab \t\t\t 110")
    print("3.  Hara Bhara Kebab \t\t\t 110")
    print("4.  Shanghai Spring Roll \t\t 150")
    print("5.  American Corn Ball \t\t\t 150")
    print("6.  Cripsy American Corn \t\t 140")
    print("7.  Cripsy Baby Corn \t\t\t 140")
    print("8.  Cripsy Mushroom \t\t\t 120")
    print("9.  Cripsy Chilly Potato \t\t 120")
    print("10. Cripsy Chilly Chana \t\t 150")
    print("\nPress 0 to go back\n")
    while (choice == 1) :
        vstr = inp(1)
        if (vstr == 0):
            return tamt
        tvstr = plt()
        if (vstr == 1 or vstr == 2 or vstr==3) :
            amt = tvstr * 110
        if (vstr == 4 or vstr == 5) :
            amt = tvstr * 150
        if (vstr == 6 or vstr == 7) :
            amt = tvstr * 140
        if (vstr == 8 or vstr == 9) :
            amt = tvstr * 120
        if (vstr == 10) :
            amt = tvstr * 150
        tamt += amt
        choice = int(input("Do you want to place more order? Enter \'1\' for YES and \'2\' for NO:\n"))       
        if (choice == 2) :
            return tamt
        if (choice != 1 and choice != 2) :
            err()
    return tamt

#Non-Veg Starters
def nvs() :    
    nvstr = 0
    tnvstr = 0
    amt = 0
    tamt = 0
    choice = 1
    print("\nNon-Vegetarian Starters:\n")
    print("Non-Veg Starters \t\t Price in Rs.\n")
    print("1.  Chicken Tikka \t\t\t 170")
    print("2.  Murg Reshmi Kebab \t\t\t 170")
    print("3.  Murg Chilli Kebab \t\t\t 160")
    print("4.  Chicken Seekh Kebab \t\t 180")
    print("5.  Tangdi Kebab \t\t\t 180")
    print("6.  Murg Tandoori \t\t\t 190")
    print("7.  Fish Ajwani Tikka \t\t\t 190")
    print("8.  Chilli Chicken \t\t\t 160")
    print("9.  Drums of Heaven \t\t\t 180")
    print("10. Shanghai Chicken \t\t\t 180")
    print("\nPress 0 to go back\n")
    while (choice == 1) :
        nvstr = inp(2)
        if (nvstr == 0):
            return tamt
        tnvstr = plt()
        if (nvstr == 1 or nvstr == 2) :
            amt = tnvstr * 170
        if (nvstr == 3) :
            amt = tnvstr * 160
        if (nvstr == 4 or nvstr == 5) :
            amt = tnvstr * 180
        if (nvstr == 6 or nvstr == 7) :
            amt = tnvstr * 190
        if (nvstr == 8) :
            amt = tnvstr * 160
        if (nvstr == 9 or nvstr == 10) :
            amt = tnvstr * 180
        tamt += amt
        choice = int(input("Do you want to place more order? Enter \'1\' for YES and \'2\' for NO:\n"))        
        if (choice == 2) :
            return tamt
        if (choice != 1 and choice != 2) :
            err()   
    return tamt

#Main Course Menu
def mcourse() :    
    mcamt = 0
    ch = 0
    while (1):
        print("Welcome to the Main Course Menu")
        print("\nMain Course includes Indian and Chinese Dishes\n")
        print("Enter \'1\' for Indian Veg Dishes\nEnter \'2\' for Indian Non-Veg Dishes")
        print("Enter \'3\' for Chinese Dishes\nEnter \'0\' For Main Menu:\n")
        ch = int(input())
        if(ch == 0) :
            return mcamt
        elif (ch == 1) :
            mcamt += vd()
        elif(ch == 2) :
            mcamt += nvd()
        elif(ch == 3) :
            mcamt += cd()
        else :
            err()
    return mcamt

#Indian Veg Dishes
def vd() :    
    vfd = 0
    tvfd = 0
    amt = 0
    tamt = 0
    choice = 1
    print("\nIndian Vegetarian Dishes:\n")
    print("Indian Veg Dishes\t\t\t Price in Rs.\n")
    print("1.  Shahi Paneer\t\t\t\t 180")
    print("2.  Navratan Korma\t\t\t\t 180")
    print("3.  Kadahi Paneer\t\t\t\t 150")
    print("4.  Malai Kofta\t\t\t\t\t 140")
    print("5.  Kadahi Vegetable\t\t\t\t 140")
    print("6.  Vegetable Avial\t\t\t\t 140")
    print("7.  Shabnam Curry\t\t\t\t 150")
    print("8.  Makai Palak\t\t\t\t\t 150")
    print("9.  Veg. Pulao\t\t\t\t\t 110")
    print("10. Kashmiri Pulao\t\t\t\t 140")
    print("11. Butter Naan\t\t\t\t\t  40")
    print("12. Stuffed Kulcha \t\t\t\t  60")
    print("\nPress 0 to go back\n")
    while (choice == 1) :
        vfd = inp(3)
        if (vfd == 0):
            return tamt
        tvfd = plt()
        if (vfd == 1 or vfd == 2) :
            amt = tvfd * 180
        if (vfd == 3) :
            amt = tvfd * 150
        if (vfd == 4 or vfd == 5 or vfd == 6) :
            amt = tvfd * 140
        if (vfd == 7 or vfd == 8) :
            amt = tvfd * 150
        if (vfd == 9) :
            amt = tvfd * 110
        if (vfd == 10) :
            amt = tvfd * 140
        if (vfd == 11) :
            amt = tvfd * 40
        if (vfd == 12) :
            amt = tvfd * 60
        tamt += amt
        choice = int(input("Do you want to place more order? Enter \'1\' for YES and \'2\' for NO:\n"))       
        if (choice == 2) :
            return tamt
        if (choice != 1 and choice != 2) :
            err()
    return tamt


#Indian Non-Veg Dishes
def nvd() :    
    vfd = 0
    tvfd = 0
    amt = 0
    tamt = 0
    choice = 1
    print("\nIndian Non-Vegetarian Dishes:\n")
    print("Indian Non-Veg Dishes\t\t\t\t Price in Rs.\n")
    print("1.  Chicken Tikka Masala\t\t\t\t150")
    print("2.  Chicken Lababdar\t\t\t\t\t150")
    print("3.  Railway Lamb Curry\t\t\t\t\t180")
    print("4.  Kadahi Chicken\t\t\t\t\t160")
    print("5.  Mughlai Chicken\t\t\t\t\t160")
    print("6.  Murg Navratan Korma\t\t\t\t\t160")
    print("7.  Mutton Do Pyaza\t\t\t\t\t180")
    print("8.  Murg Masallam\t\t\t\t\t170")
    print("9.  Mutton Rogan Josh\t\t\t\t\t190")
    print("10. Prawn Malai Curry\t\t\t\t\t190")
    print("11. Fish Sarsowala\t\t\t\t\t140")
    print("12. Fish Dhaniawala \t\t\t\t\t160")
    print("\nPress 0 to go back\n")
    while (choice == 1) :
        vfd = inp(4)
        if (vfd == 0):
            return tamt
        tvfd = plt()
        if (vfd == 1 or vfd == 2) :
            amt = tvfd * 150
        if (vfd == 3) :
            amt = tvfd * 180
        if (vfd == 4 or vfd == 5 or vfd == 6) :
            amt = tvfd * 160
        if (vfd == 7) :
            amt = tvfd * 180
        if (vfd == 8) :
            amt = tvfd * 170
        if (vfd == 9 or vfd == 10) :
            amt = tvfd * 190
        if (vfd == 11) :
            amt = tvfd * 140
        if (vfd == 12) :
            amt = tvfd * 160
        tamt += amt
        choice = int(input("Do you want to place more order? Enter \'1\' for YES and \'2\' for NO:\n"))       
        if (choice == 2) :
            return tamt
        if (choice != 1 and choice != 2) :
            err()
    return tamt   

#Chinese Dishes
def cd() :    
    fd = 0
    tfd = 0
    amt = 0
    tamt = 0
    choice = 1
    print("\nChinese Dishes:\n")
    print("Chinese Dishes\t\t\t\t Price in Rs.\n")
    print("1.  Schezwan Fried Rice\t\t\t\t240")
    print("2.  Schezwan Chicken\t\t\t\t280")
    print("3.  Chilly Chicken\t\t\t\t280")
    print("4.  Chicken Noodle\t\t\t\t210")
    print("5.  Veg. Hakka Noodle\t\t\t\t210")
    print("6.  Chicken Manchurian\t\t\t\t190")
    print("7.  Paneer Manchurian\t\t\t\t190")
    print("8.  Chilly Paneer\t\t\t\t190")
    print("9.  Shanghai Fried Rice\t\t\t\t240")
    print("10. Veg. Fried rice\t\t\t\t210")
    print("11. Chicken Fried Rice\t\t\t\t210")
    print("12. Kimchi Rice Veg.\t\t\t\t210")
    print("\nPress 0 to go back\n")
    while (choice == 1) :
        fd = inp(5)
        if (fd == 0):
            return tamt
        tfd = plt()
        if (fd == 1) :
            amt = tfd * 240
        if (fd == 2 or fd == 3) :
            amt = tfd * 280
        if (fd == 4 or fd == 5) :
            amt = tfd * 210
        if (fd == 6 or fd == 7 or fd == 8) :
            amt = tfd * 190
        if (fd == 9) :
            amt = tfd * 240
        if (fd == 10 or fd == 11 or fd == 12) :
            amt = tfd * 210
        tamt += amt
        choice = int(input("Do you want to place more order? Enter \'1\' for YES and \'2\' for NO:\n"))
        if (choice == 2) :
            return tamt
        if (choice != 1 and choice != 2) :
            err()
    return tamt

#Desserts
def des() :    
    d = 0
    damt = 0
    totald = 0
    tamt = 0
    choice = 1
    print("\nCool with Desserts: Welcome to the Desserts Menu\n")
    print("Desserts\t\t\t    Price in Rs.\n")
    print("1.  Softy Pineapple \t\t\t  110")
    print("2.  Softy Crunchy Chocolate \t\t  110")
    print("3.  Chocolate Walnut Brownie \t\t   90")
    print("4.  Choco-Vanilla Doughnut \t\t  100")
    print("5.  Marbled Lava Cake \t\t\t   80")
    print("6.  Mocha Magic \t\t\t   90")
    print("7.  Black Forest Gateaux \t\t   90")
    print("8.  Mango Shake \t\t\t   80")
    print("9.  Pineapple Shake \t\t\t   80")
    print("10. Tooty Fruity Mocktail \t\t  100")
    print("11. Super Swinger Sundae \t\t  115")
    print("12. Arctic Royale \t\t\t  125")
    print("\nPress 0 to go back\n")
    while (choice == 1) :
        d = inp(6)
        if (d == 0):
            return tamt
        totald = plt()
        if (d == 1 or d == 2) :
            damt = totald * 110
        if (d == 3) :
            damt = totald * 90
        if (d == 4) :
            damt = totald * 100
        if (d == 5) :
            damt = totald * 80
        if (d == 6 or d == 7) :
            damt = totald * 90
        if (d == 8 or d == 9) :
            damt = totald * 80
        if (d == 10) :
            damt = totald * 100
        if (d == 11) :
            damt = totald * 115
        if (d == 12) :
            damt = totald * 125
        tamt += damt
        choice = int(input("Do you want to place more order? Enter \'1\' for YES and \'2\' for NO:\n"))
        if (choice == 2) :
            return tamt
        if (choice != 1 and choice != 2) :
            err()
    return tamt

#Bill
def bill(samt,mcamt,desamt,tamt,mod) :
    gst = 0
    print("\n\n-----------------------------------------------------------------")
    print("************* MULTI CUISINE RESTAURANT *************")
    print("\t************* BILL *************")
    print("Starters = Rs." + str(samt))
    print("Main Course = Rs." + str(mcamt))
    print("Desserts = Rs." + str(desamt))
    print("Total cost = Rs." + str(tamt))
    gst = (5 / 100.0 * tamt)
    print("GST % = '5%' of total cost")
    print("GST in Rupees = Rs." + str(gst))
    print("Amount to be paid = Rs." + str((tamt + gst)) + " including GST")
    print("\nMode of Payment: " + mod)
    print("\n-----------------------------------------------------------------")

#Error Message
def err() :
    print("\nERROR! Invalid Input!")
    print("Please follow the instructions and try again!\n")

#Closing Message
def thnx() :
    print("\n\nThanks for coming to the Multi-Cuisine Restaurant!!")
    print("Visit Again!!!")
    print()

#Selection Input Processor
def inp(x) :    
    while (1) :
        i = int(input("Choose your item from the above list by entering number:\n"))
        if (x == 1 or x == 2) :
            if (i > 10 or i < 0) :
                err()
            else :
                break
        elif(x == 3 or x == 4 or x == 5 or x==6) :
            if (i > 12 or i < 0) :
                err()
            else :
                break
    return i

#Plates Input Processor
def plt() :    
    while (1) :
        i = int(input("How many plates do you want to order from the above list? (Press '0' to cancel):\n"))
        if(i<0):
            err()
        elif(i==0):
            print("\nSelection cancelled successfully.\n")
            break
        elif(i>50):
            print("\nWe are sorry, we are unable to process orders of more than 50 plates at a time.")
            print("ORDER NOT ACCEPTED.\n")
        else:
            break
    return i

#Main Function
def main():
    samt = mcamt = desamt = 0
    print("WELCOME TO THE MULTI-CUISINE RESTAURANT!\n")
    while(1):
        ch = mm()
        if (ch == 1):
            samt += starters()
        elif (ch == 2):
            mcamt += mcourse()
        elif (ch == 3):
            desamt += des()
        elif(ch == 0):
            mod = input("Enter Mode of Payment:")
            tamt = samt + mcamt + desamt
            bill(samt,mcamt,desamt,tamt,mod)
            thnx()
            print("\nPress 'Enter' key to exit.")
            x=input()
            os.system('cls')    #Clearing screen after complete execution
            exit()
        else:
            err()

os.system('cls')    #Clearing screen before starting (for Windows OS)
main()              #Running the main function