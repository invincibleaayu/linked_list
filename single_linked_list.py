class node:
    def __init__(self,data_val=None):                               #init acts as a constructor of c++ 
        self.data_val=data_val
        self.next_val=None

class linked_list:
    def __init__(self):                                             #same as above
        self.head_val=None
first_linked_list=linked_list()                                     #initializing the first value as none 
second_linked_list=node()                                           #initializing the second instance value as none 
def create_node():
    create_node.values=int(input("enter the number you want to print:-"))
    if first_linked_list.head_val == None:
        first_val=input("enter your 1st number:-")
        first_linked_list.head_val=node(first_val)
        first_linked_list.head_val.next_val=None
        temp=first_linked_list.head_val                             #to create an instance of the fist node 
    else:                                                           #yedi tei variable liyo bbhaney tyo change hunxa so tesko instance
        pass                                                        #preserve garna lai gareko look traverse function for more detail
                                                                    #takes unique new value in this loop
    for value in range(1,create_node.values):
        data=input("enter your another number:-")
        second_linked_list=node(data)
        second_linked_list.next_val=None
        temp.next_val=second_linked_list                            #linking previous node with new node
        temp=second_linked_list                                     #making this node as previous
        

def traverse():
    temp=first_linked_list.head_val                                 #created the instance of first_linked_list to 
    if temp==None:                                                  #calculate the chain of node
        print("the list are empty!!!!")
    while temp is not None:
        print(temp.data_val)
        temp=temp.next_val
def insert():
    position=int(input("enter the place you want to add:-"))
    if (position > create_node.values):                                  #function attribute is created
        print("Out of bound")
    else:
        new_data=input("Enter the number you want to add:-")
        if position==1:                                                  #if the body has to be the first one
            temp=first_linked_list.head_val                              #created the instance of first_linked_list to 
            first_linked_list.head_val=node(new_data)
            first_linked_list.head_val.next_val=temp

        else:
            count=1
            new_linked_list=linked_list()                               #created new object as for inserting a whole new node
            temp=first_linked_list.head_val
            while first_linked_list.head_val.next_val != None:
                count+=1
                if count == position:
                    temp_nextVal=temp.next_val                           #saved the instance of next val that node pointing
                    new_linked_list.head_val=node(new_data)              
                    temp.next_val=new_linked_list.head_val
                    new_linked_list.head_val.next_val=temp_nextVal
                    break
                temp=temp.next_val                                          #pointing temp to the new val as next val of the node
        print("Node added sucessfully")
        print("Updated list:-")
        traverse()                                                           #calling function to show updated list

def search():
    count = 0
    temp=first_linked_list.head_val
    value=input("Enter the value you want to search:-")
    while temp is not None:
        count+=1
        if(temp.data_val == value):
            print("The input value is found which is at position",count)
        temp=temp.next_val 



def delete():
    temp=first_linked_list.head_val
    del_position= int(input("Enter the position you want to delete:-"))
    if del_position > create_node.values:
        print("Out of bound")
    else:
        if del_position == 1:                                           #here we need to make change in first_linked_list because
            first_linked_list.head_val=temp.next_val                    #it is the instance of my class
            traverse()
        else:
            count=0
            while(temp is not None):
                del_count=int(del_position-1)
                count+=1
                if(count == del_count):
                    temp.next_val=temp.next_val.next_val
                temp=temp.next_val
            traverse()
if __name__ == "__main__":
    create_node()                                                   #created node
    traverse()                                                      #shows element of node
    insert()                                                        #insertion of value anywhere user like
    search()                                                        #searching the number and printing its position
    delete()                                                        #delete any node user want to delete
                      






    


    


    



