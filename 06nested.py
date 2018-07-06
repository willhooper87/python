print("menu:")
print("3 - level 3")
print("4 - level 4")

examlevel = int(input("enter exam level: "))

if examlevel == 3:
    mark = int(input("enter level 3 mark: "))

    if mark > 65:
     print("pass")
    
    else:
        print("fail")

elif examlevel == 4:
    mark = int(input("enter level 4 mark:"))

    if mark > 50:
        print("pass")

    else:
         print("fail")

else:
    print("invalid level")
