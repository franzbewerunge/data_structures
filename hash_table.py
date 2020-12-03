class HashItem: 
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 

class HashTable: 
    
    def __init__(self): 
        self.size = 256 
        self.slots = [None for i in range(self.size)] 
        self.count = 0 
    
    def _hash(self, key): 
        mult = 1 
        hv = 0 
        for ch in key: 
            # Multiply to reduce hash collisions
            hv += mult * ord(ch) 
            mult += 1 
        
        # Return as index within of array size
        return hv % self.size
        
    def put(self, key, value):

        item = HashItem(key,value)
        h = self._hash(key)
        
        # Loop as long until we find empty slot
        while self.slots[h] is not None:

            if self.slots[h].key is key:
                break

            h = (h + 1) % self.size
        
        if self.slots[h] is None:
            self.count += 1
            self.slots[h] = item
    
    def get(self, key, item = None):
        
        h = self._hash(key)
        
        while self.slots[h] is not None:

            if self.slots[h].key is key:
                return self.slots[h].value
                
            h = (h + 1) % self.size

        # Return None if key is not found
        return None        
