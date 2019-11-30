class node:
    def __init__(self,data_val=None):                               #it acts as a constructor of c++ 
        self.data_val=data_val
        self.next_val=None

class linked_list:
    def __init__(self):                                             #same as above
        self.head_val=None
first_linked_list=linked_list()                                     #initializing the first value as none 
second_linked_list=linked_list()                                    #initializing the second instance value as none 
def create_node():
    values=int(input("enter the number you want to print"))
    if first_linked_list.head_val == None:
        first_val=input("enter your 1st number:")
        first_linked_list.head_val=node(first_val)
        first_linked_list.head_val.next_val=None
        temp=first_linked_list.head_val                             #to create an instance of the fist node 
    else:                                                           #yedi tei variable liyo bbhaney tyo change hunxa so tesko instance
        pass                                                        #preserve garna lai gareko look traverse function for more detail
                                                                    #takes unique new value in this loop
    for value in range(1,values):
        data=input("enter your another number:")
        second_linked_list.head_val=node(data)
        second_linked_list.head_val.next_val=None
        temp.next_val=second_linked_list.head_val                   #linking previous node with new node
        temp=second_linked_list.head_val                            #making this node as previous
        

def traverse():
    temp=first_linked_list.head_val                                 #created the instance of first_linked_list to 
    if temp==None:                                                  #calculate the chain of node
        print("the list are empty")
    while temp is not None:
        print(temp.data_val)
        temp=temp.next_val


if __name__ == "__main__":
    create_node()
    traverse()
    
                      






    


    


    



