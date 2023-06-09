import os
import glob 

def my_notes():
    
    if len(glob.glob("*.txt")) == 0:
        print("You don't have any notes")
        
    else:
        print("Your notes are:\n")
        for file in os.listdir():
            if file.endswith(".txt"):
                print(file)
    
def create_note():
    
    note_name = input("Please enter a note name\n")
    
    if ".txt" in note_name:
        note_name = note_name
    else:
        note_name = note_name + ".txt"
         
    try:
        with open(note_name, 'x') as note:
            note.write('')
            
    except FileExistsError:
        
         print('Ohho! this note name already exist. Try again.')
            
    else:
        print("Your note created. You can start writing now")
        my_notes()
    
def write_note():
    
    if len(glob.glob("*.txt")) == 0:
        print("You don't have any notes")
    
    else:
        notename = input('Enter the name of the note to work with\n')
        
        if ".txt" in notename:
            notename = notename
        else:
            notename = notename + ".txt"
        
        if not os.path.exists(notename):
            print("Note does not exist. Please create a new note.")   
            
        else:
            with open(notename, 'a') as note:
                while True:
                    take_note = input("Please enter your texts or Q/q to exit \n")
                    if take_note in ["q", "Q"]:
                        break
                    else:
                        note.write(take_note + "\n")
                        
            with open(notename, 'r') as note:
                content = note.read()
                print("your updated note is: ")
                print(content)
            
def delete_note():
    
    if len(glob.glob("*.txt")) == 0:
        print("You don't have any notes")
    
    else:
        
        filename = input("Enter the note name to be deleted forever\n")
        if ".txt" in filename:
            filename = filename
        else:
            filename = filename + ".txt"
            
        if os.path.exists(filename):
            os.remove(filename)
            print("\nYour note has been deleted")
        else:
            print('This note does not exist')
    
    
        
def delete_all():
    
    if len(glob.glob("*.txt")) == 0:
        print("You don't have any notes")
    
    else:
        for file in os.listdir():
            if file.endswith(".txt"):
                os.remove(file)
                print("All your notes has been deleted.")
                
def view_all():
    
    if len(glob.glob("*.txt")) == 0:
        print("You don't have any notes")
        
    else:
        print(f"Your notes overviews\n")
        for file in os.listdir():
            if file.endswith(".txt"):
                with open(file) as f:
                    print(f"Your {file} note contains: \n{f.read()}")
                    
def update_note():
    
    view_all()
    
    choice = input("choose a note you want to update\n")
    
    if ".txt" in choice:
        choice = choice
    else:
        choice = choice + ".txt"
        
    if not os.path.exists(choice):
        print("Note does not exist. Please create a new note.")
        
    else: 
        print("\nYour note choice is:\n", choice)
        print("\n")
        print("Enter your preference:\n")
        print("Clear note content: 1")
        print("Rewrite note content: 2")
        print("Delete a word/replace a word/insert word or a sentence at a position: 3")
        
        try:
            action = int(input("Enter a choice between 1, 2, 3\n"))
            
        except ValueError:
            print("Please enter the mentioned choice only\n")
    
        else:
            if action not in [1, 2, 3]:
                print('Please enter a valid value\n')
        
            elif action == 1:
                with open(choice, 'w') as file:
                    file.write(' ')
                    print("Your note content is cleared.")
            
            elif action == 2:
                
                with open(choice, 'w') as note:
                    while True:
                        take_note = input("Please enter your texts or Q/q to exit \n")
                        
                        if take_note in ["q", "Q"]:
                            break
                        else:
                            note.write(take_note + "\n")
                            
                with open(choice) as note:
                    print("your updated note is: ")
                    print(note.read())
                    
            elif action == 3:
                
                with open(choice, "r+") as file:
                    content = file.read().split()
                    print("Content length is:", len(content))
                    print("Your content is:", ' '.join(content))
                    
                    try:
                        cursor_input = int(input("Enter the word position to replace a word or insert a sentence or enter above range for adding something to end \n."))
                        cursor = file.seek(cursor_input - 1)
                        print("\nYour modified position now is:", cursor_input)
                        
                        try:
                            content.pop(cursor)
                            
                        except IndexError:
                            print("Please enter the value within range to update word or add something new else it will be added to the end")
                    
                    except ValueError:
                        print("Enter number only within range")
                    
                    else:
                        replacement_input = input("Enter the word/sentence to added at the position. Hit enter if you just want to delete the word at that position.")
                        content.insert(cursor, replacement_input)
                        content = ' '.join(content)
                        print(content)
                        with open(choice, "w") as file:
                            file.write(content)
