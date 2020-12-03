class HashItem:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class ChainedHashTable:

    def __init__(self):
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0
        self.load_balance = 0

    def _hash(self, key):
        
        hash_value = 0
        multiplier = 1

        for character in key:
            hash_value += multiplier * ord(character)
        
        return hash_value % self.size

    def set(self, key, value):

        item = HashItem(key, value)

        hash_key = self._hash(item.key)

        while self.slots[hash_key] is not None:

            # Check list of slots with existing keys
            for item in self.slots[hash_key]:

                if item.key == key:
                    return

            # Append key to slots if not found already
            self.slots[hash_key].append(item)
            break
        

        if self.slots[hash_key] is None:

            # Add list with item to empty slot 
            self.slots[hash_key] = [item]
            self.count += 1
        
        # Log current Load Balance on hash table 
        self.load_balance =  round(len([element for element in self.slots if element is not None]) / self.size, 2)
        print(f'Load Balance Currently at {self.load_balance}')

    def get(self, key):

        hash_key = self._hash(key)

        # Check list of slots with existing keys
        for item in self.slots[hash_key]:
            
            if item.key == key:         
                return item.key
            
        return None
