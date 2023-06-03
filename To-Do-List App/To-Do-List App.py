class Task():
    
    """This program allows you manage your to-do list and is fully 
    tested from the point of view of users. 
    It's also very user friendly"""
    
    
    def __init__(self):
        
        self.tasks = []
        self.active_tasks = []
        self.completed_tasks = []
        
        
    # all users to find help 
    def app_help(self):
        
        print("""You can use this app to create to-do-lists and manage your tasks:\n
                          - use create_task() to create new tasks\n
                          - delete_task() to delete a single task \n
                          - delete_all_tasks() to delete all task from your main list\n
                          - create_active_tasks() to create an active task list\n
                          - create_completed_tasks() to mark a single task as complete\n
                          - all_tasks_completed() to mark all as complete\n
                          - delete_completed_tasks() deletes everything in completed list\n
                          - show_status() shows status of all tasks""")
        
        
    # allow users to create tasks
    def create_task(self):
        
        while True:
            
            new_tasks = input('Enter new tasks or Q or q to quit:\n')
            
            if new_tasks == "Q" or new_tasks == 'q':
                break 
                
            elif new_tasks == '':
                print("Please add a task!!")
                continue
                
            else:
                self.tasks.append(new_tasks)
                
                if len(self.tasks) != 0:
                    print("\n")
                    print(f"Your Tasks are:{self.tasks}")
                    
    
    # allow users to delete a single task from main list
    def delete_task(self):
        
        if len(self.tasks) == 0:
            
            print("You don't have anything in your task list")
        
        else:
            while True:
                
                delete_task = input('Enter the task number to be deleted or Q/q to quit:')
                
                if delete_task == 'q' or delete_task == 'Q':
                    break
                else:
                    try:
                        try:
                            self.tasks.pop(int(delete_task))
                            print("Task Deleted\n")
                            print(f"Your Tasks are:{list(enumerate(self.tasks))}")
                            if len(self.tasks) == 0:
                                print("You don't have any pending tasks")
                                break 
                        except IndexError:
                            print("Please enter the number within task length range")
                        
                    except ValueError:
                        print("Please enter either task number or q/Q")
    
    # Allow users to delete all tasks from main and active lists
    def delete_all_tasks(self):
        
        if len(self.tasks) != 0:
            self.tasks.clear()
            self.active_tasks.clear()
            print("All tasks are clear")
            
        else:
            print("You don't have any task in your list")
            
    # allow users to create active tasks
    def create_active_tasks(self):
        
        if len(self.tasks) !=0: 
            self.active_tasks = self.tasks[:]
            print(f"Your active tasks are:{self.active_tasks}")
            
        else:
            print("You don't have any task in tasks list")
            
            while True:
                new_task_input = input("Want to create new tasks?:yes or no").lower()
                
                if new_task_input == "yes":
                    self.create_task()
                    break
                if new_task_input == "no":
                    break
                if new_task_input not in ["yes", "no"]:
                    print("Please enter either yes or no")
                
    # allow users to mark a task as complete
    def create_completed_tasks(self):
        
        if len(self.active_tasks) == 0:
            print("You don't have anything in your active task list")
        
        else:
            
            while True:
                
                completed_input = input("Enter task number to mark as complete or Q/q to quit")
                
                if completed_input == 'Q' or completed_input == 'q':
                    break
                    
                else:
                    try:
                        try:
                            popped_task = self.active_tasks.pop(int(completed_input))
                            self.tasks.remove(popped_task)
                            self.completed_tasks.append(popped_task)
                            
                            print("\n")
                            print(f"Your completed tasks are: {self.completed_tasks}\n")
                            
                            if len(self.active_tasks) == 0:
                                print("Great Job 🎉 All Done!!")
                                break
                            else:
                                print(f"Your active tasks are:{list(enumerate(self.active_tasks))}")
                                
                        except IndexError:
                            print("Please enter number within task range")
                            
                    except ValueError:
                        print("Please enter either task number or Q/q")
                        
    # allow users to mark all tasks as completed
    def all_tasks_completed(self):
        
        if len(self.active_tasks) == 0:
            print("You don't have anything in your active task list")
        else:
            self.completed_tasks = self.active_tasks[:]
            print(f"Your completed tasks are: {list(enumerate(self.completed_tasks))}\n")
            
        
    # to delete all completed tasks
    def delete_completed_tasks(self):
        
        if len(self.completed_tasks) == 0:
            
            print("There is nothing to delete")
        else:
            self.completed_tasks.clear()
            
            print("Completed tasks are deleted")
            
    # allow users to see all task list status
    def show_status(self):
        
        print("Here is the detail of your task lists:\n")
        
        if len(self.tasks) == 0:
            print("Your task list: All Done 🥰 \n")
        else:
            print(f"Your task list:{self.tasks}\n")
        
        if len(self.active_tasks) == 0:
            print("Your active tasks are: All Done 🥰 \n")
        else:
            print(f"Your active tasks are: {self.active_tasks}\n")
            
        if len(self.completed_tasks) == 0:
            print(f"Your completed tasks are: All Done 🥰 \n")
        else:
            print(f"Your completed tasks are: {self.completed_tasks}\n")
                                         