# Still learning new things

taskList = []

def add_task() :
    print("Add new task : ")
    inputTask = input()
    taskList.append(inputTask)

def show_tasks() :
    i = 1
    for i in taskList :
        print(i, ". ", i)
        ++i

def main() :
    print("WELCOME TO-DO-LIST")
    while True :
        print("Input : ")
        inputMenu = input()
        
