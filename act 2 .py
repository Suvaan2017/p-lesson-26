class Employee:
        def __init__(self) :
         print ("Employee created")
        def __del__(self):
            print ("Destructor called, Employee deleted.")
def Create_obj():
            print ('making object....')
            obj = Employee()    
            print ('function end....')
            return obj
print ('Calling Create_obj()')
obj = Create_obj()
print ('program end....')