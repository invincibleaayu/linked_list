import sys
class Stack:
    def __init__(self,value=None):#initialize the value of top ,array
        self.value=value
        self.array_size=int(input("enter the capacity of your stack:-"))
        self.storage=list()

    def push(self):

        Range=int(input("how many number do youwant to add:-"))
        #print(Range)
        if Range < self.array_size:
            for value in range(0,Range):
                print(value)
                value=input("enter the value you wanna add:-")
                self.storage.append(value)
        else:
            print("this is the overflow condition!!! ")
            sys.exit()
if __name__ == "__main__":
    stack_obj=Stack()
    stack_obj.push()