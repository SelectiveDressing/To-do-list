import sys
import json
with open('old_list.json', 'r+') as data_file:
    data = json.loads(data_file.read())

def main():
    print("To Do list for Selective Dressing:")
    print("0: create new list.")
    print("1. Open existing list")
    just = input(" >  ")
    if just=="0":
        task1 = Task()
    elif just == "1":
        task1 = Task(data)
    else:
        sys.exit()

    while True:
        print("*"*50)
        print("1: Add a task")
        print("2: Remove a task")
        print("3: Show the list")
        print("4: Change a task")
        print("5: Sort the list")
        print("6: Update list")
        print("0: Exit")
        print("Select from the above menu")
        user = input("> ")
        if user == "1":
            print("Task to be added.")
            arg = input("> ")
            task1.add_task(arg)
        elif user == "2":
            print("Task to be removed.")
            arg = input("> ")
            task1.remove_task(arg)
        elif user == "3":
            task1.get_list()
        elif user == "4":
            arg = (input("Task to be changed: ")).lower()
            arg2 = (input("status, priority, or task")).lower()
            arg3 = (input("change to what?: ")).lower()
            task1.change_list(arg, arg2, arg3)
        elif user == "5":
            arg = (input("Sort the list by: status, priority, or task:")).lower()
            task1.sort_list(arg)

        elif user == "6":
            print("\nsaved")
            task1.save_list()
        elif user == "0":
            print("Exiting your To-Do list app.")
            sys.exit()
        else:
            print("That's not a valid selection")

class Task(object):
    """docstring for Task"""
    def __init__(self,task_list=[]):
        self.task_list = task_list
        
    def add_task(self,a_task,status="inprogress",priority="normal"):
        new_dict={}
        if a_task is not None:
            
            new_dict["task"]=a_task
            new_dict["status"]=status
            new_dict["priority"]=priority
            self.task_list.append(new_dict)
            print ("\n Task added to list!")
            return a_task
        else:
            print("Please give correct input.")

    def remove_task(self,r_task):
        if r_task is not None:
            for item in self.task_list:
                if r_task in item.values():
                    self.task_list.remove(item)
                    print("\n Task removed from the list.")
                    break
        else:
            print("Please give correct input.")

    def get_list(self):

        if len(self.task_list)!=0:
            print("Your list is: \n")
            for indx, task in enumerate(self.task_list):
                print("#{}: Task: {} \t\nStatus: {} \t\nPriority: {}".format(indx+1,task["task"],task["status"],task["priority"]))
                print("\n")
        else:
            print("Your list is Empty.")

    def sort_list(self,arg):
        if arg is not None:
            s_list = list(sorted(self.task_list,key=lambda k: k[arg]))
            for indx, task in enumerate(s_list):
                    print("#{}: Task: {} \t\nStatus: {} \t\nPriority: {}".format(indx+1,task["task"],task["status"],task["priority"]))
                    print("\n")

    def change_list(self,c_task,c_arg,c_new):
        if c_task is not None:
            for item in self.task_list:
                if c_task in item.values():
                    if c_arg == "task":
                        item["task"]=c_new
                        print("Your task name changed to {}".format(item["task"]))
                    elif c_arg == "status":
                        item["status"]=c_new
                        print("Your task status changed to {}".format(item["status"]))
                    elif c_arg == "priority":
                        item["priority"]=c_new
                        print("Your task priority changed to {}".format(item["priority"]))
                    else:
                        print("\n{} not found in the task.".format(c_arg))

    def save_list(self):
        if self.task_list is not None:
            for item in self.task_list:
                data.append(item)
            with open('old_list.json', 'w') as data_file:
                json.dump(data, data_file)
        else:
            print("Nothing to save.")



if __name__ == '__main__':
    main()
        
        