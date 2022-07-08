# Made by @v6nom on Github
# >>> https://github.com/v6nom/sk-tools

import requests
from bs4 import BeautifulSoup
import random
import os
import time
from pystyle import Add, Colorate, Colors, Box, Write
import sys
from colorama import Fore
import fade


def clean():
    time.sleep(5)
    os.system('cls')
    main()


def teletype_print(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)


def generator():
    sk_key_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    length_short = 24
    length_medium = 34
    length_long = 99

    try:
        amount = Write.Input(f"\n[?] How many sk key you want to generate [X for unlimited] -> ", Colors.blue_to_cyan,
                             interval=0.035)

        if amount == "x" or amount == "X":
            pass
        else:
            for _ in amount:
                if not str.isdigit(amount):
                    Write.Print("\n[!] Your character is not a number", Colors.blue_to_purple, interval=0.05)
                    clean()

        teletype_print(f"\n[{Fore.LIGHTCYAN_EX}1{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Length Short", 0.035,
                       add_new_line=True)
        teletype_print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}2{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Length Medium", 0.035,
                       add_new_line=True)
        teletype_print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}3{Fore.WHITE}] {Fore.LIGHTCYAN_EX}Length Long", 0.035,
                       add_new_line=True)
        teletype_print(f"\n{Fore.LIGHTCYAN_EX}> {Fore.WHITE}Select an option: ", 0.07, False)
        choice_length = input()
        print("")
        if amount == "X" or amount == "x":
            while True:
                if choice_length == "1":
                    end_sk_key_short = "".join(random.sample(sk_key_string, length_short))
                    sk_key_generated_short = "sk_live_" + end_sk_key_short
                    with open(f"[GENERATED] SK Key Short.txt", "a") as f:
                        f.write(f"{sk_key_generated_short}\n")
                    Write.Print(f"{sk_key_generated_short}\n", Colors.blue_to_purple, interval=0)

                elif choice_length == "2":
                    end_sk_key_medium = "".join(random.sample(sk_key_string, length_medium))
                    sk_key_generated_medium = "sk_live_" + end_sk_key_medium
                    with open(f"[GENERATED] SK Key Medium.txt", "a") as f:
                        f.write(f"{sk_key_generated_medium}\n")
                    Write.Print(f"{sk_key_generated_medium}\n", Colors.blue_to_purple, interval=0)

                elif choice_length == "3":
                    end_sk_key_long = "".join(random.choices(sk_key_string, k=length_long))
                    sk_key_generated_long = "sk_live_" + end_sk_key_long
                    with open(f"[GENERATED] SK Key Long.txt", "a") as f:
                        f.write(f"{sk_key_generated_long}\n")
                    Write.Print(f"{sk_key_generated_long}\n", Colors.blue_to_purple, interval=0)
    except KeyboardInterrupt:
        print(fade.purplepink("\n[!] The SK Key has been successfully saved in a file !"))
        clean()
    else:
        try:
            amount = int(amount)
            for x in range(amount):
                if choice_length == "1":
                    end_sk_key_short = "".join(random.sample(sk_key_string, length_short))
                    sk_key_generated_short = "sk_live_" + end_sk_key_short
                    with open(f"[GENERATED] {amount} SK Key Short.txt", "a") as f:
                        f.write(f"{sk_key_generated_short}\n")
                    Write.Print(f"{sk_key_generated_short}\n", Colors.blue_to_purple, interval=0)

                elif choice_length == "2":
                    end_sk_key_medium = "".join(random.sample(sk_key_string, length_medium))
                    sk_key_generated_medium = "sk_live_" + end_sk_key_medium
                    with open(f"[GENERATED] {amount} SK Key Medium.txt", "a") as f:
                        f.write(f"{sk_key_generated_medium}\n")
                    Write.Print(f"{sk_key_generated_medium}\n", Colors.blue_to_purple, interval=0)

                elif choice_length == "3":
                    end_sk_key_long = "".join(random.choices(sk_key_string, k=length_long))
                    sk_key_generated_long = "sk_live_" + end_sk_key_long
                    with open(f"[GENERATED] {amount} SK Key Long.txt", "a") as f:
                        f.write(f"{sk_key_generated_long}\n")
                    Write.Print(f"{sk_key_generated_long}\n", Colors.blue_to_purple, interval=0)

        except KeyboardInterrupt:
            Write.Print("\n:) Have a nice day and see you later !", Colors.cyan_to_blue, interval=0.05)
            sys.exit()
        finally:
            print(fade.purplepink("\n[!] The SK Key has been successfully saved in a file !"))
            clean()


def checker():
    try:
        sk_file = Write.Input(f"\n[?] Drag the file containing SK Key -> ", Colors.blue_to_purple, interval=0.05)
        print("")
        if not os.path.isfile(sk_file):
            print(fade.purplepink("\n[!] The file doesn't exists"))
            clean()
        else:
            with open(sk_file, mode='r') as f:
                keys = f.read().splitlines()
            for sk_key in keys:
                url = f"https://shisuichk.xyz/api/sk.php?lista={sk_key}"
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')

                username = soup.find_all('span')[0].text.replace('[ ♛ Shisui ♛ ]', f'[v6nom]')
                information = soup.find(class_="text-warning").text
                status = soup.find_all('span')[2].text.replace('#Dead', 'DEAD').replace('#Live', 'LIVE')
                sk_key_checker = soup.find(class_="text-primary").text
                error = soup.find_all('span')[4].text
                text = username + information + status + sk_key_checker + error
                if status == "[DEAD] -» ":
                    Write.Print(f"{text}\n", Colors.dark_red, interval=0)
                else:
                    Write.Print(f"{text}\n", Colors.blue_to_cyan, interval=0)

                if status == "[LIVE] -» ":
                    with open("[VALID] SK Key.txt", "a") as f:
                        f.write(f"{sk_key}\n")
                        print(fade.purplepink("\n[!] The SK Key valid has been successfully saved in a file !"))
    except KeyboardInterrupt:
        Write.Print("\n:) Have a nice day and see you later !", Colors.cyan_to_blue, interval=0.05)
        sys.exit()
    finally:
        time.sleep(2)
        clean()


def main():
    os.system('mode con: cols=200 lines=60')
    try:
        text_banner = fade.greenblue("""
     ::::::::  :::    :::          :::    ::: :::::::::: :::   ::: 
    :+:    :+: :+:   :+:           :+:   :+:  :+:        :+:   :+:  
   +:+        +:+  +:+            +:+  +:+   +:+         +:+ +:+    
  +#++:++#++ +#++:++             +#++:++    +#++:++#     +#++:      
        +#+ +#+  +#+            +#+  +#+   +#+           +#+        
#+#    #+# #+#   #+#           #+#   #+#  #+#           #+#         
########  ###    ###          ###    ### ##########    ###     """)

        banner = fade.water("""
                                                              ..::^~!!!~~.
                                                           .:^~!777777??7!:
                                                      .:^!7???JJJJJJJ~77!: 
                                ..::++++++::..      !??JJ???????JJJ7!7~.  
                            .:^~!77?????????77!^:.  ~7!~^^^^^7??JJ77~:    
                         .:~!7??JJJJJYYYYJJJJJ??7!~:  .....::~????7~:      
                       .^!7?JJYYYYY5555YYYYYYJJJ???7~.   .:^7JJ?7^.        
                      ^7?JJYYYY555P555555555YYJJJYJJ?!: .^7?J?!^.          
                    .~?JJYY555PPPP555555555YYY5555YJ?!^~7J?7~:             
                    !?JYY555PPPPPPPPPPP55555PPPP55J7!!?J?!:.               
                   ^?JYY555555PPPPPP5555PPGGGPP5J7!?JJJ7:                  
                   !JJYY5555PPPPP555PPGGGGGG5J?77JJJJJ?!.                  
                   7JJYY555555555PPGGGGGG5J?7?JJYYYYYJ?!.                  
                .^!?JJYYYY555PPGGGGGGP5J77?JYYYY555YJJ7:                   
              :~7??7?JYY55PPGGGGGP5J?77?JYYY555555YYJ?^                    
           .^7?J?!^.~JY55PPPPP5J?77?JJYY55PPP5555YYJ7^                     
         :~7?J?~:.   ^?YYJJ?7!77?JYY555PP555555YYJ?~.                      
      .^!7?J?!^:..    :~~!77?JJYY555555555555YYJ7~:                        
    .^!7?J??7^:::^^~!77?????JYY5555555555YYJ?7~:.                          
  .^!!7JJ?????77???J??7~^. .^~!7?JJJJJ??7!~:.                              
 :~77^?JJJJ??????7!^:.           ..:...                                    
.!77?7777777!~^:.                                       
.~!!!!!~^:..
\n""")
        print(Add.Add(banner, text_banner, center=True))
        print(Colorate.Diagonal(Colors.blue_to_cyan, Box.Lines("Welcome to SK Tools")))
        print(f"[{Fore.CYAN}1{Fore.WHITE}] {Fore.CYAN}SK Key Generator")
        print(f"{Fore.WHITE}[{Fore.CYAN}2{Fore.WHITE}] {Fore.CYAN}SK Key Checker \n")

        teletype_print(f"{Fore.CYAN}> {Fore.WHITE}Select an option: ", 0.07, False)
        choice = input()

        if choice == "1":
            generator()

        if choice == "2":
            checker()

        for _ in choice:
            if not str.isdigit(choice):
                Write.Print("[!] Your character is not a number", Colors.blue_to_purple, interval=0.03)
                clean()
        if choice not in {"1", "2"}:
            Write.Print(f"[!] Your choice is not valid", Colors.blue_to_purple, interval=0.03)
            clean()

    except KeyboardInterrupt:
        Write.Print("\n:) Have a nice day and see you later !", Colors.cyan_to_blue, interval=0.03)
        sys.exit()


main()
