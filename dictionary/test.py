import time
flag = False

user_input = input("Please enter a word you want to search:\n>> ").capitalize()
time.sleep(1.35)

with open('dictionary.txt', 'r') as file:
    for line in file:
        word_dict = {}
        splitted_line = line.split("  ")
        if len(splitted_line) == 2:
            word_dict[splitted_line[0]] = splitted_line[1]
            for key,value in word_dict.items():
                if user_input == key:
                    print(f'"{user_input}" means: ' + value)
                    flag = False
                    exit()
                else:
                    flag = True
                    continue
if flag:
    print("Dear user, the word you entered is not in the dictionary, do you wish to add it? (Yes or no)\n>> ")
    choice = input()
    if choice == "yes":
        meaning = input("Please enter the definition/meaning of the word you want to add:\n>> ")
        with open('dictionary.txt', 'a') as file:
            file.write(f'\n{user_input}  {meaning}\n')
            print("The word has been added, re-run the program and enter the word to see it's meaning.")
            exit()
    else:
        print("Okay then, thank you for using this program.")
        time.sleep(1/2)
        print("Exiting the program....")
        time.sleep(1.2)
        print("Bye, the program has been stopped.")
        exit()