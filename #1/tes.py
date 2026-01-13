# Still learning new things

taskList = {}
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
            # taskList.append(task.replace("\n", ""))
            x = task.split(" || ")
            x[1].replace("\n", "")
            intx = int(x[1])
            boolx = bool(intx)
            taskList[x[0]] = boolx
        f.close()

def add_task() :
    inputTask = input("Add new task : ")
    write_data(inputTask)
    # taskList.append(inputTask)
    taskList[inputTask] = False
    print("[System] New task added")

def write_data(inputTask) :
    with open(fileName, "a") as f :
        if len(taskList) == 0 :
            f.write(f"{inputTask} || 0")
        else : 
            f.write(f"\n{inputTask} || 0")
    f.close()

def show_tasks() :
    if len(taskList) == 0 :
        print("There's no task yet ...")
    else :
        print("=============================")
        for i, task in enumerate(taskList) :
            print(f"{i + 1}. {task} ", end='')
            if taskList[task] == False :
                print("[ ]")
            else :
                print("[v]")
        print("=============================")
        
def delete_task() :
    while True :
        try :
            show_tasks()
            indx = int(input("Enter the task index : "))
            print(type(indx))
            delete_process(indx)
        except IndexError : 
            print("Out of range")
        # except :
        #     print("Input must be a number")
        else : 
            break

def delete_process(indx) :
    while True :
        for i, key in enumerate(taskList) :
            if (indx - 1) == i :
                print(f"{indx}. {(key)} {taskList[key]}")
                usrinput = input("Confirm : [Y/n]")
                if usrinput == "Y" or usrinput == "y" :
                    taskList.pop(key)
                    push_newdata()
                    print(f"Delete successfull")
                    return
                elif usrinput.lower() == "n" :
                    print("Canceling...")
                    return
                else : print("the answer should be just y or n") 
            else :
                continue
    
def push_newdata() :
    f = open(fileName, "w")
    for i, key in enumerate(taskList) :
        task = f"{key} || "
        if taskList[key] == False :
            task = task + "0"
        else :
            task = task + "1"
        if i == 0 :
            f.write(f"{task}")
        else :
            f.write(f"\n{task}")

def status_task() :
    if len(taskList) == 0 :
        print("There's no task yet ...")
    else :
        print("=============================")
        for i, task in enumerate(taskList) :
            if taskList[task] == True : 
                continue
            print(f"{i + 1}. {task} ", end='')
            if taskList[task] == False :
                print("[ ]")
            else :
                print("[v]")
        print("=============================")
    try :
        inputStatus = int(input("Enter task index : "))
        for i, key in enumerate(taskList) : 
            if (inputStatus - 1) == i :
                taskList[key] = True
            else : continue
    except :
        print("Input must be a number")
    
    
            
def main() :
    get_data()
    print("WELCOME TO-DO-LIST")
    while True :
        try :
            print("========== MENU ==========")
            print("1. add new task\n2. show tasks list\n3. Delete task\n4. Change task status\n0. Exit")
            inputMenu = int(input("Input : ")) 
        except :
            print("Input cannot be null and should be integer type!")
        else :
            if inputMenu == 1 : add_task()
            elif inputMenu == 2 : show_tasks() 
            elif inputMenu == 3 : delete_task()
            elif inputMenu == 4 : status_task()
            elif inputMenu == 0 : return False
            else : print("Menu unregistered")

main()