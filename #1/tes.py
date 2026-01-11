# Still learning new things

taskList = []
fileName = "tugas.txt"

def get_data() :
    try :
        f = open(fileName, "r")
        if not f :
            raise FileNotFoundError
    except FileNotFoundError :  
        print("Making file...")
        f = open(fileName, "w")
    else :    
        for task in f.readlines() :
            taskList.append(task.replace("\n", ""))
        f.close()

def add_task() :
    inputTask = input("Add new task : ")
    write_data(inputTask)
    taskList.append(inputTask)
    print("[System] New task added")

def write_data(inputTask) :
    with open(fileName, "a") as f :
        if len(taskList) == 0 :
            f.write(f"{inputTask}")
        else : 
            f.write(f"\n{inputTask}")
    f.close()

def show_tasks() :
    if len(taskList) == 0 :
        print("There's no task yet ...")
    else :
        print("=============================")
        for i, task in enumerate(taskList) :
            print(f"{i + 1}. {task}")
        print("=============================")
        
def delete_task() :
    while True :
        try :
            show_tasks()
            indx = int(input("Enter the task index : "))
            delete_process(indx) 
        except IndexError : 
            print("Out of range")
        except :
            print("Input must be a number")
        else : 
            break

def delete_process(indx) :
    while True :
        print(f"{indx}. {taskList[indx - 1]}")
        usrinput = input("Confirm : [Y/n]")
        if usrinput == "Y" or usrinput == "y" :
            taskList.pop(indx - 1)
            push_newdata()
            print(f"Delete successfull")
            return
        elif usrinput.lower() == "n" :
            print("Canceling...")
            return
        else : print("the answer should be just y or n")  
    
def push_newdata() :
    f = open(fileName, "w")
    for i, task in enumerate(taskList) :
        if i == 0 :
            f.write(task)
        else :
            f.write(f"\n{task}")
    
            
def main() :
    get_data()
    print("WELCOME TO-DO-LIST")
    while True :
        try :
            print("========== MENU ==========")
            print("1. add new task\n2. show tasks list\n3. Delete task\n0. Exit")
            inputMenu = int(input("Input : ")) 
        except :
            print("Input cannot be null and should be integer type!")
        else :
            if inputMenu == 1 : add_task()
            elif inputMenu == 2 : show_tasks() 
            elif inputMenu == 3 : delete_task()
            elif inputMenu == 0 : return False
            else : print("Menu unregistered")

main()