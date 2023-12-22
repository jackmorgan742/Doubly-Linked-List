from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5): # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        for j in range(5): # repeat a few times to make sure removing final node doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i%2: dll.add_last(i) # odd numbers - add last
                else: dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i%2: self.assertEqual(dll.remove_last(), n-i) # odd numbers: remove last
                else: self.assertEqual(dll.remove_first(), n-2-i) # even numbers: remove first

    # TODO: Add docstrings to and implement the unittests below
    def test_contains(self):
        '''
        tests functionality of the dunder method __contains__
        '''
        linked_lst = DLL(range(10))
        self.assertEqual(True, 5 in linked_lst) #tests contains method
        self.assertEqual(False, 30 in linked_lst)
        self.assertEqual(True, 0 in linked_lst)

        linked_lst.remove_first()  #tests if dict is updating with remove_first
        self.assertEqual(False, 0 in linked_lst)
        
        linked_lst.add_last(11)  #tests if dict is updating with add_last
        self.assertEqual(True, 11 in linked_lst)

    def test_neighbors(self):
        '''
        tests functionality of the neighbors method
        '''
        linked_lst = DLL(range(10))
        self.assertEqual('(None, Node(1))', str(linked_lst.neighbors(0))) #tests head neighbor
        self.assertEqual('(Node(8), None)', str(linked_lst.neighbors(9))) #tests tail neighbor
        self.assertEqual('(Node(4), Node(6))', str(linked_lst.neighbors(5))) #tests middle item neighbor
        with self.assertRaises(RuntimeError):
            linked_lst.neighbors(10) #tests functionality of runtime error implementation (should raise error)

    def test_remove_item(self):
        '''
        tests functionality of the remove_item function
        '''

        linked_lst = DLL(range(10))
        linked_lst.remove_node(0)
        linked_lst2 = DLL(range(10))
        self.assertNotEqual(linked_lst.__len__(), linked_lst2.__len__()) #tests if remove_node is removing a node
        self.assertEqual(False, 0 in linked_lst) #tests the head item was removed
        self.assertEqual(True, 1 in linked_lst) #tests the next node has the item

        linked_lst3 = DLL(range(10))
        linked_lst3.remove_node(9)
        self.assertNotEqual(linked_lst3.__len__(), linked_lst2.__len__()) #tests if remove_node is removing a node
        self.assertEqual(False, 9 in linked_lst3) #tests the tail item was removed
        self.assertEqual(True, 8 in linked_lst3) #tests the previous node has the item

        linked_lst4 = DLL(range(10))
        linked_lst4.remove_node(5)
        self.assertNotEqual(linked_lst4.__len__(), linked_lst2.__len__()) #tests if remove_node is removing a node
        self.assertEqual(False, 5 in linked_lst4) #tests the tail item was removed
        self.assertEqual(True, 4 in linked_lst4) #tests the previous node has the item
        self.assertEqual(True, 6 in linked_lst4) #tests the next node has the item

        with self.assertRaises(RuntimeError):
            linked_lst4.remove_node(10) #tests functionality of runtime error implementation (should raise error)

unittest.main()
