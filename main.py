import random, builtins
builtins.random = random

"""
HW01 — Library Barcodes → Book Titles (Chaining)

Implement a tiny hash table with chaining.
Do not add type hints. Use only the standard library.
"""

def make_table(m):
    """Return a new table with m empty buckets (lists)."""
    return [[] for _ in range(m)]

def hash_basic(s):
    """Return a simple integer hash for string s."""
    total = 0
    for ch in s:
        total += ord(ch)
    return total

def put(t, key, value):
    """Insert or overwrite (key, value) in table t using chaining."""
    index = hash_basic(key) % len(t)
    bucket = t[index]

    # Overwrite if key already exists
    for pair in bucket:
        if pair[0] == key:
            pair[1] = value
            return

    # Otherwise append new pair
    bucket.append([key, value])

def get(t, key):
    """Return value for key or None if not present."""
    index = hash_basic(key) % len(t)
    bucket = t[index]

    for pair in bucket:
        if pair[0] == key:
            return pair[1]
    return None

def has_key(t, key):
    """Return True if key exists in table t; else False."""
    index = hash_basic(key) % len(t)
    bucket = t[index]

    for pair in bucket:
        if pair[0] == key:
            return True
    return False

def size(t):
    """Return total number of stored pairs across all buckets."""
    count = 0
    for bucket in t:
        count += len(bucket)
    return count

if __name__ == "__main__":
    pass