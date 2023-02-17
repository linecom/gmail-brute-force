#!/usr/bin/python3
import argparse


#
# Connect to GMail's SMTP server 
#

def smtp():
    print()

#
# help output 
#

def help():
    print()


def cmd_parse(): 
    # Create the parser and add arguments
    parser = argparse.ArgumentParser(prog="gmail-brute-force.py", 
             description="Brute-force GMail accounts",
             epilog="Made for educational purposes. Creator: Olivia Gallucci")
    parser.add_argument("target_email", help="email you want to attack")
    parser.add_argument("password_list", help="/path/password_list.txt")
    parser.add_argument("attack_duration", help="amount of seconds you want to wait between attacks")
    # parser.add_argument('--c', dest='--email', help="Target email")
    # parser.add_argument(dest='--plist', help="Password list")


    # Parse and print the results
    args = parser.parse_args()
    print(args.argument1)


def main():
    # user initial input 
    cmd_parse()
    user_input = 'q' # input("prompt")


    while user_input != "q":
        print()


        user_input = input("prompt")

    print()


if __name__ == "__main__":
    main()
