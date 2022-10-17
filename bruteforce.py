import threading
import string


name=input("Enter the text : ")
''.join(sorted(set(name), key=name.index)) #Since it is a set, we write an element once.
letters=list(''.join(sorted(set(name), key=name.index)))
print(letters)

file=open("password.txt", "a")

def func():
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    for e in letters:
                        print(a + b + c + d + e)
                        file.write(a + b + c + d + e + "\n")


f=threading.Thread(target=func())
f.start()