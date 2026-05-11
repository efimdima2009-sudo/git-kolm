class Task:
    def __init__(self, name, time: float, description):
        self.name = name
        self.time = time
        self.description = description

    def __str__(self):
        return f"Name: {self.name}.\nTime: {self.time}.\nDescription: {self.description}. "
    
    def __repr__(self):
        return f"Name: {self.name}.\nTime: {self.time}.\nDescription: {self.description}. "
list_task = []
print("---To-do list---")
while True:
    list_of_options = ["Add", "Remove", 'Relook the list', "Exit"]
    for index, option in enumerate(list_of_options, start=1):
        print(index, option)

    option = int(input('What do you want to do with your list?(1-4) '))
    if option == 1:
        name_of_task = input("What`s name of the task? ")
        time_for_task = float(input("What`s time for the task? "))
        desc_of_task = input("Write description of your task ")
        task = Task(name_of_task, time_for_task, desc_of_task)
        list_task.append(task)
        for index, t in enumerate(list_task, start=1):
                print(index, t)
    elif option == 2:
        try:
            task_delete = input("Enter task you want to delete ")
            ind = list_task.index[task_delete]
            list_task.pop(ind)
        except IndexError:
            print("Enter only task that in the to-do list.")
    elif option == 3:
        if len(list_task) == 0:
            print("To-do list has no tasks.")
        else:
            print(list_task)
    elif option == 4:
        break
    else:
        print("There is no other options. Goodbye!!!")
        break