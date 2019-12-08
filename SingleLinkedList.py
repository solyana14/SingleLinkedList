# this are actual nodes that will be inserted to the linked list
class Queue:
    def __init__(self):
        self.queue = LinkedList()


class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

# the Linked list calss will have th methods to insert,delete, and update nodes

class LinkedList:
    def __init__(self):
        self.count = 0
        self.startNode = None

    def insertAtTheBegining(self, data):
        newNode = Node(data) #create a new node
        newNode.ref = self.startNode #make the reference for the new node the old start node
        self.startNode = newNode
        self.count +=1

    def insertAtTheEnd(self,data):
        newNode = Node(data)
        if self.startNode is None:
            self.startNode = newNode
            self.count +=1
            return
        n = self.startNode
        #search until the end of the linklist
        while n.ref is not None:
            n = n.ref
        n.ref = newNode #make the end of the lists refernece the newNode
        self.count +=1


    def insertAtSomeIndex(self,index,data):
        if index ==1:
            self.insertAtTheBegining(data)

        i = 1
        n = self.startNode
        while i < index -1 and n is not None:
            n = n.ref;
            i +=1

        if n is None:
            print("index out of bound")
        else:
            newNode = Node(data)
            newNode.ref = n.ref
            n.ref = newNode
            self.count += 1

    def insetrAfterSomeItem(self, x ,data):
        newNode = Node(data)
        if self.startNode is None:
            self.startNode = newNode
            self.count += 1
        else:
            n = self.startNode
            while n is not None:
                if n.item == x:
                    break
                n = n.ref
            newNode.ref = n.ref #make old reference of 'x' new reference of new node
            n.ref = newNode; #make reference of old 'x' the new node
            self.count += 1

    def insertBeforeSomeItem(self,x,data):
        newNode = Node(data)
        if self.startNode is None:
            self.startNode = newNode
            self.count += 1
            return

        if self.startNode.item == x:
            # newNode.ref = self.startNode
            # self.startNode.ref= newNode #make the new node the  Newstartnode
            self.insertAtTheBegining(data)
            # self.count += 1

            return

        n = self.startNode
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        newNode.ref = n.ref  # make old reference of 'x' new reference of new node
        n.ref = newNode;  # make reference of old 'x' the new node
        self.count +=1


    def traverseList(self):
        if self.startNode is None:
            print("Empty LInked LIst")
            return
        else:
            n = self.startNode
            while n is not None:
                print(n.item, " ")
                n= n.ref #the next item

    def countItems(self):
        # count=0
        # if self.startNode is None:
        #     print("Empty linked list")
        #     return count
        # else:
        #     n = self.startNode
        #     while n is not None:
        #         count +=1
        #         n=n.ref
        # return count
        return self.count
    def makeNewList(self):
        values = eval(input("how many nodes do you want to create? "))

        if(values ==0):
            print("You don't want to create any nodes")
            return
        for i in range(values):
            node = eval(input("Enter the number you want to enter"))
            self.insertAtTheEnd(node)
        return
    def searchItem(self,x):
        if self.startNode is None:
            print("Empty List")
            return
        n = self.startNode
        while n is not None:
            if n.item == x:
                print("item in list")
                return True
            n = n.ref
        print("item not found")
        return False

    def deleteAtTheStart(self):
        if(self.startNode is None):
            print("list is empty to delete")
            return
        self.startNode = self.startNode.ref
        self.count -=1
        return

    def deleteAtTheEnd(self):
        if self.startNode is None:
            print("list is empty")
        n = self.startNode
        # get the element before the last and make its reference none
        while n.ref.ref is not None:
            n= n.ref
        n.ref = None
        self.count -=1
        return
    def deleteItemByValue(self,item):
        if(self.startNode is None):
            print("List is empty")
            return
        if self.startNode.item == item:
            self.deleteAtTheStart()
            return
        n = self.startNode

        while n.ref is not None:
            if(n.ref.item == item):
                break
            n= n.ref
        if n.ref is None:
            print("item not in the list")
        else:
            n.ref =n.ref.ref
            self.count -=1

    def deleteItemByIndex(self,index):
        if(self.startNode is None):
            print("List is empty")
            return
        n = self.startNode
        i = 1
        while i < index-1 and n is not None:
            print(n.item,"test")
            n=n.ref
            i +=1

        # while i < index - 1 and n is not None:
        #     n = n.ref;
        #     i += 1

        # if n is None:
        #     print("index out of bound")
        # else:
        #     newNode = Node(data)
        #     newNode.ref = n.ref
        #     n.ref = newNode
        #     self.count += 1

    #this is still wierd in mmy head
    def reverseList(self):
        previous = None
        n = self.startNode

        while n is not None:
            next = n.ref
            n.ref = previous
            previous = n
            n = next

        self.startNode =previous
    #This is very important and clear
    def reverseRecursively(self):
        previous = None
        next = None
        current = self.startNode
        while current is not None:
            next = current.ref #save next Node
            current.ref = previous #reverse the current node reference
            previous = current #make previous to current for next iteration
            current = next #make current to next value for next iteration
        return previous #as this is the new head
list = LinkedList()
list.makeNewList()
print(list.reverseRecursively().item)