EMPTY = object()
DELETED = object()

class HashMap:
    def __init__(self, m=8):
        """Initialize hash map with initial table size m."""
        self.table = [EMPTY] * m
        self.count = 0

    def _hash(self, key):
        return hash(key) % len(self.table)

    def _resize(self):
        """Double the table size and reinsert all active key-value pairs."""
        old_table = self.table
        new_size = len(old_table) * 2
        self.table = [EMPTY] * new_size
        self.count = 0
        for entry in old_table:
            if entry is not EMPTY and entry is not DELETED:
                k, v = entry
                self.put(k, v)

    def put(self, key, value):
        if self.count / len(self.table) >= 0.7:
            self._resize()

        index = self._hash(key)
        first_deleted = None

        for i in range(len(self.table)):
            probe = (index + i) % len(self.table)
            slot = self.table[probe]

            if slot is EMPTY:
                if first_deleted is not None:
                    self.table[first_deleted] = (key, value)
                else:
                    self.table[probe] = (key, value)
                self.count += 1
                return

            elif slot is DELETED:
                if first_deleted is None:
                    first_deleted = probe

            elif slot[0] == key:
                # Overwrite existing key
                self.table[probe] = (key, value)
                return

        # If we found a deleted slot earlier
        if first_deleted is not None:
            self.table[first_deleted] = (key, value)
            self.count += 1

    def get(self, key):
        index = self._hash(key)
        for i in range(len(self.table)):
            probe = (index + i) % len(self.table)
            slot = self.table[probe]

            if slot is EMPTY:
                return None
            elif slot is DELETED:
                continue
            elif slot[0] == key:
                return slot[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i in range(len(self.table)):
            probe = (index + i) % len(self.table)
            slot = self.table[probe]

            if slot is EMPTY:
                return False
            elif slot is DELETED:
                continue
            elif slot[0] == key:
                self.table[probe] = DELETED
                self.count -= 1
                return True
        return False

    def __len__(self):
        return self.count
