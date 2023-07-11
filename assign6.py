rollno =  int(input("Enter your Rollno: "))
name =  str(input("Enter your Name: "))
def ds(rollno,name):
    l = [rollno,name]
    print("For List: ")
    print(l)
    t = (rollno,name)
    print("For Tuple: ")
    print(t)
    s = {rollno,name}
    print("For Set: ")
    print(s)
    d = {
         "name":name, 
         "roll" : rollno
    }
    print("For Dictionary: ")
    print(d)

    print()

    print("List Value Changed")
    l[0] = 86
    l[1] = "XOXO"
    print(l)
    print("Tuple Value changed")
    templ = list(t)
    templ[1]= "helloUser"
    t = tuple(templ)
    print(t)
    print("Set Value changed")
    s.remove(rollno)
    s.remove(name)
    s.update("Codeworld")
    print(s)
    print("Dictionary Value changed")
    d.update({rollno:816})
    d.update({name:"lazy"})
    print(d)

    print()
    del l
    del t
    del s
    del d
    print("Deletion Successful!")
    print()
ds(rollno,name)

