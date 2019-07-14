print("^^^^^^^^^^^^^^^^^MY LIBRARY^^^^^^^^^^^^^^^^^^^")
a1=input("Is your book Fiction or NON Fiction:")
if(a1=="Fiction"):
    b1=input("which genre this book belongs to:")
    if(b1=="Comedy"):
        print("This book belongs to shelf A")
    elif(b1=="Science Fiction"):
        print("This book belongs to shelf B")
    elif(b1=="Fantasy"):
        print("This book belongs to shelf C")
    elif(b1=="Historic Fiction"):
        print("This book belongs to shelf D")
    elif(b1=="Historic fiction"):
        print("This book belongs to shelf E")
elif(a1=="NON Fiction"):
    b1=input("which genre this book belongs to:")
    if(b1=="History & Geography"):
        print("This book belongs to shelf F")
    elif(b1=="Art"):
        print("This book belongs to shelf G")
    elif(b1=="Science and Technology"):
        print("This book belongs to shelf H")
    elif(b1=="Others"):
        print("This book belongs to shelf I")
else:
    print("Invalid shelf") 