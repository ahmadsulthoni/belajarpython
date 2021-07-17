#class MyClass:
 #   nama = "Sulthoni"

#name = MyClass()
#print (name.nama)

class person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age

    def myfunc(abc):
        print ("Hallo nama saya adalah " + abc.name)
        print ("Umur saya adalah " + str(abc.age))

run = person("john", 30)
run.myfunc()

#print (run.name)
#print (run.age)