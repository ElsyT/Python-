#=====importing libraries===========''


file = open('user.txt', 'r')
users = [line.strip().split(", ") for line in file] 
file.close()

#====Login Section====

attempts = 0
max_attempts = 3

while attempts < max_attempts:                # was unable to use while True : so more than 3 attempts are needed
    username = input('Enter your username: ')  
    password = input('Enter your password: ')

    found = False   # means no username found 
    for user_data in users:    # goes through the document to find the username
        if username == user_data[0] and password == user_data[1]:  # if true
            found = True  # means user name found
            break
    
    if found:
        print('You have successfully logged in.')   # if its found as false then else
        break   # did not know it was going to the next string hahahah of options
    else:   
        print('Incorrect credentials. Check if you have Caps Lock on and try again or call Admin.')
        attempts += 1    # increment is add by 1
        


while True:
 
 if username == 'admin' and password == 'adm1n':
    menu = input('''Select one of the following options:
r - register a user 
a - add task
va - view all tasks
vm - view my tasks
s - stats 
e - exit                
: ''').lower()

    if menu == 'r':
        
        # request for new registration information
        request_user = input("Please enter new username: ")
        request_pass = input("Please enter new password: ")
        new_confrimed = input("Please confirm new password: ")
        
        if request_pass == new_confrimed:  # Check if the password is the same as the username
            file = open("user.txt", 'a')   # added new information to the file
            file.write(f"\n{request_user}, {request_pass}\n")  
            file.close() 
            print("User successfully added!")
        else:
            print("Passwords do not match.") 


    elif menu == 'a':
        pass

        from datetime import datetime # this is to get the datetime (did not about this wow )

        Username = input("Please enter username of person assigned to task : ")  # request for information 
        title = input("Please enter title task name : ")
        discription = input("Please put in the description of the task: ")
        due_date = input ("When is the task due date year,month,date : ")
        
        current_date = datetime.now().strftime('%Y-%m-%d') #"string format time."
        status = 'No'

        file= open('tasks.txt','a') # add to file
        file.write(f"\n{Username}, {title}, {discription}, {due_date}, {current_date}, {status}\n") # puts in file in order of request 
        file.close()
        print("Task added successfully!")
     

    elif menu == 'va':
        
        file = open ('tasks.txt','r')
        lines = file.readlines()   # allows us to loop through the file 
        for line in lines:
         part=line.strip()    # to remove new line characters and comma
         part=part.split(', ') 
         if len(part) >= 6:
          print(f"Task:              {part[1]}\n"  # the first (1) part/ value of the file before the comma 
                  f"Assigned to:       {part[0]}\n"  # the first (0) part/ value of the file before the comma and so on
                  f"Date assigned:     {part[3]}\n"
                  f"Due date:          {part[4]}\n"
                  f"Task Complete ?:   {part[5]}\n"
                  f"Task Description:  \n {part[2]}\n")  


    elif menu == 'vm':
        
        file = open ('tasks.txt','r')
        lines = file.readlines()   # allows us to loop through the file 
        for line in lines:
         part=line.strip()    # to remove new line characters and comma
         part=part.split(', ')    
         if username == part[0]:  # the fist thing we asked for is the username wich is [0]
            print(f"Task:              {part[1]}\n"  # the first (1) part/ value of the file before the comma 
                  f"Assigned to:       {part[0]}\n"  # the first (0) part/ value of the file before the comma and so on
                  f"Date assigned:     {part[3]}\n"
                  f"Due date:          {part[4]}\n"
                  f"Task Complete ?:   {part[5]}\n"
                  f"Task Description:  \n {part[2]}\n") 
        file.close()
    
    elif  menu == 's': 
    # Read task data
        with open('tasks.txt', 'r') as user_file:
           task = len(user_file.readlines())
        

    # Read user data
        with open('user.txt', 'r') as user_file:
          users = len(user_file.readlines())

           # Display statistics
        print("Statistics:")
        print(f"Total number of tasks: {task}")
        print(f"Total number of users: {users}")
   
       
    elif menu == 'e':
     print('Goodbye!!!')
     exit()
    else:
        print("You have made entered an invalid input. Please try again")
    

 elif username != 'admin' and password != 'adm1n':
    menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit : ''').lower()
    
    
        
    if menu == 'va':
        
        file = open ('tasks.txt','r')
        lines = file.readlines()   # allows us to loop through the file 
        for line in lines:
         part=line.strip()    # to remove new line characters and comma
         part=part.split(', ') 
         if len(part) >= 6:
          print(f"Task:              {part[1]}\n"  # the first (1) part/ value of the file before the comma 
                  f"Assigned to:       {part[0]}\n"  # the first (0) part/ value of the file before the comma and so on
                  f"Date assigned:     {part[3]}\n"
                  f"Due date:          {part[4]}\n"
                  f"Task Complete ?:   {part[5]}\n"
                  f"Task Description:  \n {part[2]}\n")  


    elif menu == 'vm':
        
        file = open ('tasks.txt','r')
        lines = file.readlines()   # allows us to loop through the file 
        for line in lines:
         part=line.strip()    # to remove new line characters and comma
         part=part.split(', ')    
         if username == part[0]:  # the fist thing we asked for is the username wich is [0]
            print(f"Task:              {part[1]}\n"  # the first (1) part/ value of the file before the comma 
                  f"Assigned to:       {part[0]}\n"  # the first (0) part/ value of the file before the comma and so on
                  f"Date assigned:     {part[3]}\n"
                  f"Due date:          {part[4]}\n"
                  f"Task Complete ?:   {part[5]}\n"
                  f"Task Description:  \n {part[2]}\n")
         else: 
            print("Task not found, contact administrator") 
        file.close()

    elif menu == 'a':
       

        from datetime import datetime # this is to get the datetime (did not about this wow )

        Username = input("Please enter username of person assigned to task : ")  # request for information 
        title = input("Please enter title task name : ")
        discription = input("Please put in the description of the task: ")
        due_date = input ("When is the task due date (yyyy/mm/dd): ")
        
        current_date = datetime.now().strftime('%Y-%m-%d') #"string format time."
        status = 'No'

        file= open('tasks.txt','a') # add to file
        file.write(f" \n {Username}, {title},{discription},{due_date},{current_date},{status}\n") # puts in file in order of request 
        file.close()
        print("Task added successfully!")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

#Thank you for the template / mine does say I have 4 spaces I dont know (thank you!!!!!!!!!)
     