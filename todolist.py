tasks =[]
while True:
    print(".....TO-DO LIST APPLICATION.....")
    print("1.add task")
    print("2.view task")
    print("3.delete task")
    print("4.exit")
    
    choice=int(input("choose an option(1-4):"))
    
    if choice==1:
        task=input("enter the task:")
        tasks.append(task)
        print("task added sucessfully")
        
    elif choice==2:
        if(len(tasks)==0):
            print("no task available")
        else:
            print("your tasks are:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i]) 
    elif choice==3:
        if(len(tasks)==0):
            print("no task available")
        else:
            print("your tasks are:")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])

            remove=int(input("enter the task to remove:"))
            tasks.pop(remove-1)
            print("task removed successfully")
    elif choice==4:
        print("exiting the application")
        break
    else:
        print("invalid choice,try again.")