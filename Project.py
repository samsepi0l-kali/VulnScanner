import socket, os, http.client, urllib.parse, re, ipaddress #requests  #nmap, 
import platform
import random, codecs
from datetime import datetime

#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import pymysql


while True:

    print("      ______ _                 _     _                   ")         
    print("      | ___ \ |               | |   | |                   ")        
    print("      | |_/ / | ___   ___   __| |___| |_ _ __ ___  __ _ _ __ ___ ") 
    print("      | ___ \ |/ _ \ / _ \ / _` / __| __| '__/ _ \/ _` | '_ ` _ \ ")
    print("      | |_/ / | (_) | (_) | (_| \__ \ |_| | |  __/ (_| | | | | | |   ")
    print("      \____/|_|\___/ \___/ \__,_|___/\__|_|  \___|\__,_|_| |_| |_|    ")
    print("")                                                                            
    print("")
    print("                       ----------By Ashish & Aditya---------")


    print("\n 1: PortScanner")
    print("\n 2: Version Detection & Vulnerability Analysis")#Matplotlib to be used to analyse vulnerability
    print("\n 3: URLs Bruteforce Check")
    print("\n 4: Password Bruteforce")
    print("\n 5: Ping Sweep")
    print("\n 6: Bruteforce")
    print("\n 7: Rot13 Algo")
    print("\n 8: Exit")
    print("\n------------------Thanks for using our program------------------")


    menu_option = int(input("\nChoose Options: "))

#***********************************************PORT SCANNER*********************************************************
    if menu_option == 1:
        #Port Scanner
        print("\n Choose one:")
        print("\n 1: Single target")
        print("\n 2: Subnet of target")
        target = int(input("\nEnter Choice: "))

        print("\n Choose one:")
        print("\n 1: Range of Ports")
        print("\n 2: Single Port")
        cport = int(input("\nEnter Choice: "))
        
        #Single Target and Range of Ports
        if target == 1 and cport == 1:
            print("\nChoose Method: ")
            print("\n 1: Transmission Control Protocol")
            print("\n 2: User Datagram Protocol")

            method = int(input("\nEnter Choice: "))
        

            if method == 1:
                while True:
                    user_defined_ip = input("\nEnter an IP address that you want to scan: ")
                    try:
                        verify_ip = ipaddress.ip_address(user_defined_ip)
                        print("The entered IP address is valid")
                        break
                    except:
                        print("INVALID INTERNET PROTOCOL ADDRESS!!")



            
                while True:
                    user_defined_port = input("\Enter the port range that you want to scan: ")


                    try:
                        min_port = int(user_defined_port.split('-')[0])
                        max_port = int(user_defined_port.split('-')[1])
                        break

                    except:
                        print("\nSPECIFY A PORT RANGE!!")     



                for port in range(min_port, max_port):
                    scan_ports_sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    status = scan_ports_sockets.connect_ex((user_defined_ip, port))
                    if (status == 0):
                        print("\nPORT", port, "- OPEN")
                    else:
                        print("\nPORT", port, "- CLOSED")
                    scan_ports_sockets.close()
        
                print("Socket Response =",status)
                check = input("\nDo you want to quit or go back to the main menu? enter any key to restart or type 'exit' to end: ")
                if check.upper() == "":
                    continue
                elif check.upper() == "exit":
                    print("BYE")
                    quit()


            elif method == 2:
        
                while True:
                    user_defined_ip = input("\nEnter an IP address that you want to scan: ")
                    try:
                        verify_ip = ipaddress.ip_address(user_defined_ip)
                        print("The entered IP address is valid")
                        break
                    except:
                        print("INVALID INTERNET PROTOCOL ADDRESS!!")



            
                while True:
                    user_defined_port = input("\nEnter the port range that you want to scan: ")


                    try:
                        min_port = int(user_defined_port.split('-')[0])
                        max_port = int(user_defined_port.split('-')[1])
                        break

                    except:
                        print("\nSPECIFY A PORT RANGE!!")     



                for port in range(min_port, max_port):
                    scan_ports_sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    status = scan_ports_sockets.connect_ex((user_defined_ip, port))
                    if (status == 0):
                        print("\nPORT", port, "- OPEN")
                    else:
                        print("\nPORT", port, "- CLOSED")
                    scan_ports_sockets.close()
        
                print("Socket Response =",status)
                check = input("\nDo you want to quit or go back to the main menu? enter any key to restart or type 'exit' to end: ")
                if check.upper() == "":
                    continue
                elif check.upper() == "exit":
                    print("BYE")
                    quit()  

        #Single Target and Single Port
        if target == 1 and cport == 2:
            print("\nChoose Method: ")
            print("\n 1: Transmission Control Protocol")
            print("\n 2: User Datagram Protocol")

            method = int(input("\nEnter Choice: "))

            if method == 1:
                while True:
                    user_defined_ip = input("\nEnter an IP address that you want to scan: ")
                    try:
                        verify_ip = ipaddress.ip_address(user_defined_ip)
                        print("The entered IP address is valid")
                        break
                    except:
                        print("INVALID INTERNET PROTOCOL ADDRESS!!")
            
                
                user_defined_port = int(input("\nEnter the port that you want to scan: "))                             
                scan_ports_sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                status = scan_ports_sockets.connect_ex((user_defined_ip, user_defined_port))
                if (status == 0):
                    print("\nPORT", user_defined_port, "- OPEN")
                else:
                    print("\nPORT", user_defined_port, "- CLOSED")
                    scan_ports_sockets.close()
        
                print("Socket Response =",status)
                check = input("\nDo you want to quit or go back to the main menu? enter any key to restart or type 'exit' to end: ")
                if check.upper() == "":
                    continue
                elif check.upper() == "exit":
                    print("BYE")
                    quit()


            elif method == 2:
        
                while True:
                    user_defined_ip = input("\nEnter an IP address that you want to scan: ")
                    try:
                        verify_ip = ipaddress.ip_address(user_defined_ip)
                        print("The entered IP address is valid")
                        break
                    except:
                        print("INVALID INTERNET PROTOCOL ADDRESS!!")



            
                user_defined_port = int(input("\nEnter the port that you want to scan: "))
                
                scan_ports_sockets = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                status = scan_ports_sockets.connect_ex((user_defined_ip, user_defined_port))
                if (status == 0):
                    print("\nPORT", user_defined_port, "- OPEN")
                else:
                    print("\nPORT", user_defined_port, "- CLOSED")
                    scan_ports_sockets.close()
        
                print("Socket Response =",status)
                check = input("\nDo you want to quit or go back to the main menu? enter any key to restart or type 'exit' to end: ")
                if check.upper() == "":
                    continue
                elif check.upper() == "exit":
                    print("BYE")
                    quit()
#***********************************************************END*****************************************************

















           



#***************************************************NOT FUNCTIONABLE*********************************************************

    elif menu_option == 2:
        print("noice abhi kucch nahi banaa hai !")


    elif menu_option == 3:
        print("noice abhi kucch nahi banaa hai !")



    elif menu_option == 4:
        print("noice abhi kucch nahi banaa hai !")






#***********************************************************END*****************************************************

















        


        

#***********************************************Ping Sweep*********************************************************


        
    elif menu_option == 5:
        #Ping Sweep
        net = input("Enter the Network Address: ")
        net1= net.split('.')
        a = '.'

        net2 = net1[0] + a + net1[1] + a + net1[2] + a
        st1 = int(input("Enter the Starting Number: "))
        en1 = int(input("Enter the Last Number: "))
        en1 = en1 + 1
        oper = platform.system()

        if (oper == "Windows"):
           ping1 = "ping -n 1 "
        elif (oper == "Linux"):
           ping1 = "ping -c 1 "
        else :
           ping1 = "ping -c 1 "
        t1 = datetime.now()
        print ("Scanning in Progress:")

        for ip in range(st1,en1):
           addr = net2 + str(ip)
           comm = ping1 + addr
           response = os.popen(comm)
           
           for line in response.readlines():
              if(line.count("TTL")):
                 break
              if (line.count("TTL")):
                 print (addr, "--> Live")
                 
        t2 = datetime.now()
        total = t2 - t1
        print ("Scanning completed in: ",total)
        check = input("\nDo you want to quit or go back to the main menu? enter any key to restart or type 'exit' to end: ")
        if check.upper() == "":
            continue
        elif check.upper() == "exit":
            print("BYE")
            quit()

#***********************************************************END*****************************************************


    elif menu_option == 6:
        password = str(input("Enter Password to Store in Memory: "))
        guess = " "

        while guess != password:
            guess = str(random.randint(0, 9999))
            print("=>", guess)

            if guess == password:
                print("Password Found!")
                print("=>", guess)


    

    elif menu_option == 7:
        print("This is a Python Based Rot13 Decoder")
        text_input = str(input("Enter Text: "))
        algo = codecs.encode(text_input, 'rot_13')
        print("OUTPUT: ", algo)



            


    elif menu_option == 8:
        quit()



    else:
        print("Invalid Option!")

    
