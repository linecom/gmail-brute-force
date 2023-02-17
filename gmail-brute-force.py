#!/usr/bin/python3
import argparse, smtplib

#
# Connect to GMail's SMTP server 
#

def smtp():
    server = smtplib.SMTP("smtp.gmail.com", 200)
    server.ehlo()
    server.starttls()
    return server

def cmd_parse(): 
    # Create the parser and add arguments
    parser = argparse.ArgumentParser(prog="gmail-brute-force.py", 
             description="Brute-force GMail accounts",
             epilog="Made for educational purposes. Creator: Olivia Gallucci")
    parser.add_argument("target_email", type=str, help="email you want to attack")
    parser.add_argument("password_list", type=str, help="[/path/password_list.txt] Each password should be on a new line")
    parser.add_argument("attack_duration", type=int, help="amount of seconds you want to wait between attacks")

    args = parser.parse_args()
    return args

    


def main():
    # user initial input 
    args = cmd_parse()

    print(args)

    # make a list of the passwords from a file 
    with open(args.password_list) as file:
        pass_list = file.readlines()
        
    # remove new line characters
    pass_list = [x.strip() for x in pass_list]
    print(pass_list)

    file.close()


    # Parse and print the results
    # args = parser.parse_args()
    # print(args.argument1)


    user_input = 'q' # input("prompt")


    while user_input != "q":
        print()


        user_input = input("prompt")

    print()


if __name__ == "__main__":
    main()
