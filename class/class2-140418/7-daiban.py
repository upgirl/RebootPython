#daiban while queue
#add  sssss append print input 
#do dayin 
#over exit()

task = []
while True:
    action = raw_input("Please input your action: ")
    if action == "add":
        thing = raw_input("Please input a thing: ")
        task.append(thing)
        print task
    elif action == "do":
        if len(task) == 0:
            print "No task, Bye !"
            break
        else:
            print "do %s" % task.pop(0)
            #print "do %s" % task.pop()

    
