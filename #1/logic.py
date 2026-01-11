def main() :
    print("WELCOME TO-DO-LIST")
    while True :
        inputMenu = None
        print("========== MENU ==========")
        print("1. add new task\n2. show tasks list\n3. Delete task\n0. Exit")
        if not int(input(inputMenu)) :
            print("Should be Integer type")
            exit()
        if inputMenu != int or inputMenu == None:
            print("Input cannot be null and should be integer")
        else :
            if inputMenu == 1 : print("Menu 1")
            elif inputMenu == 2 : print("Menu 2")
            elif inputMenu == 3 : print("Menu 3")
            elif inputMenu == 0 : return False
            else : print("Menu unregistered")

main()