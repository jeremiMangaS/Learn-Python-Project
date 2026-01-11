# Still learning new things

taskList = []

def add_task() :
    inputTask = input("Add new task : ")
    taskList.append(inputTask)
    print("[System] New task added")

def show_tasks() :
    if len(taskList) < 1 :
        print("List is empty.")
    else :
        print("=============================")
        for i, task in enumerate(taskList) :
            print(f"{i + 1}, {task}")
        print("=============================")
        
def delete_task() :
    while True :
        try :
            show_tasks()
            indx = int(input("Enter the task index : "))
            if (indx - 1) <= len(taskList) and (indx - 1) > 0 : 
                delete_process(indx)
        except IndexError : 
            print("Out of range")
        except :
            print("")            
        # except : print("Input must be number")
        else : break

def delete_process(indx) :
    while True :
        print(f"{indx}. {taskList[indx - 1]}")
        usrinput = input("Confirm : [Y/n]")
        if usrinput == "Y" or usrinput == "y" :
            taskList.pop(indx - 1)
            print(f"Delete successfull")
            return
        elif usrinput == "N" or usrinput == "n" :
            print("Canceling...")
            return
        else : print("the answer should be just y or n")        
            
def main() :
    print("WELCOME TO-DO-LIST")
    while True :
        try :
            print("========== MENU ==========")
            print("1. add new task\n2. show tasks list\n3. Delete task\n0. Exit")
            inputMenu = int(input("Input : ")) 
        except :
            print("Input cannot be null and should be integer type!")
        if inputMenu == 1 : add_task()
        elif inputMenu == 2 : show_tasks() 
        elif inputMenu == 3 : delete_task()
        elif inputMenu == 0 : return False
        else : print("Menu unregistered")

main()