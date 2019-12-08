from SingleLinkedList import *
def main():
    newLinkedList = LinkedList()
    # insert at the beginning of the list
    # newLinkedList.insertAtTheEnd(1)
    # newLinkedList.insertAtTheEnd(2)
    # newLinkedList.insertAtTheEnd(3)
    # newLinkedList.traverseList()
    #
    # # insert at the beginning of the list
    # newLinkedList.insertAtTheBegining(20)
    # newLinkedList.traverseList()
    #
    # # isert before some element
    # newLinkedList.insertBeforeSomeItem(1,11)
    # newLinkedList.traverseList()
    # # insert after some element
    # newLinkedList.insetrAfterSomeItem(2,22)
    # newLinkedList.traverseList()
    # print("Total items in the linked list = ", newLinkedList.countItems())
    #
    # print(newLinkedList.searchItem(2))
    # print(newLinkedList.searchItem(33))


    #testing delete
    newLinkedList.insertAtTheEnd(10)
    newLinkedList.insertAtTheEnd(20)
    newLinkedList.insertAtTheEnd(30)
    newLinkedList.insertAtTheEnd(40)
    newLinkedList.insertAtTheEnd(50)
    newLinkedList.traverseList()

    # testing delete
    # print(newLinkedList.countItems())
    #
    # newLinkedList.deleteAtTheEnd()
    # newLinkedList.traverseList()
    # print(newLinkedList.countItems())
    #
    # newLinkedList.deleteAtTheStart()
    # newLinkedList.traverseList()
    # print(newLinkedList.countItems())
    #
    # newLinkedList.deleteItemByValue(20)
    # newLinkedList.traverseList()
    # print(newLinkedList.countItems())

    newLinkedList.reverseList()
    newLinkedList.traverseList()
main()