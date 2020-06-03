class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'

    


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    def find(self, key):
        cur = self.head

        while cur is not None:
            if cur.key == key:
                return cur
            
            cur = cur.next
        
        return None
    
    def delete(self, key):
        cur = self.head

        if cur.key == key:
            self.head = self.head.next
            return cur

        prev = cur
        cur = cur.next

        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return cur
            
            else:
                prev = prev.next
                cur = cur.next
        
        return None
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [LinkedList()] * self.capacity 
        self.load = 0
        # this gives methods access to the array 


        # print("hello", self.capacity)
        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity



    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        loadFactor = self.load / self.capacity
        
        if loadFactor > 0.7:
            new_capacity = self.capacity * 2
            self.resize(new_capacity)

        if loadFactor < 0.2:
            new_capacity = self.capacity / 2

            if new_capacity < 8:
                new_capacity = 8

        
        return loadFactor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        
        return hash


    def hash_index(self, key): # hashing function
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # create key 
        # self.hash stores it at a specific index within your created array
        # the key now points at an index
        # then add a value to the key to create key/value pair

        # get index of the passed in key
        # Find the slot for the given key
        index = self.hash_index(key) 

        # Search the LinkedList
        current = self.storage[index].find(key)
        if current is not None:
            current.value = value
        else:
            self.storage[index].insert_at_head(HashTableEntry(key, value))
            self.load += 1

        # store the value at the index
        # self.storage[index] = HashTableEntry(key, value)
        




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        

        if not key:
            print("Key does not exist")
        else:
            index = self.hash_index(key)
            self.load -= 1
            return self.storage[index].delete(key)
            
            

        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        hash_value = self.storage[index]

        if self.storage[index] is not None:
            desired = hash_value.find(key)
            if desired is not None:
                return desired.value
        
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # holding a copy of the original hashtable
        holding = self.storage.copy()

        # overwrites old storage to be bigger
        self.storage = [LinkedList()] * new_capacity

        # sets the capacity (actual number) to the new size
        self.capacity = new_capacity

        for each in holding:
            current = each.head

            while current is not None:
                self.put(current.key, current.value)
                current = current.next
                

        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
