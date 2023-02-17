#!/usr/bin/python3
import argparse, smtplib, os
from pprint import pprint

"""

also turn this into script -l0kueser vprolly

"""


#
# Connect to GMail's SMTP server 
#

def smtp():
    server = smtplib.SMTP("smtp.gmail.com", 200)
    server.ehlo()
    server.starttls()
    return server

#
# parse command line arguments entered by attacker 
#

def cmd_parse(): 
    # Create the parser and add arguments
    parser = argparse.ArgumentParser(prog="gmail-brute-force.py", 
             description="Brute-force GMail accounts",
             epilog="Made for educational purposes. Creator: Olivia Gallucci")
    parser.add_argument("target_email", type=str, help="email you want to attack")
    parser.add_argument("password_list", type=str, help="[/path/password_list.txt] Each password should be on a new line")
    parser.add_argument("attack_duration", type=int, help="amount of seconds you want to wait between 8 failed attacks")

    args = parser.parse_args()
    return args

#
# product display 
#

def product_display():
    # clear terminal 
    os.system("cls" if os.name == "nt" else "clear")
    # print title 
    print("*****                   *****" +
          "***** GMAIL BRUTE FORCE *****" + 
          "*****                   *****")
    

#
# execute the mail program 
#

def main():
    # attacker initial input 
    args = cmd_parse()

    # show product info
    product_display()
    
    print(args)

    # make a list of the passwords from a file 
    with open(args.password_list) as file:
        pass_list = file.readlines()
        
    # remove new line characters
    pass_list = [x.strip() for x in pass_list]
    file.close()

    print(pass_list)


    user_input = 'q' # input("prompt")

    # command input 
    while user_input != "q":

        # command list 
        # start attack
        # stop attack 
        # quit program 
        # [.... %90 percent finished ]
        # notify that it will wait for user input, so do not enter?? 

        print()


        user_input = input("prompt")

    print("end")


if __name__ == "__main__":
    main()
